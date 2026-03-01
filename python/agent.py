def analyze_message(message: str):
    """
    Basic placeholder logic for FLY.
    """

    # Simple escalation detection
    if any(word in message.lower() for word in ["always", "never", "you always", "you never"]):
        return {
            "action": "reframe",
            "response": "[FLY] I’m noticing absolute language. Would it help to narrow this to the specific situation?"
        }

    return {
        "action": "silent",
        "response": None
    }
