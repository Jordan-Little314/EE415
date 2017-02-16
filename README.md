# EE415/416

![Washington State University](http://i.imgur.com/SirybLo.jpg)  
![Appium](http://i.imgur.com/9r3xOF8.png)

Fall '16/Spring '17 Washington State University Computer/Electrical Engineering Senior design.  Team Surah working along side Pacific Northwest National Laboratories -
"Emulating use behavior on Android/iOS devices"

This readme will detail how to successfully download and install the necessary programs to get started with automated mobile testing using Appium.

## Using Appium on OSX and getting it working with iOS

'This set-up is assuming you are trying to configure Appium with the most up to date version of iOS and XCode, which as of writing this guide are iOS 10.2 and XCode 8.2.1'

1. Go to [Appium's](Appium.io) website and press the **Download Appium** button. It should automatically start a .dmg file download, install it as you would any other file.

2. Now we need to do some downloads through the terminal:  
'$ brew update
$ brew install node
$ npm install -g npm
$ npm install -g appium
$ npm install -g appium-doctor'

3. Everything should be in place, now it's just a matter of linking it up. ![This link](http://toolsqa.com/mobile-automation/appium/setup-appium-on-mac/) shows how to get the Appium GUI working properly. Note for our installation, it it not necessary to do steps 6 or 7.

4. In order to use the Appium GUI inspector, we need to run the server through our terminal. Do not click "Launch" on the GUI! Instead from the terminal run:  
'$ ./node_modules/.bin/appium'  
When the server starts, you are now free to press the inspector on the GUI (the magnifying glass icon). It should boot up the emulator you specified in the iOS settings and download your app to it. You can now record automation scripts!
