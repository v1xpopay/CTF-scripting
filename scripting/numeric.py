# Numerical expression in binary-hex-decimal , Decimal to Binary and Hex

num = 56
binary_repr = bin(num) 
hex_repr = hex(num)
# Bin to Dec
binary_str = "10101"
decimal_from_bin = int(binary_str, 2)
# Hex to Dec
hex_str = "2F"
decimal_from_hex = int(hex_str, 16)
# Bin to Hex
binary_str = "1111011011"
hex_from_bin = hex(int(binary_str, 2))
