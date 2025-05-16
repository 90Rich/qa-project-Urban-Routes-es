from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from UrbanLocators import LocatorsUrban
import data
from main import retrieve_phone_code


class UrbanHome:
    def __init__(self, driver):
        self.driver= driver
        self.locators = LocatorsUrban

#Rellenar dirección From (desde)
    def field_from(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.field_from))
        self.driver.find_element(*self.locators.field_from).send_keys(data.address_from)
#Comrpobación
    def get_from(self):
        return self.driver.find_element(*self.locators.field_from).get_property('value')

#Rellenar direccion to (hasta)
    def field_to(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.field_to))
        self.driver.find_element(*self.locators.field_to).send_keys(data.address_to)
# Comrpobación para el assert
    def get_to(self):
        return self.driver.find_element(*self.locators.field_to).get_property('value')

#Hacer click en pedir taxi
    def click_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.taxi_button))
        self.driver.find_element(*self.locators.taxi_button).click()

#Seleccionar tarifa comfort
    def click_comfort(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.select_comfort))
        self.driver.find_element(*self.locators.select_comfort).click()
# Comrpobación para el assert
    def get_tariff_comfort(self):
        return self.driver.find_element(*self.locators.select_comfort).text


#Acciones de llenado numero de telefono y click en boton siguiente
    def click_button_phone_number(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.click_phone_number))
        self.driver.find_element(*self.locators.click_phone_number).click()

    def field_phone_number(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.field_phone))
        self.driver.find_element(*self.locators.field_phone).send_keys(data.phone_number)
# Comrpobación para el assert
    def get_phone_number(self):
        return self.driver.find_element(*self.locators.field_phone).get_property('value')

    def click_next_button_phone_number(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.click_next_button_phone_number))
        self.driver.find_element(*self.locators.click_next_button_phone_number).click()

#Rellenar codigo del teléfono

    def field_code(self):
        new_code = retrieve_phone_code (self.driver)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.locators.field_phone_code))
        self.driver.find_element(*self.locators.field_phone_code).send_keys(new_code)

# Comrpobación para el assert
    def get_phone_code(self): #Regresa el número de código en texto para compararlo
        return self.driver.find_element(*self.locators.field_phone_code).text

    def click_confirm_code(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.click_button_confirm_code))
        self.driver.find_element(*self.locators.click_button_confirm_code).click()

#Acciones llenado de agregar tarjeta
    def click_method_pay(self):
        espera_method = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.click_method_pay))
        self.driver.find_element(*self.locators.click_method_pay).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", espera_method)

    def click_add_card(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.click_add_card))
        self.driver.find_element(*self.locators.click_add_card).click()

    def field_add_card(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.field_number_card))
        self.driver.find_element(*self.locators.field_number_card).send_keys(data.card_number)

    def get_number_card(self):
        return self.driver.find_element(*self.locators.field_number_card).get_property('value')

    def field_code_card(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.field_code_card))
        self.driver.find_element(*self.locators.field_code_card).send_keys(data.card_code)
# Comrpobación para el assert
    def get_code_card(self):
        return self.driver.find_element(*self.locators.field_code_card).get_property('value')

    def click_other_space(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.field_number_card))
        self.driver.find_element(*self.locators.field_number_card).click()

    def click_button_add(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.click_button_add))
        self.driver.find_element(*self.locators.click_button_add).click()

    def click_button_close_card(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.click_button_close_card))
        self.driver.find_element(*self.locators.click_button_close_card).click()

#Rellenar comentario
    def field_comment(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.field_comment))
        self.driver.find_element(*self.locators.field_comment).send_keys(data.message_for_driver)
# Comrpobación para el assert
    def get_comment(self): #
        return self.driver.find_element(*self.locators.field_comment).get_property('value')

#Pedir manta y pañuelos
    def slider_manta(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.click_pañuelos_manta))
        self.driver.find_element(*self.locators.click_pañuelos_manta).click()
# Comrpobación para el assert
    def get_slider_manta(self):
        return self.driver.find_element(*self.locators.click_pañuelos_manta).is_selected

#Pedir helados
    def ice_cream_add_1(self):
        ice = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.click_add_ice_cream))
        self.driver.find_element(*self.locators.click_add_ice_cream).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", ice)
    def ice_cream_add_2(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.locators.click_add_ice_cream))
        self.driver.find_element(*self.locators.click_add_ice_cream).click()
# Comrpobación para el assert
    def get_counter(self):
        return self.driver.find_element(*self.locators.counter_value).text

#Reservar Taxi
    def get_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.click_pedir_taxi))
        self.driver.find_element(*self.locators.click_pedir_taxi).click()

#Esperar información del conductor
    def time(self):
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located(self.locators.wait_time_end))
        self.driver.find_element(*self.locators.wait_time_end)
# Comrpobación para el assert
    def get_information(self):
        return self.driver.find_element(*self.locators.wait_time_end).is_displayed









