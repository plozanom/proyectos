def dec2bin(num):
    binary = ""
    dec = num

    while dec > 1:
        binary = str(dec % 2) + binary
        dec = dec // 2
    else:
        binary = str(dec) + binary

    if len(binary) < 6:
        binary = (6 - len(binary)) * "0" + binary

    return binary


def bin2dec(bin):
    dec = 0

    for i in range(len(bin)):
        if bin[i] == "0":
            dec += 0
        elif bin[i] == "1":
            dec += 2 ** (len(bin) - (i + 1))
        else:
            return f"El numero {bin} no es un binario"

    return dec
