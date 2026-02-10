import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def login(driver, timeout: int = 30):
    """
    Realiza el login en la aplicación EZCAP usando variables de entorno.
    """

    username = os.getenv("EZCAP_USERNAME")
    password = os.getenv("EZCAP_PASSWORD")

    if not username or not password:
        raise ValueError("Variables de entorno EZCAP_USERNAME o EZCAP_PASSWORD no definidas")

    wait = WebDriverWait(driver, timeout)

    try:
        # Esperar input de usuario
        user_input = wait.until(
            EC.presence_of_element_located((By.ID, "txtUserID"))
        )

        pass_input = wait.until(
            EC.presence_of_element_located((By.ID, "txtPWD"))
        )

        # Escribir credenciales
        user_input.clear()
        user_input.send_keys(username)

        pass_input.clear()
        pass_input.send_keys(password)

        # En ASP.NET normalmente el botón está dentro del form
        pass_input.send_keys(Keys.ENTER)

        # Esperar que el login termine (input desaparece)
        wait.until(
            EC.invisibility_of_element_located((By.ID, "txtUserID"))
        )

        print("✅ Login exitoso")

    except TimeoutException:
        raise RuntimeError("❌ Error: el login no se completó o la página no respondió")
