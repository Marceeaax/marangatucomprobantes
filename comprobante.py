import calculos
import selenium
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


url = "https://marangatu.set.gov.py/eset/login"

usuario = 1341595
contrasena = "Austria2022"

desde = "01/01/2022"
hasta = "31/03/2022"

opciones = ['COMPRAS', 'VENTAS', 'INGRESOS', 'EGRESOS']
opcionelegida = 'COMPRAS'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

elem = WebDriverWait(driver, 0).until(EC.visibility_of_element_located((By.NAME, "usuario")))
elem.send_keys(usuario)
elem.send_keys(Keys.TAB)

elem2 = WebDriverWait(driver, 0).until(EC.visibility_of_element_located((By.NAME, "clave")))
elem2.send_keys(contrasena)
elem2.send_keys(Keys.TAB)

elem3 = WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
elem3.click()

elem4 = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[1]/div/div/div/div/section/div/div/div[2]/div/div/div[7]/div/div[1]")))
elem4.click()

elem5 = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[1]/div/div/div/div/section/div/div/div[2]/div/div/div[5]/div/div")))
elem5.click()

fechas = calculos.calcularfechas(desde, hasta)

parent_window = driver.current_window_handle
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])

elem6 = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/div/section[1]/div/div/form/div/div/div[2]/div[1]/div/div/input")))

elem7 = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/div/section[1]/div/div/form/div/div/div[2]/div[2]/div/div/input")))

elem8 = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]/div/div/section[1]/div/div/form/div/div/div[1]/div[2]/div/select")))
select = Select(elem8)
Select.select_by_index(0)

elem9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary.btn.ng-scope')))

i = 0

for fechainicio, fechafinal in fechas:
    print(fechainicio, fechafinal)
    elem6.clear()  # clear the input field before sending the date
    elem6.send_keys(fechainicio)
    print(fechainicio)
    elem7.clear()  # clear the input field before sending the date
    elem7.send_keys(fechafinal)
    print(fechafinal)
    elem9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary.btn.ng-scope')))
    elem9.click()
    print("busqueda")
    time.sleep(1.5)
    elem10 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-labeled.btn-secondary.mb-2")))
    elem10.click()
    print("descarga")
    
        




    





