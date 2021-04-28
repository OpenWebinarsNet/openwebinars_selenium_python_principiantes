from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException

import time


def fill_textbox():

    iniciar_navegador()
    
    username_textbox = (By.ID, "username")
    password_textbox = (By.ID, "password")
    login_button = (By.ID, "loginButton")
    
    
    driver.find_element(*username_textbox).send_keys("usuario")
    time.sleep(2)
    driver.find_element(*password_textbox).send_keys("password")
    time.sleep(2)
    driver.find_element(*login_button).click()
    time.sleep(3)
    
   
    cerrar_navegador()

def comboboxes_selection():

    iniciar_navegador()
    
    #nos dirigimos a la sección de Comboboxes
    driver.find_element(By.LINK_TEXT, "Comboboxes").click()
    
    combobox_simple = (By.ID, "combobox1")
    combobox_multiple = (By.ID, "combobox2")
    boton_combobox = (By.ID, "enviaComboboxes")
    
    #INSTANCIAMOS UN OBJETO DE LA CLASE SELECT PARA PODER
    #MANIPULAR LOS COMBOBOX
    combobox_simple_element = driver.find_element(*combobox_simple)
    combobox_multiple_element = driver.find_element(*combobox_multiple)
    boton_combobox_element = driver.find_element(*boton_combobox)
        
    select_single = Select(combobox_simple_element)
    select_multiple = Select(combobox_multiple_element)
    
    for option in select_single.options:
        print(option.text)
        
    select_single.select_by_index(0)
    time.sleep(2)
    select_single.select_by_value("huevos")
    time.sleep(2)
    select_single.select_by_visible_text("Leche")
    time.sleep(2)
    
    print()
    
    for option in select_multiple.options:
        print(option.text)
        
    select_multiple.select_by_index(0)
    time.sleep(2)
    select_multiple.select_by_value("pera")
    time.sleep(2)
    select_multiple.select_by_visible_text("Granada")
    time.sleep(2)
    
    boton_combobox_element.click()
    time.sleep(2)
    
    select_multiple.deselect_by_index(0)
    time.sleep(1)
    boton_combobox_element.click()
    time.sleep(2)
    
    select_multiple.deselect_all()
    time.sleep(1)
    boton_combobox_element.click()
    time.sleep(2)
    
    cerrar_navegador()


def checkboxes_action():
    
    iniciar_navegador()
    
    #nos dirigimos a la sección de Checkboxes
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    
    boton_checkboxes = (By.ID, "enviarCheckboxbutton")
    
    verdura_check_XPATH = (By.XPATH, "//input[@value='verdura']")
    verdura_check_CSS = (By.CSS_SELECTOR, "input[value|='verdura']")
    
    #PULSAMOS EL CHECKBOX DE VERDURA MEDIANTE XPATH
    driver.find_element(*verdura_check_XPATH).click()
    time.sleep(2)
        
    all_checkboxes = (By.TAG_NAME, "input")    
    for cb in driver.find_elements(*all_checkboxes):
        if cb.get_attribute("value") == "kleenex":
            cb.click()
            time.sleep(2)
            break
    
    driver.find_element(*boton_checkboxes).click()
    time.sleep(2)
    
    # MOSTRAMOS QUÉ CHECKBOXES ESTÁN PULSADOS
    # DEBEMOS VOLVER A RECUPERAR LOS ELEMENTOS PORQUE SU
    # ESTADO HA CAMBIADO TRAS PULSARLOS
    for cb in driver.find_elements(*all_checkboxes):
        print(cb.get_attribute("value")," -> ",cb.is_selected())
    
    print()
    
    #PULSAMOS EL CHECKBOX DE VERDURA MEDIANTE CSS
    driver.find_element(*verdura_check_CSS).click()
    time.sleep(2)
        
  
    # MOSTRAMOS QUÉ CHECKBOXES ESTÁN PULSADOS
    # DEBEMOS VOLVER A RECUPERAR LOS ELEMENTOS PORQUE SU
    # ESTADO HA CAMBIADO TRAS PULSARLOS
    for cb in driver.find_elements(*all_checkboxes):
        value = cb.get_attribute("value")
        selected = str(cb.is_selected())
        print(value," -> ",selected)
  

    driver.find_element(*boton_checkboxes).click()
    time.sleep(3)
    
    cerrar_navegador()




