from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://kopibligus.com/home/signin')
driver.find_element('name', 'email').send_keys('johndoe@example.com')
driver.find_element('id', 'myPwd1').send_keys('johnKey666')
driver.find_element('id', 'submit').send_keys(Keys.ENTER)  # ButtonSubmit/Enter
driver.maximize_window()
# driver.find_element('xpath', '//*[@id="navbarToggler"]/ul[1]/li[2]/a').click()
driver.find_element('xpath', '//*[@id="navbarToggler"]/ul[1]/li[3]/a').click()
driver.find_element(
    'xpath', '/html/body/section/div/div[2]/div[1]/div[1]/div/div[1]').click()
driver.close()
