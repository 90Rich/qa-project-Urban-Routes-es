from selenium import webdriver
from UrbanMethods import UrbanHome
import data
from selenium.webdriver import DesiredCapabilities

class TestcasesField:
    driver= None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.urbanhome = UrbanHome (cls.driver)
        cls.driver.implicitly_wait(3)
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}


#Rellenar direcciones
    def test_field_from(self):
        self.urbanhome.field_from()
    def test_field_to(self):
        self.urbanhome.field_to()

#Click pedir Taxi
    def test_click_taxi_button(self):
        self.urbanhome.click_taxi_button()

#Seleccionar tarifa comfort
    def test_click_button(self):
        self.urbanhome.click_comfort()

#prubeas telefono
    #def test_click_button_phone_number(self):
        #self.urbanhome.click_button_phone_number()
    #def test_click_field_phone_number(self): hacer click en el campo de numero de telefono?
        #self.urbanhome.click_fiel_phone_number()
    #def test_field_phone(self):
        #self.urbanhome.fiel_phone_number()
    #def test_click_next_button_phone_number(self):
        #self.urbanhome.click_next_button_phone_number()
    #def test_field_code(self):
        self.urbanhome.field_code()
    #def test_click_comfirm_code(self):
        #self.urbanhome.click_confirm_code()

#Prubeas de la tarjeta
    def test_click_method_pay(self):
        self.urbanhome.click_method_pay()
    def test_click_add_card(self):
        self.urbanhome.click_add_card()
    def test_field_add_card(self):
        self.urbanhome.field_add_card()
    def test_field_code_card(self):
        self.urbanhome.field_code_card()
    def test_click_other_space(self):
        self.urbanhome.click_other_space()
    def test_click_button_add(self):
        self.urbanhome.click_button_add()
    def test_click_button_close_card(self):
        self.urbanhome.click_button_close_card()







    @classmethod
    def teardown(cls):
        cls.driver.quit()


