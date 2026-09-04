"""Mi primer chatbot — Q2003B.

El chasis del bot. No necesitas editar este archivo: tu parte
está en personalidad.py.
"""
import importlib
import os

from flask import Flask, jsonify, render_template, request

import personalidad

app = Flask(__name__)

MODELO = "gemini-3.5-flash"
HISTORIAL = []  # la conversación de esta corrida, por turnos


def hay_llave():
    return bool(os.environ.get("GEMINI_API_KEY"))


@app.route("/")
def portada():
    importlib.reload(personalidad)
    return render_template(
        "index.html",
        nombre=personalidad.NOMBRE_DE_TU_BOT,
        hay_llave=hay_llave(),
    )


@app.route("/preguntar", methods=["POST"])
def preguntar():
    if not hay_llave():
        return jsonify(error=(
            "Falta la llave. Agrégala en Secrets (candado del panel izquierdo) "
            "con el nombre GEMINI_API_KEY y vuelve a presionar Run."
        ))

    pregunta = (request.get_json(silent=True) or {}).get("pregunta", "").strip()
    if not pregunta:
        return jsonify(error="Escribe una pregunta primero.")

    # Se recarga en cada pregunta: tus cambios de personalidad entran al guardar.
    importlib.reload(personalidad)

    from google import genai

    cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    HISTORIAL.append({"role": "user", "parts": [{"text": pregunta}]})
    try:
        respuesta = cliente.models.generate_content(
            model=MODELO,
            contents=HISTORIAL[-20:],
            config={"system_instruction": personalidad.PERSONALIDAD},
        )
        texto = (respuesta.text or "").strip()
    except Exception as error:
        HISTORIAL.pop()
        return jsonify(error=f"El modelo no contestó: {error}")

    if not texto:
        HISTORIAL.pop()
        return jsonify(error="Llegó una respuesta vacía. Pregunta otra vez.")

    HISTORIAL.append({"role": "model", "parts": [{"text": texto}]})
    return jsonify(respuesta=texto, nombre=personalidad.NOMBRE_DE_TU_BOT)


@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    HISTORIAL.clear()
    return jsonify(listo=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
