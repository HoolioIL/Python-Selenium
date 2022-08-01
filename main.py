import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#service = Service('C:/Users/JFIL/Desktop/PythonFolder/automation/chromedriver.exe')
s = Service('C:/Users/JFIL/Desktop/PythonFolder/automation/chromedriver.exe')
driver = webdriver.Chrome(service=s)


baseUrl = "https://registrovisitas2022.herokuapp.com/"
user = "mario@bros.jp"
password = "123456789"
driver.get( baseUrl )
time.sleep(5)


driver.find_element("xpath", '//input[@formcontrolname="email"]').send_keys( user )
driver.find_element("xpath", '//input[@formcontrolname="password"]').send_keys( password)

driver.find_element("xpath", '//button[@type="submit"]').click()

time.sleep(25)

driver.find_element("xpath", '//p[contains( text(), "Incidencias ocurridas")]/parent::div//following-sibling::a').click()

time.sleep(2)

select_category = Select( driver.find_element("xpath", '//select[@formcontrolname="categoria"]'))
select_category.select_by_value("6260ce2b411aaba4f06916e9")

comentarios = driver.find_element( "xpath", '//textarea[@formcontrolname="comentarios"]')
message = "This is a comment from selenium with Python"
comentarios.send_keys( message )

time.sleep( 3 )

save_button = driver.find_element( "xpath", '//button[@type="submit"]').click()

WebDriverWait(driver, timeout=10 ).until( EC.visibility_of_element_located(( By.CLASS_NAME, "swal2-modal" )))

message = " ".join([x.capitalize() for x in message.split()])

texto_table = driver.find_element( "xpath", f'//table/tbody/tr/td[ contains( text(), "{ message }")]' )

print( texto_table.text )

assert texto_table.text == message

time.sleep ( 3 )
driver.quit()