from PyPDF2 import PdfReader
import pandas as pd

pdfData = "pdfFormularioCompacto.pdf"

def extractorDatosFormulario(x):
    reader = PdfReader(x)
    page = reader.pages[0]
    text = page.extract_text().split("\n")
    return print([text[i] for i in [12,13,14,15,16,17,18,19]])

extractorDatosFormulario(pdfData)