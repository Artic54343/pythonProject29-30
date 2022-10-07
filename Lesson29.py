


# class Mobile:
#     color = 'red'
#     ram = 4
#     storage = 32
#     model = 'Alcatel'
#
#     def show_color(self, new_color):
#         self.color = new_color
#
#     def change_ram(self, new_ram):
#         self.ram = new_ram
#
#     def change_storage(self, new_storage):
#         self.storage = new_storage
#
# a7 = Mobile()
# print(a7.ram)


# class Mobile:
#     __color = 'Black'
#     imei = 123112313
#     model = 'IPhone X'
#     cpu = 'Avalanche'
#     def change_color(self, new_color):
#         self.color = new_color
#     def change_imei(self,new_imei):
#         self.imei = new_imei
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self,new_color):
#         if new_color in ['Black', 'White', 'Pinc']:
#             self.__color = new_color
#
#     @color.deleter
#     def color(self,):
#         self.__color = 'metal'
#
# iphone14 = Mobile()
# print(iphone14.color)
# iphone14.color = 'Green'
# print(iphone14.color)
# iphone14.color = 'White'
# print(iphone14.color)
# del iphone14.color
# print(iphone14.color)


# class Itstep:
#     __url = 'mystat.itstep.org/ru/main/dashboard/page/index'
#
#     def show_http(self, new_http):
#         self.url = new_http
#
#     @property
#     def color(self):
#         return self.url
#
#
#     @__url.setter
#     def color(self, new_url):
#         if new_url in ['https://', 'http']:
#             self.url = new_url
#
# step = Itstep()
#
# print(step.url)
# step.url = 'https://'
# print(step.color)
# step.url = 'http'
# print(step.url)


class Site:
    __url = 'mystat.itstep.org'
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        protocol = 'http://'
        if 'http' not in new_url:
            self.__url = protocol + new_url


roadmap = Site()
roadmap.url = 'mystat.itstep.org'
print(roadmap.url)