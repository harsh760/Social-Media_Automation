from selenium import webdriver
from time import sleep
import contacts

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

sleep(15)

wishingContacts = contacts.contacts("contacts.csv")

msg = " A very Happy New Year wishes from Harsh"

for key,value in wishingContacts.items():
    sleep(1)
    searchUser = driver.find_element_by_css_selector("input[type='text']")
    searchUser.click()
    searchUser.send_keys(key)

    sleep(1)

    user = driver.find_element_by_css_selector("span[title='"+key+"']")
    user.click()

    sleep(1)

    msgBox = driver.find_element_by_class_name('_3u328')
    msgBox.click()
    msgBox.send_keys("Hello " +value+ msg)

    send = driver.find_element_by_class_name('_3M-N-')
    send.click()