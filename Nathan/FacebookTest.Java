package firsttest;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class SimpleAndroidCalcTest {

 WebDriver driver;

 @BeforeTest
 public void setUp() throws MalformedURLException {
  // Created object of DesiredCapabilities class.
  DesiredCapabilities capabilities = new DesiredCapabilities();

  // Set android deviceName desired capability. Set your device name.
  capabilities.setCapability("deviceName", "ZX1G324FVL");

  // Set BROWSER_NAME desired capability. It's Android in our case here.
  capabilities.setCapability(CapabilityType.BROWSER_NAME, "Android");

  // Set android VERSION desired capability. Set your mobile device's OS version.
  capabilities.setCapability(CapabilityType.VERSION, "5.1");

  // Set android platformName desired capability. It's Android in our case here.
  capabilities.setCapability("platformName", "Android");

  // Set android appPackage desired capability. It is
  // com.android.calculator2 for calculator application.
  // Set your application's appPackage if you are using any other app.
  capabilities.setCapability("appPackage", "com.facebook.katana");

  // Set android appActivity desired capability. It is
  // com.android.calculator2.Calculator for calculator application.
  // Set your application's appPackage if you are using any other app.
  
  capabilities.setCapability("appActivity", "com.facebook.katana.LoginActivity");
  // Created object of RemoteWebDriver will all set capabilities.
  // Set appium server address and port number in URL string.
  // It will launch calculator app in android device.
  driver = new RemoteWebDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
  driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS);
 }

 @Test
 public void Sum() {
	 
	 //Open the pictures
	 driver.findElement(By.id("com.facebook.katana:id/feed_composer_photo_button")).click();
	 
	 //Open the camera
	 driver.findElement(By.id("com.facebook.katana:id/primary_action_button")).click();
	 
	 //Take a picture.
	 driver.findElement(By.id("com.android.camera2:id/shutter_button")).click();
	 
	 //Save it
	 driver.findElement(By.id("com.android.camera2:id/done_button")).click();
	 
	 //Add a description
	 driver.findElement(By.id("com.facebook.katana:id/composer_status_text")).sendKeys("I took a picture!");	 
	 
	 //Post the picture.
	 driver.findElement(By.id("com.facebook.katana:id/primary_named_button")).click();
 }

@AfterTest
 public void End() {
  driver.quit();
 }
}
