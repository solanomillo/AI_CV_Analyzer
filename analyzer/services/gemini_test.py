import os
import google.generativeai as genai
from django.conf import settings


def test_gemini_connection():
    """
    Prueba básica de conexión con la API de Google Gemini
    """
    API_KEY = os.getenv("GEMINI_API_KEY")
    MODELO_NAME = os.getenv("GEMINI_MODELO_FLASH", "gemini-2.5-flash")

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY no encontrada en variables de entorno")

    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel(MODELO_NAME)

    response = model.generate_content(
        "Respondé con una sola frase: ¿funciona la conexión?"
    )

    return response.text
