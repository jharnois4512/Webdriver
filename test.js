const webdriver = require('selenium-webdriver')
const chrome = require('selenium-webdriver/chrome')
const fire = require('selenium-webdriver/firefox')
const proxy = require('selenium-webdriver/proxy')
const proxyAddr = "127.0.0.1:8888"

/* used for encoding crx files for Chrome extensions */
function encode(file) {
  var stream = require('fs').readFileSync(file);
  return new Buffer.from(stream).toString('base64');
}

async function webDrive() {
  /* Chrome driver */
  // var opts = new chrome.Options()
  // opts.addExtensions(encode("adblock.crx"), encode("ublock.crx"))
  // var driver = new webdriver.Builder()
  //             .withCapabilities(webdriver.Capabilities.chrome())
  //             .setChromeOptions(opts)
  //             .setProxy(proxy.manual({https: proxyAddr}))
  //             .build()

  /* Firefox driver */
  var fireCap = new webdriver.Capabilities()
  var fireOpts = new fire.Options()
  fireOpts.addExtensions("adblock.xpi")
  fireCap.setAcceptInsecureCerts(true)
  var driver = new webdriver.Builder()
              .withCapabilities(fireCap)
              .setFirefoxOptions(fireOpts)
              .forBrowser("firefox")
              .setProxy(proxy.manual({https: proxyAddr}))
              // .setFirefoxOptions(fireOpts)
              .build()

  /* Internet Explorer driver */
  // var driver = new webdriver.Builder()
  //             .forBrowser("internet explorer")
  //             .build()

  /* Opera Driver */
   
  /* sites to start driving along with cookies */
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
  // (await driver).close
  // (await driver).quit
}

webDrive()
