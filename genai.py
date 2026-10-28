from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
