def rgb_to_hex(r: int, g: int, b: int) -> str:
    def rounding(x):
        return min(255, max(x, 0))

    return ("{:02X}" * 3).format(rounding(r), rounding(g), rounding(b))


print(rgb_to_hex(-20, 275, 125))