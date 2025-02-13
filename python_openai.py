import os
from openai import OpenAI # Importamos el paquete instalado en pip

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # Ponemos en OPENAI_API_KEY la clave api obtenida en la web adecuada
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o", # aquí se indica el modelo de GPT que se va a usar
)