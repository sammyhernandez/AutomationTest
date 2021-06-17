#Prueba de Alcance
Este proyecto de automatizacion esta escrito en Python, y usando pytest framework

Este proyecto compila usando Data-Driven Test.

La prueba en este proyecto usa las marcas:registrar_usuario, validar_correo,agregar_producto,iniciar_sesion,validar_formulario para identificar cada una de las pruebas.

#Chrome WebDriver
En el orden a correr las pruebas de interfaz de usuario, es necesario tener en el PATH de nuestras variables de entorno el chrome driver,
puede ser descargado desde aqui.
(https://chromedriver.chromium.org/)

#En el orden de correr el Banco de pruebas (test suite) es necesario tener el pytest instalado.
bash
pip install -U pystest

#Correr Banco de pruebas
Ir a la carpeta del proyecto y ejecutar esta linea de comando siguiendo las optiones
pytest: run all test
pytest: -v | pytest --verbose: corre todas las pruebas en modo verbose

#Correr una prueba especifica
Para correr una prueba especifica, puedes usar la marca de anotacion en pytest
bash
pytest -m validar_formulario
