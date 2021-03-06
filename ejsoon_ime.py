# coding=utf8                                       #
# --------------------------------------------------#
# This is an OPEN SOURCE input method, license:     #
#       ---GNU version 2.0---                       #
# --------------------------------------------------#
# Only a python script but evdev is needed.         #
# Only for linux gnome up to now(2015 12 5).        #
# Only I am the first and the last user.            #
# It is really the BEST CangJie ime for me!         #
# --------------------------------------------------#
# This project include a cin table, you can find    #
# the original cj-ext.cin from this site:           #
#   "https://github.com/yahoo/KeyKey/blob/master/   #
#    YahooKeyKey-Source-1.1.2528/DataTables/"       #
# But the table must be sorted as the provided one. #
# --------------------------------------------------#
# Dependence:                                       #
#   python (2.x or 3.x)                             #
#   pyperclip (1.5.4 or newer)                      #
#   evdev (0.4.4 or newer)                          #
# --------------------------------------------------#
# In the Ubuntu12.04 or newer,you can do like:      #
# Download pyperclip.py from:                       #
#   https://pypi.python.org/pypi/pyperclip          #
# Then install it by python setuptools.             #
# And then install evdev:                           #
#   sudo apt-get install python-evdev               #
# Go to the ejsoon_ime.py folder, do this:          #
#   sudo python ejsoon_ime.py                       #
# Have fun and smile.                               #
# --------------------------------------------------#
# {Ctrl} + {space} = start / stop                   #
# left{Alt} = terminal input mode                   #
# {Ctrl} + {z} = quit (DO NOT QUIT BEFORE STOP!!)   #
# --------------------------------------------------#
from evdev import InputDevice, list_devices, ecodes, categorize, UInput
import math, sys
import pyperclip

devices = map(InputDevice, list_devices())
for device in devices:
 if device.name.count('keyboard') > 0 or \
    device.name.count('Keyboard') > 0:
  dev = InputDevice(device.fn)

inputMode = 0
isModeChange = 0
isFirst = 1
isShift = 0
isUpper = 0

keyList = []
keyAppendHistory = 0
maxKeyAppendHistory = 0

letters = ''
eLetters = ''
addLetter = ''
ccList = []
ccIndex = -1
selectPage = 0
inputStatus = -3
newUI = UInput()

lArray = []
ccArray = []
cinFile = open('yahooCJ.cin', 'r')
for readLine in cinFile:
 if 2 == len(readLine.split()):
  lArray.append(readLine.split()[0])
  ccArray.append(readLine.split()[1])
 else:
  lArray.append('zxaa')
  ccArray.append('　')
cinFile.close()

isShiftString = ['_', 's', 'i']

def input_init(event):
 global isModeChange, inputStatus, letters, eLetters, addLetter, \
        selectPage, ccIndex
 if 1 == math.fabs(inputStatus - 1):
  letters = ''
  eLetters = ''
 if 2 != math.fabs(inputStatus + 1) or '' != addLetter or isModeChange > 0:
  selectPage = 0
 isModeChange = 0
 inputStatus = -3
 ccIndex = -1

def display(displayString):
 backSpaceCount = 36
 while backSpaceCount:
  sys.stdout.write('\b')
  backSpaceCount -= 1
 sys.stdout.write(displayString)
 sys.stdout.flush()

def display_manage(event):
 global inputMode, isModeChange, letters, addletter, \
        selectPage, inputStatus, isShift, isShiftString
 displayString = ''
 if inputMode > 0 and ('' !=  addLetter or inputStatus > -3 or \
    1 == isModeChange):
  displayString = '[' + str(int(inputMode)) + isShiftString[isShift] + ']'
  if 1 == math.fabs(1 - inputStatus):
   displayLetters = ''
  else:
   displayLetters = letters
  if len(displayLetters) > 0 and len(displayLetters) < 6:
   for lettersIndex in range(0, len(displayLetters)):
    if 'z' == letters[lettersIndex]:
     displayString += match_cc('hjwg')[0]
    elif 'x' == letters[lettersIndex]:
     displayString += match_cc('toog')[0]
    else:
     displayString += match_cc(letters[lettersIndex])[0]
  if 5 - len(displayLetters) > 0:
   for lettersIndex in range(0, 5 - len(displayLetters)):
    displayString += match_cc('zxaa')[0]
  displayString += '{'
  if '' != displayLetters and len(displayLetters) < 6:
   if len(match_cc(displayLetters)) > 4 * selectPage + 3:
    for ccIndex in range(4 * selectPage, 4 * selectPage + 4):
     displayString += str(ccIndex % 4 + 1) + '.' + \
                      match_cc(displayLetters)[ccIndex] + ' '
   else:
    for ccIndex in range(4 * selectPage, len(match_cc(displayLetters))):
     displayString += str(ccIndex % 4 + 1) + '.' + \
                      match_cc(displayLetters)[ccIndex] + ' '
    for ccIndex in range(len(match_cc(displayLetters)), 4 * selectPage + 4):
     displayString += str(ccIndex % 4 + 1) + '.' + \
                      match_cc('zxaa')[0] + ' '
  elif len(displayLetters) > 5:
    displayString += '<' + displayLetters + '>'
  else:
   for ccIndex in range(0, 4):
    displayString += str(ccIndex % 4 + 1) + '.' + \
                     match_cc('zxaa')[0] + ' '
  displayString += '}'
  display(displayString)
 elif 0 == inputMode and isModeChange > 0:
  displayString += '---Ctrl + Space => Start---         '
  display(displayString)

def keycode_to_letter(event):
 addLetter = ''
 if 1 == range(16, 26).count(event.scancode) or \
    1 == range(30, 39).count(event.scancode) or \
    1 == range(44, 51).count(event.scancode):
  addLetter = event.keycode[-1].lower()
 return addLetter

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

