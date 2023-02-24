def rgb_to_hex(r: int, g: int, b: int) -> str:
    def rounding(x):
        return min(255, max(x, 0))

    return ("{:02X}" * 3).format(rounding(r), rounding(g), rounding(b))


print(rgb_to_hex(-20, 275, 125))



#
# def check_range_color(color: int) -> int:
#     if color < 0:
#         return 0
#     elif color > 255:
#         return 255
#     return color
#
#
# def rgb_to_hex(r: int, g: int, b: int) -> str:
#     res = ""
#     for c in (r, g, b):
#         c = hex(check_range_color(c))[2::].upper()
#         if len(c) == 1:
#             c = "0" + c
#         res += c
#     return res
