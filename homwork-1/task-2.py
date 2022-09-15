rubles, kopecks = map(int, input("Enter pie price: ").split())
count = int(input("Enter pie count: "))

# считаем стоимость пирожка в копейках
price = rubles * 100 + kopecks
#считаем стоимость count штук
cost = count * price

# выводим с подсчетами
print("Cost ", count, " pies is ", cost // 100, " rub. ", cost % 100, " kop.", sep="")
