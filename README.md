# Proyecto Urban Routes


Este proyecto automatiza el flujo de reserva de taxis en la plataforma *Urban Routes*.
Se utiliza `Selenium WebDriver` en `Python`.

## Estrucutura del proyecto

- main.py: Contiene la función `retrieve_phone_code` que entrega el codigo del SMS.
- data.py: Contiene datos de entrada (como direcciones, teléfono, etc.).
- UrbanLocators.py: Contiene los localizadores de elementos web (XPaths, IDs, etc.).
- UrbanMethods.py: Contiene funciones/metodos reutilizables para interactuar con la web.
- UrbanTestcases.py: Archivo principal de pruebas.
- .gitignore: Archivos que Git debe ignorar

## Requisitos

Necesitas tener lo siguiente:
- pytest intalado
- selenium instalado
- Google Chrome y ChromeDriver

para poder ejecutar las pruebas y selenieum.

## Como ejecutar las pruebas

Desde la terminal, estando en la carpeta del proyecto:
pytest UrbanTestcases.py

## Lista de comprobación de pruebas

1. Configurar la dirección.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor en el modal.

## Resumen de pruebas realizadas

============================= test session starts =============================
collecting ... collected 9 items

UrbanTestcases.py::TestcasesField::test_1_field_and_click 
UrbanTestcases.py::TestcasesField::test_2_select_tariff 
UrbanTestcases.py::TestcasesField::test_3_phone 
UrbanTestcases.py::TestcasesField::test_4_pay_method 
UrbanTestcases.py::TestcasesField::test_5_comment 
UrbanTestcases.py::TestcasesField::test_6_slider 
UrbanTestcases.py::TestcasesField::test_7_ice 
UrbanTestcases.py::TestcasesField::test_8_taxi 
UrbanTestcases.py::TestcasesField::test_9_information 

============================= 9 passed in 39.02s ==============================
PASSED         [ 11%]PASSED           [ 22%]PASSED                   [ 33%]PASSED              [ 44%]PASSED                 [ 55%]PASSED                  [ 66%]PASSED                     [ 77%]PASSED                    [ 88%]PASSED             [100%]
Process finished with exit code 0


## Notas

- El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación del SMS del teléfono.
- Asegúrate de que el sitio web esté disponible antes de correr las pruebas.
- En todos los metodos se usa `WebDriverWait` para mayor estabilidad en las pruebas.


## Autor

- Ricardo Gómora, cohort QA26- 8.vo sprint
- 15/05/2025

