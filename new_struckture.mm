<map version="freeplane 1.2.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="if event == key" ID="ID_1723255651" CREATED="1283093380553" MODIFIED="1399392053474"><hook NAME="MapStyle">

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default" MAX_WIDTH="600" COLOR="#000000" STYLE="as_parent">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="9"/>
<node TEXT="sys" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="left" ID="ID_951464906" CREATED="1399393590625" MODIFIED="1399396594900" HGAP="59" VSHIFT="-122">
<icon BUILTIN="checked"/>
<hook NAME="FreeNode"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      lArray
    </p>
    <p>
      ccArray
    </p>
    <p>
      newUI
    </p>
  </body>
</html>
</richcontent>
</node>
<node TEXT="(out)" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="left" ID="ID_988939860" CREATED="1399393538682" MODIFIED="1399459739654" HGAP="-290" VSHIFT="-85">
<hook NAME="FreeNode"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="5" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1899456153" STARTINCLINATION="40;-5;" ENDINCLINATION="31;-30;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<node ID="ID_1868180094" CREATED="1399419083947" MODIFIED="1399467438524" HGAP="-60" VSHIFT="60"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#ff0000">isModeChange</font>
    </p>
  </body>
</html>

</richcontent>
</node>
<node TEXT="inputMode" ID="ID_1189333007" CREATED="1399459709046" MODIFIED="1399459716980" HGAP="-40"/>
<node TEXT="isFirst" ID="ID_452452911" CREATED="1399459669897" MODIFIED="1399459724123" HGAP="-40"/>
<node TEXT="isShift" ID="ID_603521464" CREATED="1399459677589" MODIFIED="1399459725715" HGAP="-50" VSHIFT="-10"/>
</node>
<node TEXT="key code to letter()" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="left" ID="ID_1924562326" CREATED="1399392460533" MODIFIED="1399459559101" HGAP="-645" VSHIFT="25">
<hook NAME="FreeNode"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="5" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1131887828" STARTINCLINATION="50;-6;" ENDINCLINATION="50;4;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="letters" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="left" ID="ID_676187896" CREATED="1399393572433" MODIFIED="1399420211640" HGAP="-456" VSHIFT="141">
<hook NAME="FreeNode"/>
<cloud COLOR="#f23e3e" SHAPE="ARC"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#ff0000" WIDTH="5" TRANSPARENCY="255" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_676187896" STARTINCLINATION="52;58;" ENDINCLINATION="52;58;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="switch input mode(event)" POSITION="right" ID="ID_166643725" CREATED="1399392055778" MODIFIED="1399420290150" VSHIFT="-70">
<edge COLOR="#ff0000"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      keyList
    </p>
    <p>
      keyAH
    </p>
    <p>
      maxKeyAH
    </p>
  </body>
</html>
</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_512218200" STARTINCLINATION="111;-29;" ENDINCLINATION="-22;-27;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<node TEXT="switch grab(inputMode)" ID="ID_1857614057" CREATED="1399392371546" MODIFIED="1399459811519" HGAP="70" VSHIFT="-50"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      orginP
    </p>
  </body>
</html>

</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_988939860" STARTINCLINATION="19;18;" ENDINCLINATION="-34;-13;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
<node TEXT="inputMode" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_512218200" CREATED="1399395393794" MODIFIED="1399399622441" HGAP="530" VSHIFT="-27">
<hook NAME="FreeNode"/>
<cloud COLOR="#45d724" SHAPE="ARC"/>
</node>
<node TEXT="input manage(event)" POSITION="right" ID="ID_1899456153" CREATED="1399392069642" MODIFIED="1399467440767" HGAP="40" VSHIFT="10">
<edge COLOR="#0000ff"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1131887828" STARTINCLINATION="57;-3;" ENDINCLINATION="-60;-9;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1899456153" STARTINCLINATION="405;104;" ENDINCLINATION="405;104;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="add letter" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_1131887828" CREATED="1399398283553" MODIFIED="1399420215452" HGAP="511" VSHIFT="63">
<hook NAME="FreeNode"/>
<cloud COLOR="#2de625" SHAPE="ARC"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#df3535" WIDTH="5" TRANSPARENCY="255" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1131887828" STARTINCLINATION="2;46;" ENDINCLINATION="2;46;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="inputType" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_1891090553" CREATED="1399393630776" MODIFIED="1399415681353" HGAP="-140" VSHIFT="84">
<icon BUILTIN="idea"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      (1)add letter
    </p>
    <p>
      (2)input function
    </p>
    <p>
      (0)outControl
    </p>
  </body>
