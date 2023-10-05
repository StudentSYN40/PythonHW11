import collections


def id_pet(ch):
    pets_list()
    id = ent_int("Введите ID питомца: ")
    pet = get_pet(id)
    while pet == False:
        print("Питомца с таким ID нет в списке!")
        id = ent_int("Введите ID питомца: ")
        pet = get_pet(id)
    match ch:
        case "id":
            return id
        case "pet":
            return pet
        case "id,pet":
            return id, pet


def ent_int(text):
    while True:
        s = input(text) # получаем строку
        try:
            n = int(s) # пробуем перевести в число, если не удается переходим в except
            break
        except :
            print("Введите арабскими цифрами")
    return n


def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1  # Если список pets пуст, устанавливаем новый идентификатор в 1

    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = ent_int("Введите возраст питомца: ")
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        }
    }


def read():
    if pets:
        pet = id_pet("pet")
        for pet_name, pet_data in pet.items():
            pet_type = pet_data["Вид питомца"]
            age = pet_data["Возраст питомца"]
            owner_name = pet_data["Имя владельца"]
            age_suffix = get_suffix(age)
            print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner_name}')
    else:
        print("Список пуст")


def update():
    if pets:
        id, pet = id_pet("id,pet")
        for pet_name, pet_data in pet.items():
            pet_type = pet_data["Вид питомца"]
            age = pet_data["Возраст питомца"]
            owner_name = pet_data["Имя владельца"]
            age_suffix = get_suffix(age)
            print(f"1. Имя питомца: {pet_name}\n2. Вид питомца: {pet_type}"
                f"\n3. Возраст питомца: {age} {age_suffix}\n4. Имя владельца: {owner_name}"
                "\n5. Обновить всю информацию")
            info = ent_int("Какую информацию хотите обновить: ")
            while info < 1 or info > 5:
                print("Введите арабскими цифрами от 1 до 5")
                info = ent_int("Какую информацию хотите обновить: ")
            if info == 1:
                pet_name = input("Имя питомца: ")
            elif info == 2:
                pet_type = input("Вид питомца: ")
            elif info == 3:
                age = ent_int("Возраст питомца: ")
            elif info == 4:
                owner_name = input("Имя владельца: ")
            elif info == 5:
                pet_name = input("Имя питомца: ")
                pet_type = input("Вид питомца: ")
                age = ent_int("Возраст питомца: ")
                owner_name = input("Имя владельца: ")
            pets[id] = {
                pet_name: {
                    "Вид питомца": pet_type,
                    "Возраст питомца": age,
                    "Имя владельца": owner_name
                }
        }
                    
    else:
        print("Список пуст")


def delete():
    if pets:
        id = id_pet("id")
        pets.pop(id)
    else:
        print("Список пуст")

def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    age_word = "лет"
    if age % 10 == 1 and age != 11:
        age_word = "год"
    elif 2 <= age % 10 <= 4 and (age < 10 or age > 20):
        age_word = "года"
    return age_word


def pets_list():
    print("Список питомцев: ")
    for ID, pet_info in pets.items():
        for pet_name in pet_info:
            print(f'ID: {ID}, Питомец: {pet_name}')


pets = {}


# Главный цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, stop): ")
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "stop":
        print("Завершение программы")
    else:
        print("Такой команды нет!")
