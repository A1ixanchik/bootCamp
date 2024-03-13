class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100


# class Iphone:
#     def __init__(self, color):
#         self.color = color
#         self.battery = Battery()


# a = Iphone('white')
# print(a.battery._power)
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a


# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
#         #когда обьект создается из вне класса и передается внутрь - агрегация

# battery = Battery()
# nokia1 = Nokia('Gray', battery)
# nokia1.battery._power
# del nokia1

# nokia2 = Nokia('black', battery)
