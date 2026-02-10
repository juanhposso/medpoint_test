import os
import sys
from browser import open_chrome
from excel_reader import read_profiles_from_excel
from login import login


def main():
    """
    Función principal de la aplicación.
    """

    # =========================
    # CONFIGURACIÓN
    # =========================

    if getattr(sys, 'frozen', False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    EZCAP_URL = "http://mpmezapp2/pno/login.aspx"
    CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver.exe")
    EXCEL_PATH = os.path.join(BASE_DIR, "input", "profiles.xlsx")

    print("\n-----------------")
    print("BASE_DIR:", BASE_DIR)
    print("EXCEL_PATH:", EXCEL_PATH)
    print("EXISTS:", os.path.exists(EXCEL_PATH))
    print("\n-----------------\n")

    # =========================
    # VALIDACIÓN DEL EXCEL
    # =========================

    if not os.path.exists(EXCEL_PATH):
        print("ERROR: No se encontró el archivo Excel.")
        print(f"Ruta esperada:\n{EXCEL_PATH}")
        input("Presiona ENTER para salir...")
        sys.exit(1)

    # =========================
    # LECTURA DE EXCEL
    # =========================

    try:
        profiles_df = read_profiles_from_excel(EXCEL_PATH)
        print("Excel cargado correctamente")
        print(profiles_df.head())
    except Exception as e:
        print("No se pudo leer el Excel:", e)
        input("Presiona ENTER para salir...")
        sys.exit(1)

    # =========================
    # ABRIR NAVEGADOR
    # =========================

    driver = open_chrome(
        url=EZCAP_URL,
        chromedriver_path=CHROMEDRIVER_PATH
    )

    login(driver)
    
    input("Presiona ENTER para cerrar el navegador y salir...")
    driver.quit()


if __name__ == "__main__":
    main()
