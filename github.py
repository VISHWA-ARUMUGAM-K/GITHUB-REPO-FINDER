from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep, strftime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Import webdriver
nl = "\n"
links_array = []
name = ""
# Initialize webdriver object
options = Options()
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chromedriver_path = "C:\Drivers\chromedriver_win32\chromedriver"
# service = Service("C:\Drivers\chromedriver_win32\chromedriver")

# webdriver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()))

webdriver = webdriver.Chrome(
    executable_path=chromedriver_path, options=options)


webdriver.get("https://github.com/")
webdriver.maximize_window()


sleep(0.5)
signin = webdriver.find_element(
    By.XPATH, "//a[@class='HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0']").click()
sleep(0.5)

Username = webdriver.find_element(
    By.NAME, "login").send_keys("vishwakrishoooo@gmail.com")
password = webdriver.find_element(By.NAME, "password").send_keys("vishwA01")
login = webdriver.find_element(By.NAME, "commit").click()

sleep(0.5)
links = webdriver.find_elements(
    By.XPATH, "//div[@class='wb-break-word']//a")
for i in links:
    if i.get_attribute("href") in links_array:
        continue
    else:
        links_array.append(i.get_attribute("href"))

for i, j in enumerate(links_array, start=1):
    if name == j.split("/")[-2]:
        None
    else:
        name = j.split("/")[-2]
        print(f"github name : {name}")

print("Getting repositories ...")

for i, j in enumerate(links_array, start=1):

    print(i, j.split("/")[-1])


ans = input("enter repository number : ")
sleep(0.5)
webdriver.find_element(
    By.XPATH, f"//aside[@aria-label='Account']//li[{ans}]//div[1]//div[1]//a[1]").click()
try:
    webdriver.find_element(
        By.XPATH, "//summary[@class='Button--primary Button--medium Button flex-1 d-inline-flex']").click()
    link = webdriver.find_element(
        By.XPATH, "//div[@class='input-group']//input")
    link = link.get_attribute("value")
    print(link)

    webdriver.quit()
except:
    print("new repository found")
    link = webdriver.find_element(
        By.XPATH, "//span[@class='input-group width-full']//input")
    link = link.get_attribute("value")
    print(link)
    webdriver.quit()