def input_cc():
 global letters, eLetters, ccIndex, inputStatus, isShift, \
        isFirst, isUpper
 if 0 == inputStatus:
  pyperclip.copy(match_cc(letters)[ccIndex])
 elif 2 == inputStatus:
  if 1 == isUpper:
   eLetters = str.upper(eLetters)
   isUpper = 0
  pyperclip.copy(eLetters)
 if isFirst > 0:
  newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 0)
  newUI.write(ecodes.EV_KEY, int(42 + (inputMode - 1 ) * 12), 0)
  dev.ungrab()
 if isShift > 0:
  newUI.write(ecodes.EV_KEY, int(42 + (inputMode - 1 ) * 12), 1)
 newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 1)
 newUI.write(ecodes.EV_KEY, ecodes.KEY_V, 1)
 newUI.write(ecodes.EV_KEY, ecodes.KEY_V, 0)
 newUI.write(ecodes.EV_KEY, int(29 + (inputMode - 1 ) * 68), 0)
 if isShift > 0:
  newUI.write(ecodes.EV_KEY, int(42 + (inputMode - 1 ) * 12), 0)
 if isFirst > 0:
  isFirst = 0
  dev.grab()
 newUI.syn()

def input_manage(event):
 global inputMode, inputStatus, isFirst, isShift, isUpper, \
        letters, eLetters, addLetter, ccIndex, selectPage
 if inputMode > 0:
  addLetter = keycode_to_letter(event)
  if '' != addLetter and 1 != keyList.count('KEY_LEFTCTRL') and \
     1 != keyList.count('KEY_LEFTSHIFT') and \
     1 != keyList.count('KEY_LEFTALT'):
   #if (len(letters) < 5 or 2 == inputMode) and 1 == event.keystate:
   if 1 == event.keystate:
    eLetters += addLetter
    if len(letters) < 5:
     letters += addLetter
    else:
     addLetter = ''
  elif '' == letters:
   newUI.write(ecodes.EV_KEY, event.scancode, event.keystate)
   newUI.syn()
  elif '' != letters:
   if 'KEY_ESC' == event.keycode and 1 == event.keystate:
    letters = ''
    eLetters = ''
    inputStatus = -2
   elif 'KEY_BACKSPACE' == event.keycode:
    if 1 == event.keystate:
     letters = letters[0:-1]
     eLetters = eLetters[0:-1]
     inputStatus = -1
   elif 'KEY_SPACE' == event.keycode:
    if 1 == event.keystate:
     ccIndex = 4 * selectPage
     if len(match_cc(letters)) > ccIndex:
      inputStatus = 0
     else:
      if 2 == inputMode:
       letters = ''
       eLetters = ''
       inputStatus = -2
      ccIndex = -1
   elif 1 == range(3, 6).count(event.scancode):
    ccIndex = event.scancode - 2 + 4 * selectPage
    if len(match_cc(letters)) > ccIndex:
     inputStatus = 0
    else:
     ccIndex = -1
   elif 2 == math.fabs(4 - event.scancode):
    if 1 == event.keystate:
     if 6 == event.scancode and len(match_cc(letters)) > 4 * (selectPage + 1):
      selectPage += 1
      inputStatus = 1
     if 2 == event.scancode and selectPage > 0:
      selectPage -= 1
      inputStatus = 1
   elif 'KEY_ENTER' == event.keycode:
    if 1 == event.keystate:
     inputStatus = 2
   elif 'KEY_LEFTSHIFT' == event.keycode:
    if 1 == event.keystate:
     isUpper = 1
    elif 0 == event.keystate:
     isUpper = 0
   else:
    newUI.write(ecodes.EV_KEY, event.scancode, event.keystate)
    newUI.syn()
  if 1 == event.keystate and 1 == math.fabs(inputStatus - 1):
   input_cc()

def switch_grab(event):
 global inputMode, isModeChange, isShift, isFirst, letters, \
        keyAppendHistory, maxKeyAppendHistory
 if inputMode > 0 and 0 == keyAppendHistory:
  dev.grab()
  isModeChange = 1
 elif 0 == inputMode and 1 == event.keystate:
  dev.ungrab()
  isModeChange = 1
  maxKeyAppendHistory = 0
  letters = ''
  eLetters = ''
  isShift = 0
  isFirst = 2

def switch_input_mode(event):
 global inputMode, isModeChange, isShift, keyAppendHistory, \
        maxKeyAppendHistory, keyList
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
   switch_grab(event)
  elif 1 == keyList.count('KEY_RIGHTCTRL') and \
     1 == keyList.count('KEY_SPACE') and \
     1 == math.fabs(inputMode - 1):
   inputMode = math.fabs(math.fabs(inputMode * 2 - 1) - 3)
   switch_grab(event)
 elif 1 == maxKeyAppendHistory and 0 == event.keystate:
  if 1 == keyList.count('KEY_LEFTALT') and isShift < 2:
   isShift += 1
   isModeChange = 1
   if 2 == isShift:
    newUI.write(ecodes.EV_KEY, ecodes.KEY_I, 1)
    newUI.write(ecodes.EV_KEY, ecodes.KEY_I, 0)
    newUI.syn()
  elif 1 == keyList.count('KEY_RIGHTALT') and isShift > 0:
   isShift = 0
   isModeChange = 1
 if 0 == keyAppendHistory:
  keyList = []

print("---Welcome to ejsoon IME---")
sys.stdout.write('---Ctrl + Space => Start---         ')
sys.stdout.flush()
for event in dev.read_loop():
 if event.type == ecodes.EV_KEY:
  event = categorize(event)
  switch_input_mode(event)
  input_manage(event)
  display_manage(event)
  input_init(event)
