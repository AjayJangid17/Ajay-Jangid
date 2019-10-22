from selenium import webdriver

u = input('Enter email ID: ')
p = input('Enter Password: ')

url = 'https://en-gb.facebook.com/login/'

driver = webdriver.Chrome(r"C:\Users\Enfield\Downloads\chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(u)
driver.find_element_by_id('pass').send_keys(p)
driver.find_element_by_id('loginbutton').click()
