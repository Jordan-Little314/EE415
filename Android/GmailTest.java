package gmailtest;


import java.net.MalformedURLException;

import java.net.URL;
import java.util.concurrent.TimeUnit;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class GmailTest {

 WebDriver driver;

 @BeforeTest
 public void setUp() throws MalformedURLException {
  // Created object of DesiredCapabilities class.
  DesiredCapabilities capabilities = new DesiredCapabilities();

  // Set android deviceName desired capability. adb devices in cmd
  capabilities.setCapability("deviceName", "0146B55A0F00F017");

  // Set BROWSER_NAME desired capability.
  capabilities.setCapability(CapabilityType.BROWSER_NAME, "Android");

  // Set android VERSION desired capability.
  capabilities.setCapability(CapabilityType.VERSION, "4.4.2");

  // Set android platformName desired capability.
  capabilities.setCapability("platformName", "Android");

  // Set android appPackage desired capability.
  capabilities.setCapability("appPackage", "com.google.android.gm");

  // Set android appActivity desired capability.
  capabilities.setCapability("appActivity", "com.google.android.gm.GmailActivity");

  
  // Created object of RemoteWebDriver will all set capabilities.
  // Set appium secmdrver address and port number in URL string.
  // It will launch app in android device.
  driver = new RemoteWebDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
  driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
 }

 @Test
 public void RunTest() {
	 
	 
	//compose an email 
	 driver.findElement(By.id("com.google.android.gm:id/compose")).click();
	 driver.findElement(By.xpath("//android.widget.MultiAutoCompleteTextView")).sendKeys("415testacc@gmail.com");
	 driver.findElement(By.id("com.google.android.gm:id/subject")).sendKeys("This is a Test");
	 driver.findElement(By.id("com.google.android.gm:id/body")).sendKeys("Body of the email goes here.");
	 //attach picture
	 driver.findElement(By.xpath("//android.widget.ImageButton")).click();
	 driver.findElement(By.name("Attach picture")).click();
	 driver.findElement(By.id("com.android.documentsui:id/icon_thumb")).click();
	 driver.findElement(By.id("com.google.android.gm:id/send")).click();
	 //return to home
	 driver.navigate().back();
	 
	 
 }

}