def radiobuttons_action():
    
    iniciar_navegador()
    
    #nos dirigimos a la sección de Radiobuttons
    driver.find_element(By.LINK_TEXT, "Radiobuttons").click()
    
    boton_radiobuttons = (By.ID, "enviarRadiobutton")
    
    agua_radio_XPATH = (By.XPATH, "(//input[@name='bebida'])[2]")
    agua_radio_CSS = (By.CSS_SELECTOR, "input[value|='agua']")
    dorada_radio_CSS = (By.CSS_SELECTOR, "input[value|='dorada']")
    
    #PULSAMOS EL RADIO DE AGUA MEDIANTE XPATH
    driver.find_element(*agua_radio_XPATH).click()
    time.sleep(2)
        
    all_first_radiobuttons = (By.XPATH, "//input[@name='bebida']")    
    for rb in driver.find_elements(*all_first_radiobuttons):
        rb.click()
        time.sleep(1)
        break

    driver.find_element(*boton_radiobuttons).click()
    time.sleep(2)
    
    # MOSTRAMOS QUÉ RADIOBUTTONS ESTÁN PULSADOS
    # DEBEMOS VOLVER A RECUPERAR LOS ELEMENTOS PORQUE SU
    # ESTADO HA CAMBIADO TRAS PULSARLOS
    for rb in driver.find_elements(*all_first_radiobuttons):
        print(rb.get_attribute("value")," -> ",rb.is_selected())
    
    print()
    
    #PULSAMOS EL RADIO DE DORADA
    driver.find_element(*dorada_radio_CSS).click()
    
    #PULSAMOS EL RADIO DE AGUA MEDIANTE CSS
    driver.find_element(*agua_radio_CSS).click()
    time.sleep(2)
        
  
    # MOSTRAMOS QUÉ RADIOBUTTONS ESTÁN PULSADOS
    # DEBEMOS VOLVER A RECUPERAR LOS ELEMENTOS PORQUE SU
    # ESTADO HA CAMBIADO TRAS PULSARLOS    
    for cb in driver.find_elements(*all_first_radiobuttons):
        value = cb.get_attribute("value")
        selected = str(cb.is_selected())
        print(value," -> ",selected)
  

    driver.find_element(*boton_radiobuttons).click()
    time.sleep(3)
    
    cerrar_navegador()



def calendar_action():
    
    iniciar_navegador()
    
    #nos dirigimos a la sección de Radiobuttons
    driver.find_element(By.LINK_TEXT, "Calendars").click()
    
    calendar_input = (By.NAME, "fecha")

    calendar_elemento = driver.find_element(*calendar_input)
    
    time.sleep(1)
    calendar_elemento.send_keys("10121980")
    time.sleep(1)
    calendar_elemento.send_keys(Keys.TAB)
    time.sleep(1)
    calendar_elemento.send_keys("1248")
    time.sleep(3)

    cerrar_navegador()
    
    

def alerts_action():
    
    iniciar_navegador()
    
    #nos dirigimos a la sección de Radiobuttons
    driver.find_element(By.LINK_TEXT, "Alerts").click()
    
    alert_simple = (By.ID, "buttonAlertSimple")
    alert_confirm = (By.ID, "buttonAlertConfirm")
    alert_prompt = (By.ID, "buttonAlertPrompt")
    
    time.sleep(1)
    # ACCIONA ALERT SIMPLE
    driver.find_element(*alert_simple).click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    
    
    # ACCIONA ALERT CONFIRM
    driver.find_element(*alert_confirm).click()
    time.sleep(1)
    driver.switch_to.alert.dismiss()
    time.sleep(1)
    
    # ACCIONA ALERT PROMPT
    driver.find_element(*alert_prompt).click()
    time.sleep(1)
    #CHROME NO MUESTRA EL TEXTO EN EL ALERT, FIREFOX SI.
    driver.switch_to.alert.send_keys("hola! :)")
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    
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
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://localhost:3000")
         
def cerrar_navegador():
    driver.quit()
   
def ir_a_waits():
    driver.find_element(By.LINK_TEXT, "Waits").click()   
   
   

'''
 PODÉIS IGNORAR ESTA FUNCIÓN HASTA CONOCER EL USO DE execute_script.
 ESTAMOS EJECUTANDO SCRIPTS DE JAVASCRIPT EN LA PÁGINA PARA HACER
 SCROLL HASTA EL ELEMENTO Y SETEARLE UN HIGHLIGHT
'''
def iluminar_elemento(elemento):
    driver.execute_script("window.scrollTo(0, arguments[0]);", (elemento.location["y"]-100))
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow;');", elemento)
##########################################################



if __name__ == "__main__":
    alerts_action()