import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.net.URL;

public class {scriptName} {
	public static void main(String[] args) {
		DesiredCapabilities capabilities = new DesiredCapabilities();
		capabilities.setCapability("appium-version", "1.0");
		capabilities.setCapability("platformName", "iOS");
		capabilities.setCapability("platformVersion", "10.2");
		capabilities.setCapability("deviceName", "iPhone 6");
		capabilities.setCapability("app", "/Users/WSU/Library/Developer/Xcode/DerivedData/Homework_2_(Joke_App)-axpklxluqpqqsjfvojodtotpwlum/Build/Products/Release-iphonesimulator/Homework 2 (Joke App).app");
		wd = new AppiumDriver(new URL("http://0.0.0.0:4723/wd/hub"), capabilities);
		wd.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
		wd.findElement(By.name("Answer")).click();
		wd.findElement(By.name("New Joke")).click();
		wd.findElement(By.name("Answer")).click();
		wd.findElement(By.name("(null)")).click();
(JavascriptExecutor)wd.executeScript("mobile: tap", new HashMap<String, Double>() {{ put("tapCount", 3); put("touchCount", 1); put("duration", 0.8844467474489797); put("x", 178); put("y", 301); }});
		wd.close();
	}
}
