from datetime import datetime, timedelta
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calcularfechas(start_date_str, end_date_str):
    # Convert date strings to datetime objects
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y')
    end_date = datetime.strptime(end_date_str, '%d/%m/%Y')

    # Initialize list to hold month ranges
    month_ranges = []

    # Loop over each month between the start and end dates
    current_month = start_date

    while current_month <= end_date:
        # Get the last day of the current month
        next_month = current_month.replace(day=28) + timedelta(days=4)
        last_day = next_month - timedelta(days=next_month.day)

        # Append the first and last day of the current month to the list of month ranges
        month_ranges.append((current_month.strftime('%d/%m/%Y'), last_day.strftime('%d/%m/%Y')))

        # Move to the next month
        current_month = next_month.replace(day=1)

    return month_ranges

url = "https://marangatu.set.gov.py/eset/login"

usuario = 1341595
contrasena = "Austria2022"

desde = "01/01/2022"
hasta = "31/03/2022"

opciones = ['COMPRAS', 'VENTAS', 'INGRESOS', 'EGRESOS']

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


# wait until the page has loaded




