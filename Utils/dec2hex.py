# La primera función convierte un numero entero en un numero hexadecimal
# La segunda función cumple el proceso contrario


def dec2hex(dec):
    hexa = ""
    hexa_dic = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    hexa_list = []

    while dec > 0:
        hexa_list.append(dec % 16)
        dec //= 16

    for i in hexa_list:
        if i in hexa_dic:
            hexa = hexa_dic[i] + hexa

    return hexa


def hexa2dec(hexa):
    inv_hexa = hexa[::-1].upper()
    hexa_dic = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    dec = 0

    for i in range(len(inv_hexa)):
        for j in hexa_dic:
            if inv_hexa[i] == j:
                dec += (16**i) * hexa_dic[j]

    return dec
