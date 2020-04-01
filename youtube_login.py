import selenium
from selenium import webdriver

print("Selenium Version : " + selenium.__version__)

options = webdriver.ChromeOptions()
options.add_argument("--window-position=0,0")
options.add_argument("--window-size=1024,768")

# Pass the argument 1 to allow and 2 to block
# remove the notification allow pop-up
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

# remove "Chrome is being controlled by automated test software" notificatoin
options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])

driver = webdriver.Chrome(
    executable_path=r'C:\chromedriver80.exe', options=options)

print("Browser Version : " + driver.capabilities['browserVersion'])
print("chrome Driver Version : " +
      driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])

# stackoverflow SSO
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys('********@gmail.com')
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('********')
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
driver.implicitly_wait(5)

driver.get("https://www.youtube.com/")
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()