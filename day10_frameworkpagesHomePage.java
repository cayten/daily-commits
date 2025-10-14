// pages/HomePage.java
package day10_framework.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage {
    private final WebDriver driver;
    private final By searchBox = By.name("q");

    public HomePage(WebDriver driver) {
        this.driver = driver;
    }

    public String getTitle() {
        return driver.getTitle();
    }

    public boolean isSearchBoxPresent() {
        return !driver.findElements(searchBox).isEmpty();
    }
}
