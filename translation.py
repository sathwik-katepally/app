import openai

openai.api_key = "REMOVED"

def translate_to_swedish(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Translate to Swedish while maintaining contextual meaning."},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']