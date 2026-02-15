import ollama

response = ollama.chat(
    model="mistral",
    messages=[
        {"role": "user", "content": "Explain AI alignment in simple terms."}
    ]
)

print(response['message']['content'])
