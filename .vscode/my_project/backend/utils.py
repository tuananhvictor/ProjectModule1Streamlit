def get_password_hash(text: str, shift: int, mode: str) -> str:
    """
    Mã hóa hoặc giải mã văn bản bằng thuật toán Caesar cipher.

    Args:
        text (str): Văn bản cần mã hóa hoặc giải mã.
        shift (int): Số lượng ký tự cần dịch chuyển.
        mode (str): Chế độ thực hiện ('e' cho mã hóa và 'd' cho giải mã).

    Returns:
        str: Văn bản đã được mã hóa hoặc giải mã.
    """
    result = ""

    # Kiểm tra chế độ
    if mode not in ('e', 'd'):
        raise ValueError("Chế độ không hợp lệ. Sử dụng 'e' cho mã hóa hoặc 'd' cho giải mã.")

    for char in text:
        if char.isalpha():
            # Xác định mã ASCII gốc
            ascii_offset = 65 if char.isupper() else 97
            # Dịch chuyển ký tự
            shift_amount = shift if mode == 'e' else -shift
            # Mã hóa hoặc giải mã ký tự
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            # Giữ nguyên ký tự không phải là chữ cái
            result += char

    return result
