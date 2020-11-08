import random

SubBytesList = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
                0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
                0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
                0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
                0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
                0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
                0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
                0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
                0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
                0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
                0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
                0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
                0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
                0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
                0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
                0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
InvSubBytesList = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
                   0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
                   0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
                   0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
                   0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
                   0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
                   0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
                   0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
                   0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
                   0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
                   0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
                   0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
                   0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
                   0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
                   0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
                   0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
Rcon = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
koef_matrix = [0x02, 0x03, 0x01, 0x01, 0x01, 0x02, 0x03, 0x01, 0x01, 0x01, 0x02, 0x03, 0x03, 0x01, 0x01, 0x02]
inv_koef_matrix = [0x0e, 0x0b, 0x0d, 0x09, 0x09, 0x0e, 0x0b, 0x0d, 0x0d, 0x09, 0x0e, 0x0b, 0x0b, 0x0d, 0x09, 0x0e]


def SubByte(byte):
    return SubBytesList[byte]


def InvSubByte(byte):
    return InvSubBytesList[byte]


def SubBytes(bytes_list):
    for i in range(len(bytes_list)):
        bytes_list[i] = SubBytesList[bytes_list[i]]
    return bytes_list


def InvSubBytes(bytes_list):
    for i in range(len(bytes_list)):
        bytes_list[i] = InvSubBytesList[bytes_list[i]]
    return bytes_list


def change_indexation_order(bytes_list, Nk=4, Nb=4):
    bytes_changed_indexes = []
    for i in range(0, Nk):
        for j in range(0, Nk*Nb):
            if j % Nk == i:
                bytes_changed_indexes.append(bytes_list[j])
    return bytes_changed_indexes


