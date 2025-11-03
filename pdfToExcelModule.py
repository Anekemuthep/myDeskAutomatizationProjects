from PyPDF2 import PdfReader
import pandas as pd
import re

pdfData = "pdfFormularioCompacto.pdf"

def extractorDatosFormulario(x):
    reader = PdfReader(x)
    page = reader.pages[0]
    text = page.extract_text().split("\n")
    return [text[i] for i in [14,15,16,17,18,19]]

data= extractorDatosFormulario(pdfData)

import pandas as pd
import re
import ast

def parse_iva_data(data_input):
    """
    Extrae pares clave-valor de una lista o texto con formato de lista.
    Devuelve un DataFrame con una sola fila de datos numéricos.
    """
    # Convertir string en lista si es necesario
    if isinstance(data_input, str):
        try:
            data_list = ast.literal_eval(data_input)
        except Exception:
            raise ValueError("El texto recibido no tiene formato de lista válido.")
    elif isinstance(data_input, list):
        data_list = data_input
    else:
        raise ValueError("El argumento debe ser una lista o un texto que contenga una lista.")

    if not data_list:
        raise ValueError("La lista está vacía.")

    result = {}

    # Procesar todos los ítems de la lista
    for item in data_list:
        match = re.match(r'\d*\s*(.*?)\s+([\d\.]+)$', item.strip())
        if match:
            key = match.group(1).strip().lower()
            value = int(match.group(2).replace('.', ''))
            result[key] = value

    return pd.DataFrame([result])

#data = [
#    '562MONTO SIN DER. A CRED. FISCAL 10.000',
#    '504REMANENTE CRÉDITO MES ANTERIOR 65.346',
#    '544RECUP. IMP. ESP. DIESEL (Art. 2) 0',
#    '779Monto de IVA postergado 6 o 12 cuotas 0',
#    '537TOTAL CRÉDITOS 65.346',
#    '089IMP. DETERM. IVA 0'
#]

df = parse_iva_data(data)
print(df)