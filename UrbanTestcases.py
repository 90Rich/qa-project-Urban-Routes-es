from selenium import webdriver
from UrbanMethods import UrbanHome
import data

class TestcasesField:
    driver= None
    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.urbanhome = UrbanHome (cls.driver)

#Rellenar campos de direcciones Desde, Hasta, hacer click en pedir taxi y
    def test_1_field_and_click(self):
        self.urbanhome.field_from()
        self.urbanhome.field_to()
        assert self.urbanhome.get_from() == data.address_from #Comprobar que se escribio la direccion Desde
        assert self.urbanhome.get_to() == data.address_to #Comprobar que se escribio la direccion Hasta
#Click en botón "Pedir Taxi"
        self.urbanhome.click_taxi_button()

#Hacer click en tarifa comfort
    def test_2_select_tariff(self):
        self.urbanhome.click_comfort()
        assert self.urbanhome.get_tariff_comfort() == 'Comfort' #Comrpobar que se selecciono la tarifa "Comfort"

#Hacer click en número de teléfono para agregarlo, rellenarlo y hacer click en siguiente
    def test_3_phone(self):
        self.urbanhome.click_button_phone_number()
        self.urbanhome.field_phone_number()
        assert self.urbanhome.get_phone_number() == data.phone_number #Comprobar que se escribió el "número de teléfono"
        self.urbanhome.click_next_button_phone_number()

#Rellenar el campo del "código" y hacer click en "confirmar"
        self.urbanhome.field_code()
        assert self.urbanhome.get_phone_code() != "Introduce él código" #Comprobar que se escribió el "codigo SMS"
        self.urbanhome.click_confirm_code()

#Hacer click en "Método de pago"
    def test_4_pay_method(self):
        self.urbanhome.click_method_pay()

#Click en "Agregar tarjeta", rellenar el campo de "numero de tarjeta" y rellenar numero de "codigo"
        self.urbanhome.click_add_card()
        self.urbanhome.field_add_card()
        assert self.urbanhome.get_number_card() == data.card_number #Comprobar que se escribió el "número de tarjeta"
        self.urbanhome.field_code_card()
        assert self.urbanhome.get_code_card() == data.card_code #Comprobar que se escribió el "codigo de la tarjeta"

#Click en otro espacio para activar boton de "Agregar"
        self.urbanhome.click_other_space()

#Hacer click en boton "Agregar" y cerrar ventana
        self.urbanhome.click_button_add()
        self.urbanhome.click_button_close_card()

#Rellenar comentario
    def test_5_comment(self):
        self.urbanhome.field_comment()
        assert self.urbanhome.get_comment() == data.message_for_driver #Comprobar que se escribió el "Comentario para el conductor"

#Realizar pedido de "Manta y pañuelos"
    def test_6_slider(self):
        self.urbanhome.slider_manta()
        assert self.urbanhome.get_slider_manta(), "No esta seleccionado" #Comprobar que el slider cambio a seleccionado

#Realizar pedido de 2 helados
    def test_7_ice(self):
        self.urbanhome.ice_cream_add_1()
        self.urbanhome.ice_cream_add_2()
        assert self.urbanhome.get_counter() == '2' #Comprobar que se pidem "2 helados"

#Hacer click en el boton "Reservar"
    def test_8_taxi(self):
        self.urbanhome.get_taxi()

#Esperar a que aparezca información del conductor
    def test_9_information(self):
        self.urbanhome.time()
        assert self.urbanhome.get_information(), 'No es visible el elemento esperado' #Comprubea que el elemento esperado es visible


    @classmethod
    def teardown(cls):
        cls.driver.quit()


