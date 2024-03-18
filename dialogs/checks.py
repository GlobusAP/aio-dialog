def name_check(text: str) -> str:
    if text.isalpha():
        return text
    raise ValueError


def age_check(text: str) -> str:
    if text.isdigit() and 2 <= int(text) <= 120:
        return text
    raise ValueError
