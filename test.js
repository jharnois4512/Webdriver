const webdriver = require('selenium-webdriver')
const proxy = require('selenium-webdriver/proxy')
const again = require('chromedriver');
const proxyAddr = "0.0.0.0:8080"

async function webDrive() {
  var driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.chrome()).setProxy(proxy.manual({https: proxyAddr})).build()
  await driver.get('https://www.google.com');
  driver.manage().getCookies().then(function (cookies) {
    console.log("############GOOGLE COOKIES############");
    console.log(cookies);
  });
  await driver.get('https://www.wpi.edu/we-are-wpi');
  driver.manage().getCookies().then(function (cookies) {
    console.log("############WPI COOKIES############");
    console.log(cookies);
  });
  await driver.get('https://www.yahoo.com');
  driver.manage().getCookies().then(function (cookies) {
    console.log("############YAHOO COOKIES############");
    console.log(cookies);
  });
  (await driver).close
  (await driver).quit
}

webDrive()