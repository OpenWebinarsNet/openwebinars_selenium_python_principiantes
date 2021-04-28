from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException

import time




def implicit_wait():

    iniciar_navegador()
   
    # SETEAMOS UN VALOR DE 10 SEGUNDOS DE ESPERA IMPLICITA
    driver.implicitly_wait(10)

    # UNA VEZ SETEADA LA ESPERA IMPLÍCITA, VAMOS A LA SECCIÓN WAITS
    ir_a_waits()

    boton_implicit_wait = (By.ID, "implicitWaitButton")
    
    driver.find_element(*boton_implicit_wait).click()
    
    time.sleep(3)
    
    cerrar_navegador()

def explicit_wait():

    iniciar_navegador()
   
    wait = WebDriverWait(driver, 10, 0.2)

    # UNA VEZ SETEADA LA ESPERA IMPLÍCITA, VAMOS A LA SECCIÓN WAITS
    ir_a_waits()

    boton_explicit_wait = (By.ID, "explicitWaitButton")
    
    boton_explicit_wait_elemento = wait.until(EC.element_to_be_clickable(boton_explicit_wait))
    boton_explicit_wait_elemento.click()    
    
    time.sleep(3)
    
    cerrar_navegador()


def simulate_fluent_wait():
    
    '''
    PARA PODER LANZAR UN ERROR A TRAVÉS DE WEBDRIVERWAIT NECESITEMOS UTILIZAR EL MÉTODO:
    
     wait.until_not
     
    ESTO SE DEBE A QUE ES EL ÚNICO MÉTODO DEL WAIT QUE CAPTURA LAS EXCEPCIONES QUE LANZAMOS
    EL MÉTODO wait.until SÓLO ELEVA EXCEPCIONES DE TIPO TIMEOUTEXCEPTION.
    
    SÓLO EN CASO DE CAPTURAR EL ERROR QUE ESPERAMOS, WAIT.UNTIL_NOT DEVOLVERÁ UN BOOLEANO 'TRUE'
    
    PODÉIS COMPROBAR SI FUNCIONA ELIMINANDO LA TUPLA QUE CONTIENE 'StaleElementReferenceException' EN
    LA DECLARACIÓN DEL WAIT
    '''
    
    iniciar_navegador()
   
    #VAMOS A QUEDARNOS EN LA SECCIÓN DE LOGIN PARA DISPONER DEL BOTÓN INICIALMENTE
    
    boton_login = driver.find_element(By.ID, "loginButton")

    
    '''
    A CONTINUACIÓN NOS VAMOS A CAMBIAR DE SECCIÓN Y PREGUNTAREMOS POR EL BOTÓN QUE ALMACENAMOS ANTERIORMENTE
    AL HABER CAMBIADO DE SECCIÓN, SELENIUM NO PODRÁ ENCONTRAR DICHO BOTÓN Y, POR ELLO, DEVOLVERÁ
    EL ERROR STALEELEMENTREFERENCEEXCEPTION.
    '''
    driver.find_element(By.LINK_TEXT, "Alerts").click()

    wait = WebDriverWait(driver, 3, 0.5, (StaleElementReferenceException))    
    try:
        print(wait.until_not(lambda x: boton_login.is_displayed()))
    except Exception as e:
        print(e.with_traceback)

    time.sleep(3)
    
    cerrar_navegador()




### FUNCIONES COMUNES A TODAS LAS FUNCIONES DE LOCALIZACION
def iniciar_navegador():
    '''
    PARA PODER SETEAR LA VARIABLE DE MANERA GLOBAL DENTRO DE LAS FUNCIONES,
    INDICAMOS A LA VARIABLE QUE ES DE TIPO GLOBAL. POSTERIORMENTE PODEMOS
    MODIFICARLA
    '''
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000")
      
    
    
def cerrar_navegador():
    driver.quit()
   
def ir_a_waits():
    driver.find_element(By.LINK_TEXT, "Waits").click()   
   
   

'''
 PODÉIS IGNORAR ESTA FUNCIÓN HASTA CONOCER EL USO DE execute_script
 ESTAMOS EJECUTANDO SCRIPTS DE JAVASCRIPT EN LA PÁGINA PARA HACER
 SCROLL HASTA EL ELEMENTO Y SETEARLE UN HIGHLIGHT
'''
def iluminar_elemento(elemento):
    driver.execute_script("window.scrollTo(0, arguments[0]);", (elemento.location["y"]-100))
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow;');", elemento)
##########################################################



if __name__ == "__main__":
    simulate_fluent_wait()