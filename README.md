# Mi primer chatbot

Un chatbot que corre en tu Replit, con la personalidad que tú le escribas.
El modelo es Gemini, con una llave gratuita que tú mismo generas.

## Ponlo a andar (5 pasos)

1. **Importa este repositorio a Replit.** Create Repl, pestaña
   *Import from GitHub*, y pega la liga de este repo.
2. **Instala lo necesario.** En la Shell, una sola vez:

   ```
   pip install -r requirements.txt
   ```

3. **Crea tu llave gratis.** Entra a `aistudio.google.com` con tu cuenta de
   Google, botón *Get API Key*, *Create API Key*, y cópiala. Es tuya: no la
   compartas ni la pegues en ningún archivo.
4. **Guárdala en Secrets.** En Replit, el candado del panel izquierdo.
   Nombre: `GEMINI_API_KEY`. Valor: tu llave. Los Secrets existen para esto:
   la llave queda fuera del código y fuera de GitHub.
5. **Presiona Run.** Se abre el chat en el Webview. Pregunta algo.

## Hazlo tuyo

Todo tu trabajo va en **un solo archivo: `personalidad.py`**.

- `NOMBRE_DE_TU_BOT`: ponle nombre.
- `PERSONALIDAD`: dile quién es, cómo habla y en qué ayuda.

Guarda el archivo y haz tu siguiente pregunta: el cambio entra de inmediato,
sin reiniciar nada. Prueba las ideas comentadas al final del archivo.

## Si algo truena

| Lo que ves | Qué pasa | Qué hacer |
|---|---|---|
| Aviso "Falta la llave" | El Secret no existe o tiene otro nombre | El nombre exacto es `GEMINI_API_KEY`; detén y vuelve a dar Run |
| `Module not found` | Falta instalar | `pip install -r requirements.txt` en la Shell |
| `Address already in use` | El programa ya corre en el otro carril | Detenlo donde lo arrancaste: botón rojo de Console si fue con Run, Ctrl+C si fue en la Shell |
| El modelo no contesta | Llave mal copiada o demasiadas preguntas seguidas | Revisa el Secret; espera un minuto y reintenta |

## Cómo está hecho

- `app.py`: el chasis (Flask). No necesitas tocarlo.
- `personalidad.py`: tu archivo.
- `templates/` y `static/`: la cara del chat.
- El modelo se llama por el SDK `google-genai`; la conversación vive en la
  memoria del programa mientras corre, y el botón Reiniciar la borra.
