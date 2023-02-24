class Candy:
    def __init__(self, taste: str):
        self.taste = taste

# Юзаем shallow с immutable значениями, тогда бы работало как deepcopy.
chocolate = Candy("Chocolate")
lemon = Candy("Lemon")

box1 = [chocolate, lemon]
box2 = box1
box2[0] = Candy("Caramel")
print(box1[0].taste)  # Caramel // так как это не копия значений, а копия ссылки


box1 = [chocolate, lemon]
box2 = box1.copy()  # shallow copy.
# #1 [#2, #3]
# #2 [#2, #3] - так работает поверхностное копирование. Ссылка на list другой(отдельная переменная), но ссылки на
# значения в листе те же
box2[0] = Candy("Caramel")  # #2 [#5, #3]
print(box1[0].taste)  # Chocolate  // не изменилось. Создали новый объект, с новой ссылкой. в box1 по прежнему #2


print(box1[1].taste)  # Lemon
box2[1].taste = "Orange"
# Было #2 [#5, #3]. Стало #2 [#5, #3(но тут меняем аттрибут]. Теперь он меняется и в box1, так как у него #1 [#2, #3]
print(box1[1].taste)  # Orange


from copy import deepcopy
chocolate = Candy("Chocolate")
lemon = Candy("Lemon")

box1 = [chocolate, lemon]
box2 = deepcopy(box1)  # копирует со всеми вложенными объектами
box2[1].taste = "Orange"
print(box2[1].taste)  # Orange
print(box1[1].taste)  # Lemon
