autobiograficos = []


def numtolist(num):
    res = list(map(int, str(num)))
    return res


def listtonum(list):
    res = int("".join(map(str, list)))
    return res


def decomp(n):
    aux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list = numtolist(n)
    for i in list:
        aux[i] += 1
    return listtonum(aux[:len(str(n))])

number = 2476300000

while number < 10**10:
    maximum = max(int(x) for x in str(number))
    if len(str(number)) >= maximum + 1:
        if number == decomp(number):
            autobiograficos.append(number)
            print(autobiograficos)
    if number % 100000 == 0:
        print("Calculando...", number, autobiograficos)
    number += 1
print(autobiograficos)


