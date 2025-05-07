from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from UrbanLocators import LocatorsUrban
import data


class UrbanHome:
    def __init__(self, driver):
        self.driver= driver
        self.locators = LocatorsUrban

# no modificar
    def retrieve_phone_code(driver) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                  {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code


#Rellenar dirección From (desde)
    def field_from(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.locators.field_from))
        self.driver.find_element(*self.locators.field_from).send_keys(data.address_from)


#Rellenar direccion to (hasta)
    def field_to(self):
        self.driver.find_element(*self.locators.field_to).send_keys(data.address_to)

#Hacer click en pedir taxi
    def click_taxi_button(self):
        self.driver.find_element(*self.locators.taxi_button).click()

#Seleccionar tarifa comfort
    def click_comfort(self):
        self.driver.find_element(*self.locators.select_comfort).click()

#Acciones de llenado numero de telefono
    def click_button_phone_number(self):
        self.driver.find_element(*self.locators.click_phone_number).click()

    #def click_field_phone_number(self):
        #self.driver.find_element(*self.locators.click_field_phone).click()

    def fiel_phone_number(self):
        self.driver.find_element(*self.locators.field_phone).send_keys(data.phone_number)

    def click_next_button_phone_number(self):
         self.driver.find_element(*self.locators.click_next_button_phone_number).click()

    def field_code(self):
        new_code = self.retrieve_phone_code()
        #WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.field_code))
        self.driver.find_element(*self.locators.field_code).send_keys(new_code)

    def click_confirm_code(self):
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.locators.click_button_confirm_code))
        self.driver.find_element(*self.locators.click_button_confirm_code).click()

#Acciones llenado de agregar tarjeta
    def click_method_pay(self):
        espera_method = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.locators.click_method_pay))
        self.driver.find_element(*self.locators.click_method_pay).click()
        self.driver.execute_script("arguments[0].scrollIntoView();", espera_method)

    def click_add_card(self):
        self.driver.find_element(*self.locators.click_add_card).click()

    def field_add_card(self):
        self.driver.find_element(*self.locators.field_number_card).send_keys(data.card_number)

    def field_code_card(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.locators.field_code_card))
        self.driver.find_element(*self.locators.field_code_card).send_keys(data.card_code)

    def click_other_space(self):
        self.driver.find_element(*self.locators.field_number_card).click()

    def click_button_add(self):
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.locators.click_button_add))
        self.driver.find_element(*self.locators.click_button_add).click()

    def click_button_close_card(self):
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.locators.click_button_close_card))
        self.driver.find_element(*self.locators.click_button_close_card).click()








