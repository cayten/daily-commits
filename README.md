# Day 9 — Mini Test Automation Framework (Java + TestNG) 🧱

Minimal yet practical TestNG + Selenium skeleton. Good for interviews & demos.

## ✅ Features
- `BaseTest` with setup/teardown
- One smoke test (`HomePageTest`) that opens a page and validates title
- Maven + TestNG runner
- Uses WebDriverManager for driver binaries (no manual download)

## ▶️ How to Run
1) Install **JDK 17+** and **Maven**.
2) In project folder:
```bash
mvn -q -Dtest=HomePageTest test
```
> Not using Maven? Import as a Maven project in IntelliJ and run the TestNG test.

## 🧩 Dependencies (pom.xml)
- selenium-java
- testng
- webdrivermanager

## 🔧 Environment
By default, tests run with **Chrome**. You can switch to headless by setting:
```bash
mvn -Dheadless=true -Dtest=HomePageTest test
```

---

Made for daily green commits 🌱 and quick demonstrations.
