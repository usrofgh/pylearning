# In python all properties which I declare will be rewrite to descriptor - it's an any class which has at least one
# redefined method - get/set/delete magics
# https://prnt.sc/cg_ng6uo_dAm - example from zoom
# Any object that has __get__ , __set__ , or __delete__
# Descriptor only with __get__  - non-data descriptor. With __set__ and/or __delete__  - data descriptor


# self is the instance of the descriptor
# @classmethod, @staticmethod,   @property - descriptors
# descriptors instantiated once per class, so every instance containing a descriptor shares that instance

# any property we can change to descriptor but not backward

class Two:
    def __get__(self, instance, owner):
        print("get called")
        return 2


class Example:
    x = 5
    y = Two()


ex = Example()
print(ex.x)  # 5
print(ex.y)  # 2. here I call __get__, print info and return 2 to y


# -----------------------------------------------------------------------

class ArraySize:  # descriptor class
    def __get__(self, instance, owner):  # instance - array_obj. owner - class Array
        return len(instance.arr)


class Array:
    size = ArraySize()

    def __init__(self, arr: list):
        self.arr = arr


array_obj = Array([1, 2, 3])
print(array_obj.size)  # 3
array_obj.arr.append(1)
print(array_obj.size)  # 4


# with help property:
class Array1:
    def __init__(self, arr: list):
        self.arr = arr

    # @property size() works under hood like above
    @property
    def size(self):
        return len(self.arr)


ar = Array1([1, 2, 3])
print(ar.size)  # 3


# -----------------------------------------------------------------------


class Temperature:
    def __get__(self, instance, owner):
        print("get temperature")
        return instance._temperature

    def __set__(self, instance, value):
        print("set temperature")
        if not (0 <= value <= 100):
            print("Temperature must be in range 0..100!")
            return
        instance._temperature = value


class GlassOfWater:
    temperature = Temperature()  # access through this var, a real value I get and write with help __get__, __set__

    def __init__(self, temperature: int):
        self.temperature = temperature

    def heat(self):
        self.temperature += 1


glass = GlassOfWater(98)
print(glass.temperature)  # 98
glass.heat()
print(glass.temperature)  # 99
print('\n')  # 99
# -----------------------------------------------------------------------
# advanced


class Temperature1:
    def __init__(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def __get__(self, instance, owner):
        print("get temperature")
        return instance._temperature

    def __set__(self, instance, value):
        print("set temperature")
        if not (self.min_temp <= value <= self.max_temp):
            print(f"Temperature must be in range {self.min_temp}..{self.max_temp}!")
            return
        instance._temperature = value


class GlassOfWater1:
    temperature = Temperature1(10, 30)
    air_temperature = Temperature1(10, 100)

    def __init__(self, temperature: int, air_temperature=0):
        self.temperature = temperature
        self.air_temperature = air_temperature

    def heat(self):
        self.temperature += 1

    def air_heat(self):
        self.air_temperature += 1


glass = GlassOfWater1(29, 20)
print(glass.__dict__)  # {'_temperature': 29}
print(GlassOfWater1.__dict__["temperature"])  # <__main__.Temperature1 object at 0x0000023F2B75A470>
print(GlassOfWater1.__dict__["temperature"].__dict__)  # {'min_temp': 10, 'max_temp': 30}
glass.heat()
print(glass.temperature)  # 30
glass.heat()  # Temperature must be in range 10..30!

print(glass.__dict__)  # {'_temperature': 22} - why 22 if i need 29 and 20