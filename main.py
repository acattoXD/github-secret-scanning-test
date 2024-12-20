from openai import OpenAI

# This is only a project to test the GitHub Secret Scanning feature. This is a real API key, but it's not used in any real project. This key is read-only, meaning that you can't even do anything with the key.
# A report will be made in the README.md file to show that the secret scanning feature is working.
# The key will be removed after the report is made.

client = OpenAI(api_key="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")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is human life expectancy in the United States?"},
    ]
)
print(response.choices[0].message.content)
