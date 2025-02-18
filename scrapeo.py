from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pyautogui as py
import time
import pyperclip
import os

tiempoEntrePasos = 0.7 

#### Va a ser mas sencillo realizar el scrapeo con selenium ya que el codigo HTML de la pagina no es dinamico
## y contiene <id unicos>

def descarga_info(driver, año, div):
    ## una vez dentro filtramos por el curso que ingresara el usuario en la interfaz grafica
    curso = driver.find_element(By.XPATH, "//input[@class='form-control input-xs' and @type='text' and @placeholder='Curso']")
    curso.clear()
    curso.send_keys(año)
    
    # Division
    division = driver.find_element(By.XPATH, "//input[@class='form-control input-xs' and @type='text' and @placeholder='División']")
    division.clear()
    division.send_keys(div)

    py.press("enter")
    time.sleep(tiempoEntrePasos)
    button_ver = driver.find_element(By.XPATH, "//a[@class='btn btn-xs btn-default' and contains(@href, 'division/ver/')]")
    button_ver.click()

    asistencias_cursadas = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/a[2]")
    asistencias_cursadas.click()

    cambiar_año = driver.find_element(By.XPATH, "/html/body/div/div[1]/section[3]/div/div[1]/div/div/button[1]")
    cambiar_año.click()

    time.sleep(tiempoEntrePasos)
    veinte_veinticuatro = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/form/div[2]/div/div/div/div/div[3]/table/tbody/tr/td/span[6]")
    veinte_veinticuatro.click()
    time.sleep(tiempoEntrePasos)
    seleccionar_año = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Seleccionar']")
    seleccionar_año.click()
    time.sleep(tiempoEntrePasos)
    descargar_excel = driver.find_element(By.XPATH, "/html/body/div/div[1]/section[4]/div[4]/div/div/div[1]/div/a")
    descargar_excel.click()

    time.sleep(tiempoEntrePasos)
    # Volvemos hacia atras y repetimos el proceso
    driver.back()
    time.sleep(tiempoEntrePasos)
    driver.back()
    time.sleep(tiempoEntrePasos)
    driver.back()

def scrapeo ():

    # Ruta del EdgeDriver (si no está en el PATH, debes especificarlo)
    edge_driver_path = "C:/msedgedriver.exe"  # Cambia esto

    # Configurar la carpeta de descarga
    carpeta_descargas = os.path.abspath("C:/Users/Usuario/OneDrive/Escritorio/automatizacionNotas/inputs")  # Cambia esta ruta

    # Crear opciones para Edge
    options = webdriver.EdgeOptions()
    prefs = {
        "download.default_directory": carpeta_descargas,  # Carpeta donde se guardarán los archivos
        "download.prompt_for_download": False,  # No preguntar dónde guardar
        "download.directory_upgrade": True,  # Actualizar la carpeta de descarga sin preguntar
        "safebrowsing.enabled": True  # Deshabilitar advertencias de descargas peligrosas
    }
    options.add_experimental_option("prefs", prefs)

    # Inicializar WebDriver con las opciones
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=options)

    # Abrir una página
    driver.get("https://dti.mendoza.edu.ar/gem/division/listar/1444")

    # Ingresamos las credenciales del GEM
    input_email = driver.find_element(By.ID,"identity")
    input_email.click()
    input_email.send_keys("ivanabukaczyk@gmail.com")

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("fmartin14")

    button_ingresar = driver.find_element(By.NAME, "submit")
    button_ingresar.click()

    time.sleep(1)
    año = [1,2,3,4,5]
    division = [1,2, 3, 4, 5]

    for a in año:
        for div in division:
            descarga_info(driver, a, div)
            time.sleep(2)




