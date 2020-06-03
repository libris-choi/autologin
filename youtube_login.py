import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import shutil

print("Selenium Version : " + selenium.__version__)

temp_folder = r'C:\Temp\Test'
print("Remove Temp folder : " + temp_folder)
try:
    shutil.rmtree(temp_folder)
except FileNotFoundError:
    print("Cannot find the path specified")

options = webdriver.ChromeOptions()
options.add_argument("--window-position=2560,-627")
options.add_argument("--window-size=1438,925")
options.add_argument("--disk-cache-dir=" + temp_folder) # Default
options.add_argument("--user-data-dir=" + temp_folder)
options.add_argument("--ignore-gpu-blacklist")
#options.add_argument("--use-gl")
options.add_argument("--enable-gpu-rasterization")
#options.add_argument("--enable-skia-renderer")
options.add_argument("--enable-oop-rasterization")

# Pass the argument 1 to allow and 2 to block
# remove the notification allow pop-up
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,
    "download.default_directory": 'C:\\Downloads'
})

# remove "Chrome is being controlled by automated test software" notificatoin
options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])

driver = webdriver.Chrome(
    executable_path=r'C:\chromedriver83.exe', options=options)

print("Browser Version : " + driver.capabilities['browserVersion'])
print("chrome Driver Version : " +
      driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])

# GPU
#driver.get('chrome://flags')
#driver.get('chrome://gpu')

# stackoverflow SSO
#driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.implicitly_wait(5)

try:
    driver.find_element_by_xpath('//input[@type="email"]').send_keys('********@gmail.com')
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('********')
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    driver.implicitly_wait(5)

# Already log-in
except NoSuchElementException:
    None
    
driver.get("https://www.youtube.com/")
driver.implicitly_wait(5)

try:
    driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
    driver.implicitly_wait(5)
# Already log-in
except NoSuchElementException:
    None
