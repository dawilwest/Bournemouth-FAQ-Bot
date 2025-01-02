from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

git remote add origin https://github.com/Tamunonengiyeofori/Bournemouth-FAQ-Bot.git
git branch -M main
git push -u origin main