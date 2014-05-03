from evdev import InputDevice, list_devices, \
                  ecodes, categorize, UInput
import math, sys
import pyperclip

devices = map(InputDevice, list_devices())
for device in devices:
 if device.name.count('keyboard') > 0:
  dev = InputDevice(device.fn)

keyList = []
inputMode = 0
keyAppendHistory = 0
maxKeyAppendHistory = 0
letters = ''
originalPaste = ''
newUI = UInput()

lArray = []
ccArray = []
cinFile = open('cj-ext.cin', 'r')
for readLine in cinFile:
 if 2 == len(readLine.split()):
  lArray.append(readLine.split()[0])
  ccArray.append(readLine.split()[1])
cinFile.close()

def display_letter_cc(letters, ccList, event = None):
 if None != event and \
    'KEY_BACKSPACE' == event.keycode and 1 == event.keystate:
  sys.stdout.write('%-4s<-- ' %letters)
 else:
  sys.stdout.write('%-8s' %letters)
 if [] != ccList:
  for ccListIndex in range(len(ccList)):
   sys.stdout.write(str(ccListIndex + 1) + \
   '.' + ccList[ccListIndex] + ' ')
 sys.stdout.write('\n')

def switch_grab(event, inputMode):
 global letters
 global originalPaste
 global keyAppendHistory
 global maxKeyAppendHistory
 if inputMode > 0 and 0 == keyAppendHistory:
  dev.grab()
  newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 0)
  newUI.syn()
  print('---Start---')
  originalPaste = pyperclip.paste()
  maxKeyAppendHistory = 0
 elif 0 == inputMode and 1 == event.keystate:
  dev.ungrab()
  print('---Suspend---')
  pyperclip.copy(originalPaste)
  maxKeyAppendHistory = 0
  letters = ''

def match_cc(letters):
 ccList = []
 if '' != letters:
  ccCount = lArray.count(letters)
  cinIndex = 0
  while (ccCount):
   cinIndex += lArray[cinIndex:].index(letters)
   ccList.append(ccArray[cinIndex])
   cinIndex += 1
   ccCount -= 1
 return ccList

def input_cc(ccIndex, ccList, addLetter):
 global letters
 global inputMode
 global originalPaste
 if '' != addLetter:
  display_letter_cc(letters, ccList)
 if 2 == inputMode and 0 == ccIndex and [] == ccList:
  print('---Not match! Empty---')
  letters = ''
 elif ccIndex > -2 and ccIndex < len(ccList):
  print('Entry:  ' + ccList[ccIndex])
  letters = ''
  pyperclip.copy(ccList[ccIndex])
  newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 1)
  newUI.write(ecodes.EV_KEY, ecodes.KEY_V, 1)
  newUI.write(ecodes.EV_KEY, ecodes.KEY_V, 0)
  newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 0)
  newUI.syn()

def switch_input_mode(event):
 global inputMode
 global keyAppendHistory
 global maxKeyAppendHistory
 global keyList
 if 1 == event.keystate:
  keyList.append(event.keycode)
  keyAppendHistory += 1
  maxKeyAppendHistory = keyAppendHistory
 elif 0 == event.keystate and keyAppendHistory > 0:
  keyAppendHistory -= 1
 if 2 == maxKeyAppendHistory:
  if 1 == keyList.count('KEY_LEFTCTRL') and \
     1 == keyList.count('KEY_SPACE') and \
     1 == math.fabs(inputMode * 2 - 1):
   inputMode = math.fabs(inputMode - 1)
   switch_grab(event, inputMode)
  elif 1 == keyList.count('KEY_RIGHTCTRL') and \
     1 == keyList.count('KEY_SPACE') and \
     1 == math.fabs(inputMode - 1):
   inputMode = math.fabs(math.fabs(inputMode * 2 - 1) - 3)
   switch_grab(event, inputMode)
 if 0 == keyAppendHistory:
  keyList = []

def keycode_to_letter(event):
 addLetter = ''
 if 1 == range(16, 26).count(event.scancode) or \
    1 == range(30, 39).count(event.scancode) or \
    1 == range(44, 51).count(event.scancode):
  addLetter = event.keycode[-1].lower()
 return addLetter

def select_or_input(event):
 global inputMode
 global letters
 ccIndex = -2
 if inputMode > 0:
  addLetter = keycode_to_letter(event)
  if '' != addLetter:
   if len(letters) < 5 and 1 == event.keystate:
    letters += addLetter
   else:
    addLetter = ''
  elif '' == letters:
   newUI.write(ecodes.EV_KEY, event.scancode, event.keystate)
   newUI.syn()
  elif '' != letters:
   if 'KEY_ESC' == event.keycode:
    letters = ''
    print('---Empty---')
   elif 'KEY_SPACE' == event.keycode:
    ccIndex = 0
   elif 1 == range(2, 12).count(event.scancode):
    ccIndex = event.scancode - 2
   elif 'KEY_BACKSPACE' == event.keycode and 1 == event.keystate:
    letters = letters[0:-1]
    display_letter_cc(letters, match_cc(letters), event)
   else:
    newUI.write(ecodes.EV_KEY, event.scancode, event.keystate)
    newUI.syn()
  if 1 == event.keystate:
   ccList = match_cc(letters)
   input_cc(ccIndex, ccList, addLetter)

print('---Welcome---')
print('---[Ctrl + Space] to start---')
for event in dev.read_loop():
 if event.type == ecodes.EV_KEY:
  event = categorize(event)
  switch_input_mode(event)
  select_or_input(event)
