def negation_value(negations: str, val: bool) -> bool:
    return bool(not val if len(negations) % 2 else val)
