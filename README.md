# EE415/416

![Washington State University](http://i.imgur.com/SirybLo.jpg) ![Appium](http://i.imgur.com/9r3xOF8.png)

Fall '16/Spring '17 Washington State University Computer/Electrical Engineering Senior design.  Team Surah working along side Pacific Northwest National Laboratories -
"Emulating user behavior on Android/iOS devices"

This readme will detail how to successfully download and install the necessary programs to get started with automated mobile testing using Appium.

## Using Appium on OSX and getting it working with iOS

This set-up is assuming you are trying to configure Appium with the most up to date version of iOS and XCode, which as of writing this guide are iOS 10.3 and XCode 8.3

1. Go to [Appium's](Appium.io) website and press the **Download Appium** button. It should automatically start a .dmg file download, install it as you would any other file.
  * [This link](http://toolsqa.com/mobile-automation/appium/setup-appium-on-mac/) shows how to get the Appium GUI working properly. Note for our installation, it it not necessary to do steps 6 or 7.

2. Now we need to do some downloads through the terminal:  
```
$ brew update
$ brew install node
$ npm install -g npm
$ npm install -g appium
```
  * Note that running `appium -v` will show the current version of Appium. As of writing this guide, the current version is 1.6.3. In order for Appium to work correctly on iOS 10.3 and XCode 8.3, you will need Appium 1.6.4. As of now, the only way to get that version is by downloading the beta. Run `npm uninstall -g appium && npm install -g appium@beta` if you current version of appium is less than 1.6.4.

3. For Appium testing on physical devices, a few more steps are necessary. If you don't plan to test on a physical device you can skip to step 4. [Click Here](https://github.com/imurchie/appium-xcuitest-driver/blob/isaac-rs/docs/real-device-config.md#basic-manual-configuration) and follow the steps at your discretion. (Note: I personally did the Full manual configuration portion at the bottom of the page). Once everything is done correctly the "Web Driver Runner" app should be installed on the device that was given by UDID.

4. In order to use the Appium GUI inspector, we need to run the server through our terminal.
  * Make sure you have configured Appium for iOS first. If no configuration has be done, press the Apple icon button on the Appium GUI and follow the steps from the sub-bulleted link in step 1.
Do not click "Launch" on the GUI! Instead from the terminal run:  
```
$ appium
```
When the server starts, you are now free to press the inspector on the GUI (the magnifying glass icon). It should boot up the emulator you specified in the iOS settings and download your app to it. You can now record automation scripts!
