def convert_byte(ascii_str: bytes, val: int = 0) -> list:
    res = []
    for i in ascii_str:
        res.append(i + val)
    return res
