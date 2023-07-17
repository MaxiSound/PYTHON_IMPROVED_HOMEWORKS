# - Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа
# - Верните его из класса-фабрики.


# Класс "фабрика" возвращающий информацию о животных
class FactoryAnimal:
    # метод возвращающий информацию о переданном в него объекте
    def get_animal_info(self, animal):
        return animal.__str__()


# Класс фабрика, возвращающий объект переданого имени класса
class FactoryClassAnimal:
    def __init__(self, name_class_animal):
        self.name_class_animal = name_class_animal

    # Метод возвращающий объект переданного класса
    def get_new_animal(self, *args):
        return self.name_class_animal(*args)
