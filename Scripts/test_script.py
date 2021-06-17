import pytest
from selenium import webdriver
import time
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


#Caso #1: Realizar la creacion de un usuario de forma automatizada.
@mark.registrar_usuario
def test_registrar_usuario():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    Sign_in_button = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'Create an account')]"))
    time.sleep(3)
    Email_address = driver.find_element_by_id("email_create").send_keys("sammy2248@gmail.com")
    time.sleep(3)
    Create_an_account_btn = driver.find_element_by_id("SubmitCreate").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//h3[contains(text(),'Your personal information')]"))
    #Titulo: YOUR PERSONAL INFORMATION
    Titulo = driver.find_element_by_id("id_gender1").click()
    Primer_nombre = driver.find_element_by_id("customer_firstname").send_keys("Sammy")
    Segundo_nombre = driver.find_element_by_id("customer_lastname").send_keys("Hernandez")
    Contraseña = driver.find_element_by_id("passwd").send_keys("12345/*-")
    Dia = driver.find_element_by_id("days").send_keys("18")
    Mes = driver.find_element_by_id("months").send_keys("October")
    Año = driver.find_element_by_id("years").send_keys("1990")
    #Titulo: YOUR ADDRESS
    Titulo = driver.find_element_by_id("id_gender1").click()
    Primer_nombre = driver.find_element_by_id("customer_firstname").send_keys("Sammy")
    Compañnia = driver.find_element_by_id("company").send_keys("Software Company Develop")
    Direccion = driver.find_element_by_id("address1").send_keys("New York")
    Direccion2 = driver.find_element_by_id("address2").send_keys("Manhattan street ")
    Ciudad = driver.find_element_by_id("city").send_keys("New York")
    Estado = Select(driver.find_element_by_id("id_state"))
    Estado.select_by_value("32")
    Codigo_postal = driver.find_element_by_id("postcode").send_keys("10001")
    #El campo pais, se autocompleta cuando se selecciona el estado.
    Informacion_adicional = driver.find_element_by_id("other").send_keys("Prueba")
    Telefono = driver.find_element_by_id("phone").send_keys("1-646-336-0522")
    Celular = driver.find_element_by_id("phone_mobile").send_keys("1-212-674-5377")
    Apodo = driver.find_element_by_id("alias").send_keys("SammyHernandez")
    btn_registro = driver.find_element_by_id("submitAccount").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//h1[contains(text(),'My account')]"))
    time.sleep(5)
    driver.close()

#Caso #2: Realizar la verificacion de que la pagina no permita registrar el mismo correo
@mark.validar_correo
def test_validar_correo():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    Sign_in_button = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'Create an account')]"))
    Email_address = driver.find_element_by_id("email_create").send_keys("sammy181090@gmail.com")
    Create_an_account_btn = driver.find_element_by_id("SubmitCreate").click()
    time.sleep(3)
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[@id = 'create_account_error']"))
    time.sleep(5)
    driver.close()

#Caso #3: Agregar un producto al carrito.
@mark.agregar_producto
def test_agregar_producto():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[@title = 'Blouse' and @alt = 'Blouse']"))
    Producto = driver.find_element_by_xpath("//*[@title = 'Blouse' and @alt = 'Blouse']").click()
    time.sleep(5)
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//h1[text() = 'Blouse']"))
    Agrega_al_carrito = driver.find_element_by_id("add_to_cart").click()
    time.sleep(5)
    Proceder_a_revisar = driver.find_element_by_xpath("//*[@title = 'Proceed to checkout']").click()
    time.sleep(10)
    WebDriverWait(driver, timeout=30).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'Unit price')]"))
    driver.close()

#Caso #4: Acceder a la pagina web, utilizando un usuario registrdo.
@mark.iniciar_sesion
def test_iniciar_sesion():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    btn_sign_in = driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_id("login_form"))
    Usuario = driver.find_element_by_id("email").send_keys("sammy181090@gmail.com")
    Contraseña = driver.find_element_by_id("passwd").send_keys("12345/*-", Keys.ENTER)
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'My account')]"))
    time.sleep(3)
    driver.close()

#Caso #5: completar y enviar el formulario de contacto.
@mark.formulario_contacto
def test_formulario_contacto():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    btn_contacto = driver.find_element_by_id("contact-link").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'send a message')]"))
    Cabecera = Select(driver.find_element_by_id("id_contact"))
    Cabecera.select_by_value("2")
    Correo = driver.find_element_by_id("email").send_keys("sammy181090@gmail.com")
    Numero_referencia = driver.find_element_by_id("id_order").send_keys("123456")
    Subir_archivo = driver.find_element_by_id("fileUpload").send_keys("D:\\Zerobank\\Texto.txt")
    Mensaje = driver.find_element_by_id("message").send_keys("Esto es una prueba automatizada")
    Enviar = driver.find_element_by_id("submitMessage").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'Customer service - Contact us')]"))
    time.sleep(3)
    driver.close()

#Caso #6: Validar que el formulario de contacto no se envie si hay un campo vacio.
@mark.validar_formulario
def test_validar_formulario():
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php")
    btn_contacto = driver.find_element_by_id("contact-link").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[contains(text(), 'send a message')]"))
    Cabecera = Select(driver.find_element_by_id("id_contact"))
    Cabecera.select_by_value("2")
    Correo = driver.find_element_by_id("email").send_keys("sammy181090@gmail.com")
    Numero_referencia = driver.find_element_by_id("id_order").send_keys("123456")
    Subir_archivo = driver.find_element_by_id("fileUpload").send_keys("D:\\Zerobank\\Texto.txt")
    Enviar = driver.find_element_by_id("submitMessage").click()
    WebDriverWait(driver, timeout=20).until(lambda d: driver.find_element_by_xpath("//*[@class = 'alert alert-danger']"))
    time.sleep(3)
    driver.close()




