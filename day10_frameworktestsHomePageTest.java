// tests/HomePageTest.java
package day10_framework.tests;

import day10_framework.ConfigReader;
import day10_framework.pages.HomePage;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class HomePageTest {
    private WebDriver driver;

    @BeforeClass
    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        if ("true".equalsIgnoreCase(ConfigReader.get("headless"))) {
            options.addArguments("--headless=new");
        }
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
    }

    @AfterClass(alwaysRun = true)
    public void tearDown() {
        if (driver != null) driver.quit();
    }

    @Test
    public void titleShouldContainGoogle() {
        String baseUrl = ConfigReader.get("baseUrl");
        driver.get(baseUrl);
        HomePage home = new HomePage(driver);
        Assert.assertTrue(home.getTitle().toLowerCase().contains("google"),
                "Title should contain 'google'");
        Assert.assertTrue(home.isSearchBoxPresent(), "Search box should be present");
    }
}
