from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Edge()


driver.get('https://www.demoblaze.com/index.html')


time.sleep(3)

botonRegistro = driver.find_element(By.XPATH, '//*[@id="signin2"]')
botonRegistro.click();

time.sleep(3)

registroNombre = driver.find_element(By.XPATH, '//*[@id="sign-username"]')
registroNombre.send_keys("DavidBravoITSQMET5")

time.sleep(3)

registroContra = driver.find_element(By.XPATH, '//*[@id="sign-password"]')
registroContra.send_keys("123456")

time.sleep(3)

registroBoton = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
registroBoton.click();

time.sleep(3)

alert = driver.switch_to.alert 
alert.accept()

time.sleep(3)

botonLogin = driver.find_element(By.XPATH, '//*[@id="login2"]')
botonLogin.click();

time.sleep(3)

loginNombre = driver.find_element(By.XPATH, '//*[@id="loginusername"]')
loginNombre.send_keys("DavidBravoITSQMET5")

time.sleep(3)

loginContra = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
loginContra.send_keys("123456")

time.sleep(3)

loginBoton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
loginBoton.click();

time.sleep(3)

producto1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
producto1.click();

time.sleep(3)

pcarrito1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
pcarrito1.click();

time.sleep(3)

alert = driver.switch_to.alert 
alert.accept()

time.sleep(3)

homeBoton = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
homeBoton.click();

time.sleep(3)

producto2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/div/h4/a')
producto2.click();

time.sleep(3)

pcarrito2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
pcarrito2.click();

time.sleep(3)

alert = driver.switch_to.alert 
alert.accept()

time.sleep(3)

carritoBoton = driver.find_element(By.XPATH, '//*[@id="cartur"]')
carritoBoton.click();

time.sleep(3)

ordenBoton = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
ordenBoton.click();

time.sleep(3)

nombre = driver.find_element(By.XPATH, '//*[@id="name"]')
nombre.send_keys("David Bravo")

time.sleep(3)

pais = driver.find_element(By.XPATH, '//*[@id="country"]')
pais.send_keys("Ecuador")

time.sleep(3)

ciudad = driver.find_element(By.XPATH, '//*[@id="city"]')
ciudad.send_keys("Quito")

time.sleep(3)

tarjeta = driver.find_element(By.XPATH, '//*[@id="card"]')
tarjeta.send_keys("1234567890123456")

time.sleep(3)

mes = driver.find_element(By.XPATH, '//*[@id="month"]')
mes.send_keys("Agosto")

time.sleep(3)

ano = driver.find_element(By.XPATH, '//*[@id="year"]')
ano.send_keys("2024")

time.sleep(3)

compraBoton = driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
compraBoton.click();

time.sleep(3)

confirmacionBoton = driver.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button')
confirmacionBoton.click();

time.sleep(3)

cerrarSesion = driver.find_element(By.XPATH, '//*[@id="logout2"]')
cerrarSesion.click();

time.sleep(3)