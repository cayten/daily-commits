// Day5_SeleniumBasicTest.java
// Minimal Selenium 4 + TestNG example
// Notes:
// 1) Ensure you have Selenium Java & TestNG on your classpath (Maven or IntelliJ project SDK).
// 2) Ensure the ChromeDriver executable is available on PATH or set with System.setProperty().
// 3) This is a smoke-level sanity check for demo purposes.

import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Day5_SeleniumBasicTest {

    private WebDriver driver;

    @BeforeClass
    public void setUp() {
        // If chromedriver is not on PATH, uncomment and set the location:
        // System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @Test
    public void googleTitleShouldContainGoogle() {
        driver.get("https://www.google.com");
        String title = driver.getTitle();
        Assert.assertTrue(title.toLowerCase().contains("google"), "Title should contain 'google' but was: " + title);
    }

    @AfterClass(alwaysRun = true)
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
