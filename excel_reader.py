import pandas as pd


def read_profiles_from_excel(file_path: str) -> pd.DataFrame:
    """
    Lee un archivo Excel que contiene la información de perfiles.

    Parámetros:
    ----------
    file_path : str
        Ruta del archivo Excel.

    Retorna:
    -------
    pd.DataFrame
        DataFrame con la información del Excel.
    """

    # read_excel carga el contenido del Excel en un DataFrame
    df = pd.read_excel(file_path)

    # Validación básica: el Excel no debería venir vacío
    if df.empty:
        raise ValueError("El archivo Excel está vacío.")

    return df
