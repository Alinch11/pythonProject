from typing import Set, Union, Any

import output as output

money = int(input('money = '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for value in per_cent.values():
    result = [int((value / 100 + 1) * money) for value in per_cent.values()]
print("deposit:", result)
print("Максимальная сумма, которую вы можете заработать - ", max(result))