def ShiftRows(bytes_list, inv=1, Nk=4, Nb=4):
    bytes_list = change_indexation_order(bytes_list)
    row = []
    i = 0
    while i < len(bytes_list):
        if i // 4 == 0:
            i += 1
            continue
        else:
            for j in range(4):
                row.append(bytes_list[i])
                i += 1
            row = shift(row, (-1) * inv * ((i - 1) // 4))
            for j in range(4):
                bytes_list[i - 4 + j] = row[j]
            row = []
    bytes_list = change_indexation_order(bytes_list)
    return bytes_list


def InvShiftRows(bytes_list):
    return ShiftRows(bytes_list, -1)


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst


def MixColumns(bytes_list, Nk=4):
    new_bytes_list = []
    for i in range(Nk):
        j = 0
        row = []
        while j < len(bytes_list):
            if j // Nk == i:
                row.append(bytes_list[j])
            j += 1
        temp = 0
        k = 0
        while k < len(bytes_list):
            temp ^= gmul(row[k % 4], koef_matrix[k])
            k += 1
            if k % Nk == 0:
                new_bytes_list.append(temp)
                temp = 0
    return new_bytes_list


def InvMixColumns(bytes_list, Nk=4):
    new_bytes_list = []
    for i in range(Nk):
        j = 0
        row = []
        while j < len(bytes_list):
            if j // Nk == i:
                row.append(bytes_list[j])
            j += 1
        temp = 0
        k = 0
        while k < len(bytes_list):
            temp ^= gmul(row[k % 4], inv_koef_matrix[k])
            k += 1
            if k % Nk == 0:
                new_bytes_list.append(temp)
                temp = 0
    return new_bytes_list


def RotWord(row):
    return shift(row, -1)


def AddRoundKey(bytes_list, key_lists, Nb=4, Nk=4):
    for i in range(Nb):
        for j in range(Nk):
            bytes_list[i*Nb + j] ^= key_lists[i][j]
    return bytes_list


def KeyExpansion(key, Nk=4, Nb=4, Nr=10):
    key_expanded = []

    for i in range(0, Nk):
        temp = []
        for j in range(0, Nk):
            temp.append(key[4 * i + j])
        key_expanded.append(temp)
    for i in range(Nk, Nb*(Nr + 1)):
        temp = key_expanded[i - 1].copy()
        temp2 = []
        if i % Nk == 0:
            temp = SubBytes(RotWord(temp))
            temp[0] ^= Rcon[i // Nk]
        for j in range(len(temp)):
            temp2.append(key_expanded[i - Nk][j] ^ temp[j])
        key_expanded.append(temp2)

    return key_expanded


# Умножение в поле Галуа
def gmul(a, b):
    p = 0
    while a and b:
        if b & 1:
            p ^= a
        if a & 0x80:
            a = (a << 1) ^ 0x11B
        else:
            a <<= 1
        b >>= 1
    return p


def Cipher(bytes_list, key, Nr=10, Nb=4):
    bytes_list = AddRoundKey(bytes_list, key[0:Nb])

    for this_round in range(1, Nr):
        bytes_list = SubBytes(bytes_list)
        bytes_list = ShiftRows(bytes_list)
        bytes_list = MixColumns(bytes_list)
        bytes_list = AddRoundKey(bytes_list, key[(this_round * Nb):((this_round + 1) * Nb)])

    bytes_list = SubBytes(bytes_list)
    bytes_list = ShiftRows(bytes_list)
    bytes_list = AddRoundKey(bytes_list, key[(Nr * Nb):((Nr + 1) * Nb)])

    return bytes_list


def InvCipher(bytes_list, key, Nr=10, Nb=4):
    bytes_list = AddRoundKey(bytes_list, key[(Nr * Nb):((Nr + 1) * Nb)])

    for this_round in range(Nr - 1, 0, -1):
        bytes_list = InvShiftRows(bytes_list)
        bytes_list = InvSubBytes(bytes_list)
        bytes_list = AddRoundKey(bytes_list, key[(this_round * Nb):((this_round + 1) * Nb)])
        bytes_list = InvMixColumns(bytes_list)

    bytes_list = InvShiftRows(bytes_list)
    bytes_list = InvSubBytes(bytes_list)
    bytes_list = AddRoundKey(bytes_list, key[0:Nb])

    return bytes_list


def get_key(key_file, block_size):
    with open(key_file, "rb") as key_file:
        key = key_file.read(block_size)
        key = list(key)
        if len(key) < block_size:
            length_of_key = len(key)
            for i in range(length_of_key, block_size):
                key.append(key[i % length_of_key])
    return key


def encrypt():
    inputfile = input("Укажите файл, который необходимо зашифровать: ")
    if inputfile == "":
        inputfile = "input.txt"

    outputfile = input("Укажите файл, в который будет записана шифровка: ")
    if outputfile == "":
        outputfile = "encrypted.bin"

    keyfile = input("Укажите файл, в котором находится ключ: ")
    if keyfile == "":
        keyfile = "key.txt"

    encryption = True
    read_process_write(inputfile, outputfile, keyfile, encryption)
    return 0


def decrypt():
    inputfile = input("Укажите файл, который необходимо расшифровать: ")
    if inputfile == "":
        inputfile = "encrypted.bin"

    outputfile = input("Укажите файл, в который будет записана расшифровка: ")
    if outputfile == "":
        outputfile = "decrypted.txt"

    keyfile = input("Укажите файл, в котором находится ключ: ")
    if keyfile == "":
        keyfile = "key.txt"

    encryption = False
    read_process_write(inputfile, outputfile, keyfile, encryption)
    return 0


def read_process_write(inputfile, outputfile, keyfile, encryption):
    block_size = 16  # Для AES-128 размер и блока, и ключа равен 128 битам или 16 байтам
    key = get_key(keyfile, block_size)
    key = KeyExpansion(key)
    with open(inputfile, "rb") as input_file:
        with open(outputfile, "wb") as output_file:
            last_block = False
            while not last_block:
                bytes_raw = input_file.read(block_size)
                if len(bytes_raw) == 0:
                    break
                elif len(bytes_raw) < block_size:
                    last_block = True
                    bytes_raw = list(bytes_raw)
                    while len(bytes_raw) < block_size:
                        bytes_raw.append(0x00)
                    bytes_raw = bytes(bytes_raw)

                if encryption:
                    bytes_list = Cipher(list(bytes_raw), key)
                else:
                    bytes_list = InvCipher(list(bytes_raw), key)

                bytes_list = bytes(bytes_list)
                output_file.write(bytes_list)


def generate_key():
    keyfile = input("Укажите файл, в который будет записан ключ: ")
    if keyfile == "":
        keyfile = "key.txt"
    block_size = 16
    with open(keyfile, "wb") as key_file:
        random.seed()
        key_list = []
        for i in range(0, block_size):
            key_list.append(random.randint(0, 255))
        key_list = bytes(key_list)
        key_file.write(key_list)
    return 0


def main():
    print("AES-128")
    print("Доступные режимы работы:")
    print("e для зашифрования")
    print("d для расшифровывания")
    print("g для генерации ключа")
    sym = input("Введите букву, соответствующую режиму: ")
    if sym == 'e':
        encrypt()
    elif sym == 'd':
        decrypt()
    elif sym == 'g':
        generate_key()
    else:
        print("Указан неверный параметр. Программа закрыта")
        return 0
    print("Программа успешно завершила работу")
    return 0


if __name__ == "__main__":
    main()
