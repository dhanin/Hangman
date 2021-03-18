def what_to_do(instructions):
    sentence = str(instructions).startswith("Simon says") or str(instructions).endswith("Simon says")
    if sentence:
        return f'I {str(instructions).replace("Simon says", "").lower().replace("  "," ").strip()}'
    else:
        return f"I won't do it!"
