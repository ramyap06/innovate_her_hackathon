import os
from groq import Groq

client = Groq(
    api_key= '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',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "WAP to generate a star with triangle ",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)