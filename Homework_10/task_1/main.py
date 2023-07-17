from factory import FactoryAnimal, FactoryClassAnimal
from bird import Birds
from fish import Fish
from pets import Pets

bird = Birds(True, 'Hawk', 4)
# print(bird.get_age())
# print(bird.get_wings())
# print(bird.get_name())
# print()
cat = Pets('Musy', 'Maine coon', 35)
# print(cat.get_age())
# print(cat.get_nickname())
# print(cat.get_name())
# print()
fish = Fish(True, 'Sudak', 10)
# print(fish.get_age())
# print(fish.get_fins())
# print(fish.get_name())

# Возвращаем информацию о зверушках попавшках
# попавших на фабрику miratorg
miratorg = FactoryAnimal()
print(miratorg.get_animal_info(bird))
print(miratorg.get_animal_info(cat))
print(miratorg.get_animal_info(fish))

print('---')

# Внутри класса создаём экземпляр на основе переданного типа
# и возвращаем его из класса-фабрики
factory_bird = FactoryClassAnimal(Birds)
migratory_bird = factory_bird.get_new_animal(True, 'Crane', 10)
print(type(migratory_bird))
print(migratory_bird.__str__())

factory_pets = FactoryClassAnimal(Pets)
dog = factory_pets.get_new_animal('Ball', 'Dog', 17)
print(type(dog))
print(dog.__str__())

factory_fish = FactoryClassAnimal(Fish)
red_fish = factory_fish.get_new_animal(True, 'Salmon', 4)
print(type(red_fish))
print(red_fish.__str__())