</html>
</richcontent>
<hook NAME="FreeNode"/>
<node TEXT="no letter" ID="ID_1624021960" CREATED="1399396501553" MODIFIED="1399396616623" HGAP="-210">
<node TEXT="(1)add letter&#xa;(0)outControl" ID="ID_1302566419" CREATED="1399396631373" MODIFIED="1399396878784" HGAP="-170">
<hook NAME="FreeNode"/>
</node>
</node>
<node TEXT="have letter(s)" ID="ID_1726765224" CREATED="1399396542043" MODIFIED="1399396990144" HGAP="-250" VSHIFT="30">
<node TEXT="(1)add letter" ID="ID_1351053548" CREATED="1399396676470" MODIFIED="1399396997990" HGAP="-200" VSHIFT="40"/>
<node TEXT="(2)input function" ID="ID_1067583761" CREATED="1399396867466" MODIFIED="1399396912767" HGAP="-200">
<node TEXT="esc" ID="ID_248219878" CREATED="1399396926239" MODIFIED="1399414376012" HGAP="-10" VSHIFT="90"/>
<node TEXT="back space" ID="ID_1974319977" CREATED="1399396884144" MODIFIED="1399400200773" HGAP="0"/>
<node TEXT="space" ID="ID_766174761" CREATED="1399396931464" MODIFIED="1399400206255"/>
<node TEXT="number" ID="ID_651816961" CREATED="1399398880009" MODIFIED="1399400207863" HGAP="30"/>
<node TEXT="enter" ID="ID_1931452491" CREATED="1399400173189" MODIFIED="1399400215872" HGAP="40" VSHIFT="-10"/>
</node>
</node>
</node>
<node TEXT="display manage()" POSITION="right" ID="ID_220922135" CREATED="1399392126293" MODIFIED="1399420265946" HGAP="-60" VSHIFT="60">
<edge COLOR="#00ff00"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      ---ctrl +space---_si
    </p>
    <p>
      [12Ss]
    </p>
    <p>
      [12Ss]a
    </p>
  </body>
</html>
</richcontent>
<node TEXT="isDisplayChange" ID="ID_1926985566" CREATED="1399411321766" MODIFIED="1399420682364" VSHIFT="-1"><richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p style="margin-top: 0">
      isModeChange =true
    </p>
    <p style="margin-top: 0">
      inS&gt;-3
    </p>
    <p style="margin-top: 0">
      addL!=''
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="inputStatus" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_1022452851" CREATED="1399398538492" MODIFIED="1399419920762" HGAP="667" VSHIFT="149">
<hook NAME="FreeNode"/>
<cloud COLOR="#db3131" SHAPE="ARC"/>
<hook NAME="FirstGroupNode"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      (-3) -2 -1 0 1 2
    </p>
  </body>
</html>
</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#ee3636" WIDTH="5" TRANSPARENCY="255" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1022452851" MIDDLE_LABEL="1" STARTINCLINATION="22;56;" ENDINCLINATION="22;56;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#e23636" WIDTH="5" TRANSPARENCY="255" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1022452851" MIDDLE_LABEL="0" STARTINCLINATION="-48;83;" ENDINCLINATION="-48;83;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="backSC" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_227232913" CREATED="1399393627344" MODIFIED="1399418915911" HGAP="202" VSHIFT="232">
<hook NAME="FreeNode"/>
</node>
<node TEXT="match cc(letters)" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_266740505" CREATED="1399392529083" MODIFIED="1399420207117" HGAP="418" VSHIFT="233">
<hook NAME="FreeNode"/>
<cloud COLOR="#e51a1a" SHAPE="ARC"/>
</node>
<node TEXT="selectPage" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_974391855" CREATED="1399415945665" MODIFIED="1399419881973" HGAP="716" VSHIFT="261">
<hook NAME="FreeNode"/>
<cloud COLOR="#ed2727" SHAPE="ARC"/>
</node>
<node TEXT="dString" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_1797133072" CREATED="1399393629720" MODIFIED="1399418918382" HGAP="203" VSHIFT="270">
<hook NAME="FreeNode"/>
</node>
<node TEXT="ccIndex" LOCALIZED_STYLE_REF="defaultstyle.floating" POSITION="right" ID="ID_457822174" CREATED="1399416518543" MODIFIED="1399419877853" HGAP="607" VSHIFT="274">
<hook NAME="FreeNode"/>
<cloud COLOR="#ee3a3a" SHAPE="ARC"/>
</node>
</node>
</map>
