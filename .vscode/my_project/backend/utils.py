def get_password_hash(text: str, shift: int, mode: str) -> str:
    result = ""
    if mode not in ('e', 'd'):
        raise ValueError("Chế độ không hợp lệ. Sử dụng 'e' cho mã hóa hoặc 'd' cho giải mã.")

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift_amount = shift if mode == 'e' else -shift
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result
