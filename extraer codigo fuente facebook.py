import random
import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from datetime import datetime



service = Service(r'C:\.....\geckodriver.exe')
options = Options()
profile_path = r""
profile = webdriver.FirefoxProfile(profile_path)
options.add_argument('-private')
def humanized_mouse_movement(driver, element):
    #"""Mueve el mouse en líneas imperfectas alrededor del elemento."""
    actions = ActionChains(driver)
    element_location = element.location
    element_size = element.size

    # Obtener dimensiones del viewport
    viewport_width = driver.execute_script("return window.innerWidth;")
    viewport_height = driver.execute_script("return window.innerHeight;")

    # Coordenadas del centro del botón
    center_x = element_location['x'] + element_size['width'] // 2
    center_y = element_location['y'] + element_size['height'] // 2

    # Iniciar en el centro del botón
    actions.move_to_element(element).perform()

    # Generar movimientos aleatorios dentro del viewport
    for _ in range(random.randint(5, 10)):  # Número de movimientos
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)

        # Coordenadas de destino calculadas
        target_x = center_x + offset_x
        target_y = center_y + offset_y

        # Verificar que las coordenadas estén dentro del viewport
        if 0 <= target_x <= viewport_width and 0 <= target_y <= viewport_height:
            actions.move_by_offset(offset_x, offset_y).perform()
            time.sleep(random.uniform(0.1, 0.3))  # Pausa aleatoria
driver = webdriver.Firefox(service=Service(), options=options, firefox_profile=profile)


terminos_busqueda = "migrantes rusos argentina 2023"
link = f"https://www.facebook.com/search/posts?q={terminos_busqueda}"
print(link)
driver.get(link)
output_file = f"código_fuente_FB_{terminos_busqueda}.html" 


    
while True:
    time.sleep(2)
    time.sleep(random.uniform(1,1.8))
    
    input("Configurar fecha, opciones, y presionar enter para continuar")
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_attempts = 0
    max_attempts = 12  # Número máximo de intentos si no se cargan más tweets
    
    with open(output_file, "a", encoding="utf-8") as file:
        while scroll_attempts < max_attempts:
            try:
                # Guardar el código fuente de la página
                file.write(driver.page_source)
                file.write("\n\n<!-- New Scroll -->\n\n")

                # Desplazarse hacia abajo
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.uniform(3, 5))  # Espera aleatoria para simular comportamiento humano

                # Verificar si se cargaron más tweets
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                       scroll_attempts += 1  # Incrementar intentos si no se cargó nada nuevo 
                
                else:
                    scroll_attempts = 0  # Resetear intentos si se cargo más información
                last_height = new_height
                print(f"Reintento de scrolleo: {scroll_attempts}")              
            
            
            except WebDriverException as e:
                print(f"Error: {e}")                       
                print(f"Al parecer no carga más la página")
               

        break        
                    
