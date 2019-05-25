from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.support.ui import Select


def choose_drop_item(drop_idx, item_name):
    # click on drop area
    container = driver.find_element_by_xpath("(//a[@class='chosen-single'])[" + str(drop_idx) + "]")
    container.click()
    # --- Choose Category --- #
    options = driver.find_elements_by_class_name('active-result')

    # iterate over drop options and if given item exists, click on it
    for option in options:
        if option.text == item_name: # choose given element
            option.click()
            break

driver = webdriver.Chrome('c:/Python/HomeWork/chromedriver.exe')
driver.get('https://buyme.co.il')               # Enter the website

## Button Register with click
element = driver.find_element_by_partial_link_text('הרשמה')
element.click()

elements = driver.find_elements_by_class_name("text-btn")

for elem in elements:
    if elem.text == "להרשמה":
        link = elem
link.click()

## Registration (password name..)
first_name = driver.find_element_by_xpath('//*[@placeholder="שם פרטי"]')
first_name.send_keys("Roman")

email_address = 'remont' + str(random.randint(0, 1000000)) + '@gmail.com'
email = driver.find_element_by_xpath('//*[@placeholder="מייל"]')
email.send_keys(email_address)

password_element = driver.find_element_by_xpath('//*[@placeholder="סיסמה"]')
password = "Ar12345678"
password_element.send_keys(password)

nd_password = driver.find_element_by_xpath('//*[@placeholder="אימות סיסמה"]')
nd_password.send_keys(password)

## Agriment
driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("fa-check"))



buttons = driver.find_elements_by_xpath('//*/button[@type="submit"]')
for button in buttons:
    if button.text == 'הרשמה ל-BUYME':
          registration = button
print(registration)
registration.click()
time.sleep(10)

# list of items index for each select object
items = ['עד 99 ש"ח',"מרכז","גיפט קארד למסעדות"]
# iterate over number of select items and activate each one and select the relevant item in it.
for drop in range(1,4):
    choose_drop_item(drop, items[drop-1])
# Press on search button (a type object)
driver.find_element_by_xpath("//a[@id='ember723']").click()

time.sleep(10)

restaurants = driver.find_elements_by_class_name('label')
for restaurant in restaurants:
    if restaurant.text == 'מסעדת אורבנו':
        urbano = restaurant

urbano.click()

## Pick to Who_to_send
time.sleep(10)
driver.find_element_by_class_name('btn-purchase').click()
time.sleep(10)
driver.find_element_by_xpath('//*/label[@data="forSomeone"]').click()
driver.find_element_by_xpath('//*/input[@data-parsley-required-message="מי הזוכה המאושר? יש להשלים את שם המקבל/ת"]').send_keys('Israel')

driver.find_element_by_partial_link_text('לאיזה אירוע?').click()
driver.find_element_by_xpath('//*/li[text()="יום הולדת"]').click()
driver.find_element_by_xpath('//*/input[@name="fileUpload"]').send_keys('C:/Python/HomeWork/123.jpg')
driver.find_element_by_class_name('send-now').click()
driver.find_element_by_class_name('icon-envelope').click()
driver.find_element_by_xpath('//*/input[@placeholder="כתובת המייל של מקבל/ת המתנה"]').send_keys('remont@gmail.com')
driver.find_element_by_class_name('btn-save').click()
time.sleep(10)
driver.find_element_by_xpath('//*/div[@class="submit-wrapper"]/button[text()="תשלום"]').click()
time.sleep(10)
driver.find_element_by_xpath('//*/div[@class="submit-wrapper"]/button[text()="תשלום"]').click()

