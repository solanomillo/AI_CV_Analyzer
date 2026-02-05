import json
import re
import google.generativeai as genai
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from django.conf import settings


class CVAnalyzerAgent:
    """
    Agente responsable de analizar CVs usando IA (Gemini)
    """

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODELO_FLASH)

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extrae texto desde un PDF de forma segura
        """
        try:
            reader = PdfReader(pdf_path)
        except PdfReadError:
            raise ValueError("❌ El archivo PDF está dañado o no es válido")

        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text.strip()

    def build_prompt(self, cv_text: str, target_position: str) -> str:
        """
        Prompt estricto orientado a salida JSON válida
        """
        return f"""
Actuás como un reclutador técnico senior experto en ATS.

Analizá el siguiente CV para el puesto: {target_position}

CV:
\"\"\"
{cv_text}
\"\"\"

REGLAS OBLIGATORIAS:
- Respondé ÚNICAMENTE con JSON válido
- NO markdown
- NO texto adicional

Formato requerido:

{{
  "strengths": ["..."],
  "errors": ["..."],
  "suggestions": ["..."],
  "optimized_summary": "..."
}}
"""

    def _clean_json_response(self, raw_text: str) -> str:
        """
        Limpia la respuesta del modelo y extrae el JSON
        """
        cleaned = re.sub(r"```json|```", "", raw_text).strip()
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        return match.group(0) if match else cleaned

    def analyze(self, pdf_path: str, target_position: str) -> dict:
        """
        Ejecuta el análisis completo del CV
        """
        cv_text = self.extract_text_from_pdf(pdf_path)

        if not cv_text:
            raise ValueError("❌ No se pudo extraer texto del CV")

        response = self.model.generate_content(
            self.build_prompt(cv_text, target_position)
        )

        raw_text = (response.text or "").strip()

        if not raw_text:
            raise ValueError("❌ Gemini no devolvió contenido")

        cleaned_json = self._clean_json_response(raw_text)

        try:
            return json.loads(cleaned_json)
        except json.JSONDecodeError:
            raise ValueError(
                "❌ La IA devolvió un formato inválido.\n\n"
                "Respuesta recibida:\n"
                f"{raw_text}"
            )
