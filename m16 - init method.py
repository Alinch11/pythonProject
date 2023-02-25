# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}.'
#
#
# rect_1 = Rectangle(5, 10, 50, 100)
# print(rect_1)

# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая информация: имя, фамилия, город, баланс.

# Далее сделайте вывод о клиентах в консоль в формате:

# «Иван Петров. Москва. Баланс: 50 руб.»
# class Client:
#     def __init__(self, name, city, balance):
#         self.name = name
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         return f'{self.name}. {self.city}. Баланс:{self.balance} руб.'
#
#
# client_1 = Client('Иван Петров', 'Москва', 50)
# print(client_1)


# необходимо написать программу, которая позволит создать список гостей. В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self,first_name, second_name, city, ):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city

    def __str__(self):
        return f'{self.first_name} {self.second_name} - {self.city} '

    def get_guest(self):
        return f'{self.first_name} {self.second_name},city {self.city}'


client1 = Client( "William", "Shakespeare","Moscow")
client2 = Client("Charles", "Dickens","Sochi")
client3 = Client("Lewis", "Carroll","Oxford")

guest_list = [client1, client2, client3]
for guest in guest_list:
    print(guest.get_guest())

