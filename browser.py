from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def open_chrome(url: str, chromedriver_path: str) -> webdriver.Chrome:
    """
    Abre Google Chrome y navega a una URL específica.

    Parámetros:
    ----------
    url : str
        URL que se desea abrir.
    chromedriver_path : str
        Ruta donde se encuentra chromedriver.exe

    Retorna:
    -------
    webdriver.Chrome
        Instancia activa del navegador.
    """

    # Opciones de Chrome
    chrome_options = Options()

    # Estas opciones ayudan a evitar errores comunes en VMs
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")

    # Servicio que apunta al chromedriver
    service = Service(chromedriver_path)

    # Inicializamos el navegador
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abrimos la URL
    driver.get(url)

    return driver
