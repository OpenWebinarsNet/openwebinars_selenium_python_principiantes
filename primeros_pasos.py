from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def primeros_pasos():

    #INICIAMOS EL NAVEGADOR
    #OPCION 1 - VIA RUTA
    #driver = webdriver.Chrome("/ruta/al/ejecutable/de/chromedriver")

    #OPCION 2 - VIA INSERCION DEL EJECUTABLE DENTRO DEL PATH
    driver = webdriver.Chrome()

    #NAVEGAMOS A UNA PÁGINA, POR EJEMPLO WIKIPEDIA
    driver.get("https://www.wikipedia.es")

    #EXTRAEMOS Y MOSTRAMOS EL TITULO
    title = driver.title
    print(title)

    #CERRAMOS EL NAVEGADOR.
    '''
    Recordad que driver.close() cerrará la ventana actual del navegador.
    En caso de haber más de una, cerrará la que tenga el foco en ese momento.

    Para salir correctamente del navegador hemos de usar  driver.quit(),
    que cerrará todas las ventanas y la sesión con chrome.
    '''
    driver.quit()


def localizando_ID():
    iniciar_navegador()
    
    #DECLARAMOS EL IDENTIFICADOR A TRAVÉS DE LA TUPLA (BY,"LOCALIZADOR")
    random_page_ID = (By.ID, "n-randompage")

    time.sleep(2)
    # LA FUNCIÓN FIND_ELEMENT ESPERA DOS PARÁMETROS. MEDIANTE * INDICAMOS A PYTHON QUE DEBE
    # DESGLOSAR LA VARIABLE TUPLA PARA QUE INSERTARLA COMO PARÁMETROS
    driver.find_element(*random_page_ID).click()
    time.sleep(2)

    cerrar_navegador()


def localizando_LINK_TEXT():
    
    iniciar_navegador()
    
    #DECLARAMOS EL IDENTIFICADOR A TRAVÉS DE LA TUPLA (BY,"LOCALIZADOR")
    random_page_LINK_TEXT = (By.LINK_TEXT, "Página aleatoria")

    time.sleep(2)
    driver.find_element(*random_page_LINK_TEXT).click()
    time.sleep(2)

    cerrar_navegador()


def localizando_TAG_NAME():
    
    iniciar_navegador()
    
    #DECLARAMOS EL IDENTIFICADOR A TRAVÉS DE LA TUPLA (BY,"LOCALIZADOR")
    # EXISTE UN ÚNICO TAG=BUTTON EN WIKIPEDIA, QUE NOS PERMITE GESTIONAR LOS IDIOMAS
    # VAMOS A LOCALIZARLO Y PULSARLO.
    configuracion_idiomas_TAG_NAME = (By.TAG_NAME, "button")

    time.sleep(2)
    boton_configuracion_idioma = driver.find_element(*configuracion_idiomas_TAG_NAME)
    boton_configuracion_idioma.click()
    time.sleep(2)

    cerrar_navegador()


def localizando_XPATH():
    
    iniciar_navegador()
    
    '''
    MOSTRAMOS VARIOS EJEMPLOS PARA QUE DISPONGÁIS DE VARIAS CONSTRUCCIONES
    A TRAVÉS DE XPATH
    '''
    commons_a_href_XPATH = (By.XPATH, "//a[text()='Commons']")
    
    time.sleep(2)
    commons_a_href_element = driver.find_element(*commons_a_href_XPATH)
    iluminar_elemento(commons_a_href_element)
    time.sleep(4)
    
    
    leer_articulo_destacado_button_XPATH = (By.XPATH, "//div[@id='Artículo_destacado']/following-sibling::div[@class='main-footer']/descendant::span[1]")
    
    time.sleep(2)
    leer_articulo_destacado_button_element = driver.find_element(*leer_articulo_destacado_button_XPATH)
    iluminar_elemento(leer_articulo_destacado_button_element)
    time.sleep(4)
    
    
    otros_eventos_actuales_button_XPATH = (By.XPATH, "//div[contains(@class,'footer')]/descendant::a/span[contains(text(),'eventos actuales')]")
    
    time.sleep(2)
    otros_eventos_actuales_element = driver.find_element(*otros_eventos_actuales_button_XPATH)
    iluminar_elemento(otros_eventos_actuales_element)
    time.sleep(4)
    

    cerrar_navegador()



def localizando_CSS_SELECTOR():
     
    iniciar_navegador()
    
    '''
    MOSTRAMOS VARIOS EJEMPLOS PARA QUE DISPONGÁIS DE VARIAS CONSTRUCCIONES
    A TRAVÉS DE CSS
    '''
    leer_articulo_bueno_CSS = (By.CSS_SELECTOR, "div.main-footer span")
    
    time.sleep(2)
    leer_articulo_bueno_element = driver.find_element(*leer_articulo_bueno_CSS)
    iluminar_elemento(leer_articulo_bueno_element)
    time.sleep(4)
    
    commons_a_href_CSS = (By.CSS_SELECTOR, "div#main-wmfsp table tr:nth-of-type(1) td:nth-of-type(2) a")
    
    time.sleep(2)
    commons_a_href_element = driver.find_element(*commons_a_href_CSS)
    iluminar_elemento(commons_a_href_element)
    time.sleep(4)
    
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
    driver.get("https://www.wikipedia.es")
    
def cerrar_navegador():
    driver.quit()
   
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
    localizando_CSS_SELECTOR()