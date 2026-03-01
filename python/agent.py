import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_message(message: str):
    if not message:
        return {"action": "silent", "response": None}

    prompt = f"""
You are FLY, a calm and emotionally intelligent conversational assistant.
If the message contains escalation, absolute language, or cognitive distortion,
gently reframe it in one short response.
If no intervention is needed, return SILENT.

Message:
{message}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are FLY. Be concise and neutral."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    text = response.choices[0].message.content.strip()

    if "SILENT" in text.upper():
        return {"action": "silent", "response": None}

    return {"action": "respond", "response": f"[FLY] {text}"}
