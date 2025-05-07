from selenium.webdriver.common.by import By
class LocatorsUrban:

#Rellenar campos de direcciones
    field_from = (By.ID, 'from')
    field_to = (By.ID, 'to')

#seleccionar tarifa de taxi
    #taxi_button =(By.CSS_SELECTOR, 'button.round')
    taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')

#seleccionar confort
    select_comfort = (By.XPATH, '//div[text()="Comfort"]')

#numero de telefono
    click_phone_number = (By.XPATH, '//div[text()="Número de teléfono"]')
    #click_field_phone = (By.XPATH, '//label[text()="Número de teléfono"]')
    field_phone = (By.ID, 'phone')
    click_next_button_phone_number = (By.CSS_SELECTOR, 'button.full')
#Codigo
    field_code = (By.ID, 'code')
    click_button_confirm_code = (By.XPATH, '//button[contains(text(), "Confirmar")]')

#agregar tarjeta
    click_method_pay = (By.CLASS_NAME, 'pp-text')
    click_add_card = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    field_number_card = (By.ID, 'number')
    field_code_card = (By.XPATH, '//input[@placeholder="12"]')
    click_button_add = (By.XPATH, '//button[text()="Agregar"]')
    click_button_close_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')







#
    #modo_personal =
    #type_taxi =
    #button_
