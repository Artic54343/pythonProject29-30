# class Human:
#     name = 'John'
#     surname = 'Doe'
#     prof = 'default'
#
#
#     def walk(self):
#         return 'Go'
#
#     def eat(self):
#         return 'Om nom nom'
#
# class Builder(Human):
#     prof = 'builder'
#     def buld_somerhing(self,structure):
#         return f'Buld {structure}'
#
#
# sten = Human()
# print(sten.walk())
# print(sten.eat())
#
# dender = Builder()
# print(dender.walk())
# print(dender.eat())
# print(dender.buld_somerhing('house'))


'''Создайте класс Human, который будет содержать
информацию о человеке.
С помощью механизма наследования, реализуйте класс
Builder (содержит информацию о строителе), класс Sailor
(содержит информацию о моряке), класс Pilot (содержит
информацию о летчике).
Каждый из классов должен содержать необходимые
для работы методы'''

# class Human:
#     name = 'John'
#     surname = 'Doe'
#     prof = 'default'
#
#     def walk(self):
#         return 'Go'
#
#     def eat(self):
#         return 'Om nom nom'
#
#
# class Builder(Human):
#     prof = 'builder'
#
#     def buld_somerhing(self, structure):
#         return f'Buld {structure}'
#
#
# class Sailor(Human):
#     prof = 'sailor'
#
#     def buld_floated(self, floats):
#         return f'swims in {floats}'
#
#
# class Pilot(Human):
#     prof = 'pilot'
#
#     def buld_flew(self, air):
#         return f'flies in {air}'
#
#
# sten = Human()
# print(sten.walk())
# print(sten.eat())
#
# dender = Builder()
# print(dender.walk())
# print(dender.eat())
# print(dender.buld_somerhing('house'))
#
# dender = Sailor()
# print(dender.walk())
# print(dender.eat())
# print(dender.buld_floated('sea'))
#
# dender = Pilot()
# print(dender.walk())
# print(dender.eat())
# print(dender.buld_flew('sky'))


'''Создайте класс c (паспорт), который будет
содержать паспортную информацию о гражданине заданной страны.
С помощью механизма наследования, реализуйте
класс ForeignPassport (загран.паспорт) производный от
Passport.
Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
заграничного паспорта.'''
# class Passport:
#     name = 'Artur'
#     surname = 'Zhdanov'
#     country = 'Ukraine'
#     room = '0948578465342354'
#
#     def show_number(self):
#         return '0948578465342354'
#
#     def show_the_country(self):
#         return 'Ukraine'
#
#
# class ForeignPassport(Passport):
#     surname = 'zhdanov'
#     visa = '3453454654657'
#     foreign_passport = '12233143435646'
#
#     def action_b(self):
#         return 'passport1'
#
#
# id = Passport()
# print(id.show_number())
# print(id.show_the_country())
#
# book = ForeignPassport()
# print(book.show_the_country())
# book.action_b()
# print(book.action_b())
# # print()

class Birth_identification_code:
    def __init__(self, code):
        if code == str:
            self.__code = code
        else:
            self.__code = '1231231232143'

    def __str__(self):
        return self.__code

class BirthDate:
    def __init__(self,date):
        rdate = date.split('.')
        if (int(rdate[0]) >= 1 and int(rdate[0]) <= 31) and (int(rdate[1]) >= 1 and int(rdate[1]) <= 12) and (int(rdate[2]) <= 2022):
            self.__date = date
        else:
            self.__date = '01.01.1970'
    def __str__(self):
        return self.__date

class Passport:
    name = 'Mike'
    surname = 'Wilson'
    date_of_birth = BirthDate('01.10.1991')
    identification_code = '1231231232143'
    passport_id = '213123145'
    country = 'Ukraine'
    city = 'Kyiv'
class ForeignPassport(Passport):
    visa_id = '131231231244534'
    international_id = '54354535'
    def full_info(self):
        return f'Name: {self.name} {self.surname} \nDate: {self.date_of_birth} \nIC: {self.identification_code} ' \
               f'\nID: {self.passport_id} \nCountry: {self.country}\nCity: {self.city}\nVisa ID:{self.visa_id}' \
               f'\nInternational passport ID: {self.international_id}'

citizen_1 = Passport()
print(citizen_1.date_of_birth)
print(citizen_1.city)
print(citizen_1.identification_code)
print(citizen_1.name)
print(citizen_1.passport_id)
print(citizen_1.__code())



#
# lass Country:
#     def __init__(self, country):
#
#         if country != int:
#             self.__country = country
#         else:
#             self.__country = 'Ukraine'
#     def __str__(self):
#         return self.__country
#
# class Passport:
#     name = 'Mike'
#     surname = 'Wilson'
#     date_of_birth = '01.08.1980'
#     identification_code = '1231231232143'
#     passport_id = '213123145'
#     country = Country('Poland')
#     city = 'Kyiv'
# class ForeignPassport(Passport):
#     visa_id = '131231231244534'
#     international_id = '54354535'
#     def full_info(self):
#         return f'Name: {self.name} {self.surname} \nDate: {self.date_of_birth} \nIC: {self.identification_code} ' \
#                f'\nID: {self.passport_id} \nCountry: {self.country}\nCity: {self.city}\nVisa ID:{self.visa_id}' \
#                f'\nInternational passport ID: {self.international_id}'
#
# citizen_1 = ForeignPassport()
# # print(citizen_1.full_info())
# print(citizen_1.country)