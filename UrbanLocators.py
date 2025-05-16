from selenium.webdriver.common.by import By
class LocatorsUrban:

#1 Rellenar campos de direcciones y pedir taxi
    field_from = (By.ID, 'from')
    field_to = (By.ID, 'to')
    taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')

#2 Seleccionar comfort
    select_comfort = (By.XPATH, '//div[text()="Comfort"]')

#3 Relenar campos número de teléfono,
    click_phone_number = (By.XPATH, '//div[text()="Número de teléfono"]')
    field_phone = (By.ID, 'phone')
    click_next_button_phone_number = (By.CSS_SELECTOR, 'button.full')
#Codigo
    field_phone_code = (By.ID, 'code')
    click_button_confirm_code = (By.XPATH, '//button[contains(text(), "Confirmar")]')

#4 Agregar una tarjeta de crédito
    click_method_pay = (By.CLASS_NAME, 'pp-text')
    click_add_card = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    field_number_card = (By.ID, 'number')
    field_code_card = (By.XPATH, '//input[@placeholder="12"]')
    click_button_add = (By.XPATH, '//button[text()="Agregar"]')
    click_button_close_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

#5 Escribir un mensaje para el controlador.
    field_comment = (By.ID, 'comment')

#6 Pedir manta y pañuelos
    click_pañuelos_manta = (By. XPATH, '//span[@class="slider round"]')

#7 Pedir helados
    click_add_ice_cream = (By.XPATH, '//div[text()="+"]')
    counter_value = (By.XPATH, '//div[@class="counter-value"]')

#8 Pedir taxi / Aparece el modal para buscar un taxi
    click_pedir_taxi = (By.CLASS_NAME, 'smart-button-main')

#9 espera para información del condutor
    wait_time_end = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[3]/button')









#
    #modo_personal =
    #type_taxi =
    #button_
