def binary_to_hex(binary_str):
    # Sử dụng một từ điển để ánh xạ giá trị nhị phân thành ký tự thập lục phân
    hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    # Đảm bảo độ dài của chuỗi nhị phân là bội số của 4 để dễ chia thành nhóm 4 bit
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str

    hex_str = ''
    
    # Chia chuỗi nhị phân thành các nhóm 4 bit và chuyển đổi thành ký tự thập lục phân
    for i in range(0, len(binary_str), 4):
        hex_digit = hex_dict[binary_str[i:i + 4]]
        hex_str += hex_digit

    return hex_str

# Nhập một chuỗi nhị phân từ người dùng
binary_str = input("Nhập một số nhị phân: ")

# Chuyển đổi chuỗi nhị phân thành chuỗi thập lục phân
hexadecimal_str = binary_to_hex(binary_str)

# In chuỗi thập lục phân
print("Số thập lục phân tương ứng là:", hexadecimal_str)
