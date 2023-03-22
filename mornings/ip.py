def is_valid_ip(ip_address: str) -> bool:
    octs = ip_address.split(".")
    if len(octs) != 4:
        return False

    for o in octs:
        if (
            not o.isnumeric()
            or o != str(int(o))
            or not 0 <= int(o) <= 255
        ):
            return False

    return True


print(is_valid_ip("12.255.56.1"))



# import ipaddress
#
#
# def is_valid_ip(ip_address: str) -> bool:
#     try:
#         return bool(ipaddress.IPv4Address(ip_address))
#     except Exception:
#         return False