x = int(input('Введите количество билетов: '))
s = 0
for number in range(x):
    print('Билет №', number + 1)
    y = int(input('Введите возраст участника: '))
    if y < 18:
        s = s
    elif 18 <= y < 25:
        s += 990
    else:
        s += 1390
if x > 3:
    s *= 0.9
print('Стоимость: ', s)
