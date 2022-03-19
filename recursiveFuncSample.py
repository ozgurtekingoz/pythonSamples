# coding=utf-8

def recSum(list):
    if len(list) == 0:
        return 0

    return list[0] + recSum(list[1:])


#count = recSum([1, 2, 3, 4, 5, 6])
#print (count)


def factorialResult(sayi):
    if sayi != 0:
        return sayi * factorialResult(sayi - 1)
    return 1


#result = factorialResult(input("Sayı Giriniz: "))
#print (result)
