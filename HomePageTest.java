package com.example.tests;

import com.example.base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;

public class HomePageTest extends BaseTest {

    @Test
    public void titleShouldContainGoogle() {
        driver.get("https://www.google.com");
        String title = driver.getTitle();
        Assert.assertTrue(title.toLowerCase().contains("google"),
                "Title should contain 'google' but was: " + title);
    }
}
