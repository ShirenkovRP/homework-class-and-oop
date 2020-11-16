# Задача №1 "Ферма Дядюшки Джо"

# noinspection NonAsciiCharacters
class Animal:
    product = 0

    def __init__(self, kind, name, animal_says, weight_anim):
        self.__kind = kind
        self.name = name
        self.__animal_says = animal_says
        self.weight = weight_anim

    def set_feed(self, food):
        self.weight += food
        self.product += 1
        return self.__kind + " " + self.name + " накормлена"

    def set_product(self):
        if self.product > 0:
            self.product -= 1
            self.weight -= self.weight / 15
        else:
            print(f"{self.__kind} {self.name} животное голодное\n надо покормить")

    def get_kind(self):
        return self.__kind

    def get_name(self):
        return self.name

    def get_product(self):
        return self.product

    def get_weight(self):
        return self.weight


animal_dict = {'Серый': Animal("Гусь", "Серый", "га-га-га", 3.8),
               'Белый': Animal("Гусь", "Белый", "га-га-га", 3.8),
               'Манька': Animal("Корова", "Манька", "муууу", 720),
               'Барашек': Animal("Баран", "Барашек", "беэээ", 160),
               'Кудрявый': Animal("Баран", "Кудрявый", "беэээ", 160),
               'Ко-ко': Animal("Курица", "Ко-ко", "ко-ко- ко", 2.8),
               'Кукареку': Animal("Курица", "Кукареку", "ко-ко- ко", 2.8),
               'Рога': Animal("Коза", "Рога", "меэээээ", 170),
               'Копыта': Animal("Коза", "Копыта", "меэээ", 170),
               'Кряква': Animal("Утка", "Кряква", "кря-кря-кря", 3.1)}


def main():
    print("Вы приехали помогать на ферму Дядюшки Джо")
    chose = 0
    while chose != 5:
        chose = get_chose()
        # добавить животное
        if chose == 1:
            print("Добавте животных которые живут на ферме")
            add_animal(animal_dict)

        # покормить животное
        if chose == 2:
            name = input("Введите имя животног \nили нажмите (all), чтобы накормить всех : ").title()
            fed_animal(animal_dict, name)
            
        # получить продукт
        if chose == 3:
            get_product(animal_dict)

        # узнать вес всех животных и  какое животное самое тяжелое
        if chose == 4:
            weight(animal_dict)

        # выход


def get_chose():
    print("""
            1 - добавить животное
            2 - покормить животное
            3 - получить продукт
            4 - узнать вес всех животных
                и  какое животное самое тяжелое
            5 - выход""")
    chose = int(input("Введите номер меню: "))
    if chose < 0 or chose > 5:
        print("Такого пункта нет в меню")
    return chose


def add_animal(arg):
    chose = input("Введите имя животног \nили нажмите (нет) для выхода: ").title()
    while chose != "Нет":
        
        if chose not in arg:
            kind = input("Введите вид животног: ").title()
            animal_says = input("Что говорит животное?: ").title()
            weight_anim = float(input("Введите вес животног в кг: "))

            animals = Animal(kind, chose, animal_says, weight_anim)
            arg[chose] = animals
        else:
            print("Животное с таким именем существует")
            print("Попробуйте другое имя")
        chose = input("Введите имя животног \nили нажмите (нет) для выхода: ").title()
            
    
def fed_animal(arg, arg_2="All"):
    if arg_2 in arg:
        food = float(input("Сколько еды вы хотите дать в кг: "))
        arg[arg_2].set_feed(food)
    elif arg_2 == "All":
        for i in arg:
            food = arg[i].get_weight() / 10
            arg[i].set_feed(food)
    else:
        print("Животного с таким именем нет")


def get_product(arg):
    print("Что вы хотте сделать")
    print("""
            1 - подоить корору и коз
            2 - собрать яйца
            3 - постричь овец
            4 - выход""")
    chose = int(input("Ваш выбор: "))
    while chose != 4:
        
        if chose == 1:
            for i in arg:
                if arg[i].get_kind() == "Корова" or arg[i].get_kind() == "Коза":
                    arg[i].set_product()
                
        elif chose == 2:
            for i in arg:
                if arg[i].get_kind() == "Гусь" or arg[i].get_kind() == "Утка" or arg[i].get_kind() == "Курица":
                    arg[i].set_product()
                
        elif chose == 3:
            for i in arg:
                if arg[i].get_kind() == "Овца" or arg[i].get_kind() == "Баран":
                    arg[i].set_product()
                    
        else:
            print("Такого пункта нет в меню")
        chose = int(input("Ваш выбор: "))
    

def weight(agr):
    kind = 0
    name = 0
    total = 0
    cost_max = 0
    for i in agr:
        total += agr[i].get_weight()
        if cost_max < agr[i].get_weight():
            cost_max = agr[i].get_weight()
            name = agr[i].get_name()
            kind = agr[i].get_kind()
    print(f"Общий вес всех животных {total:.2f} кг ")
    print(f"Самое тяжелое животное")
    print(f"{kind} {name} весом {cost_max} кг ")
    

main()        
