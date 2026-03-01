import os
from dotenv import load_dotenv

load_dotenv()

def _rule_based(message: str):
    if not message:
        return {"action": "silent", "response": None}

    if "never" in message.lower() or "always" in message.lower():
        return {
            "action": "respond",
            "response": "[FLY] I’m noticing absolute language. Would it help to focus on this specific moment?"
        }

    return {"action": "silent", "response": None}


def analyze_message(message: str):
    """
    Returns:
      {"action": "silent", "response": None}
      {"action": "respond", "response": "[FLY] ..."}
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # No key provided — run in demo mode
        return _rule_based(message)

    # Lazy import so demo mode doesn't require OpenAI working
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    prompt = f"""
You are FLY, a calm and emotionally intelligent conversational assistant.
If the message contains escalation, absolute language, or cognitive distortion,
gently reframe it in one short response.
If no intervention is needed, reply with exactly: SILENT

Message:
{message}
"""

    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are FLY. Be concise and neutral. No lecturing."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        text = (resp.choices[0].message.content or "").strip()

        if text.upper() == "SILENT":
            return {"action": "silent", "response": None}

        return {"action": "respond", "response": f"[FLY] {text}"}

    except Exception:
        # If OpenAI fails, fallback gracefully
        return _rule_based(message)
