import pandas as pd
import ollama

data = pd.read_csv("prompts/prompts.csv")
results = []

for _, row in data.iterrows():
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": row['prompt']}]
    )

    results.append({
        "prompt": row['prompt'],
        "category": row['category'],
        "response": response['message']['content']
    })

pd.DataFrame(results).to_csv("outputs/outputs.csv", index=False)

print("Experiment complete. Outputs saved.")
