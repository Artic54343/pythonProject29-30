# import datetime
class Mobile:
    color = 'red'
    ram = 4
    _storage = 32 #защищённый
    __model = 'Xiaomi'

    def show_time(self):
        return datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')

    def _change_ram(self, new_ram):
        self.ram = new_ram

    def __change_imei(self, new_imei):
        self.imei = new_imei
#
# mi8 = Mobile()
# print(mi8.ram)
# mi8.ram = 8
# print(mi8.ram)
# print(mi8._storage)
# mi8._storage = 8
# print(mi8._storage)
#
# print(mi8.show_time())
# print(mi8.ram)
# mi8._change_ram(12)
# print(mi8.ram)
# mi8.__Mobile = 'IPhone'
# mi8.__change_imei(456)
# print(mi8.imei)
#
# class Blender:
#     def cut(self,product):
#         if product == 'ise':
#             return 'isecream'
#         elif product == 'meat':
#             return 'mince'
#         else:
#             return 'cut '+product
#
# sliser = Blender()
# print(sliser.cut('ise'))
# print(sliser.cut('meat'))
# print(sliser.cut('tree'))


# class Storage:
#     __money = 0
#
#     def __change_money(self,count):
#         if count > 0:
#             self.__money = self.__money + count
#
#     def deposite(self,secret_key, count):
#         if secret_key == 'qwerty':
#             self.__shenge_money(count)
#
#
#
# FortNox = Storage()
# FortNox.depoosite('qwerty', 1000)


class Juicer:
    def squeeze(self, product):
        if product == 'carrot':
            return 'carrot juice'
        elif product == 'grape':
            return 'grape juice'
        elif product == 'potatoes':
            return 'potato juice'
        else:
            return 'squeeze '+product

    def Juicer_cleaning(self, product):
        if product == 'carrot':
            return 'cleaning carrot'
        elif product == 'grape':
            return 'cleaning grape'
        elif product == 'potatoes':
            return 'cleaning potatoes'
        else:
            return 'cleaning' + product
cup = Juicer()
print(cup.squeeze('grape'))
print(cup.squeeze('carrot'))
print(cup.squeeze('potatoes'))
print(cup.squeeze('melon'))
print(cup.Juicer_cleaning('grape'))

