import os
import openai
openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)