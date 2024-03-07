import json
import os 


# Функция для вывода меню
def print_menu():
    # Выводим текст меню
    text_menu = """ 
    1 - показать все рецепты
    2 - отсортировать рецепты
    3 - выбрать пропорции
    4 - уйти"""
    
    print(text_menu)
    user_answer = input("выберите цифру.")
    
    if user_answer == "1":
        # Выводим все рецепты
        for recipe in recipes:
            print_recipe(recipe)
            
    elif user_answer == "2":
        # Сортируем рецепты по игредиентам
        user_included_indredients = input("введите желаемый игредиент:").split(", ")
        user_excluded_ingredients = input("введите нежелаемый игредиент:").split(", ")
        
        print(get_recipe(user_included_indredients, user_excluded_ingredients))
        
    # elif user_answer == "3":
    #!
    else:
        print("до свидания!")
        
        
# Функция для вывода рецепта
def print_recipe(recipe, separator="-"):
    print(separator * 50)
    print(
        f"время приготовления - {recipe['time']}, количество ингредиентов {recipe['number_of_ingredients']},"
    )

    proportions = recipe["proportions"]

    print("пропорции - ")

    # Перебираем название и количество пропорции
    for name, number in proportions.items():
        print(f"{name} - {number}")

    print(
        f"оборудование - {recipe['equipment']}, описание - {recipe['description_of_the_dish']} "
    )

    print(f"название - {recipe['name_of_the_dish']}  рецет! {recipe['cooking_method']}")
    
    
# Функция для получения списка рецептов, удовлетворяющих заданным игредиентам
def get_recipe(included_ingredients, excluded_ingredients):
    # Создаем необходимые списки
    in_recipe = []
    excluded_recipes = []
    
    # Перебираем все рецепты
    for recipe in recipes:
        ingredients = recipe["ingredients"]
        # Перебираем ингредиенты на наличие нежелаемых
        for ingredient in excluded_ingredients:
            # Проверяем рецепт на наличие нежелаемого инргедиента  
            if ingredient in ingredients:
                excluded_recipes.append(recipe)
                break

    # Перебираем все рецепты
    for recipe in recipes:
        ingredients = recipe["ingredients"]
        # Перебираем ингредиенты на наличие желаемых
        for ingredient in included_ingredients:
            # Проверяем рецепт на наличие желаемого инргедиента
            if ingredient not in ingredients:
                break
        else:
            # Проверяем наличие нежелаемого ингредиента
            if recipe not in excluded_recipes:
                in_recipe.append(recipe)

    return in_recipe


def convert_proportions(proportions, number_of_servings=1):
    for i, k in proportions.items():
        for j, m in k.items():
            print(j, m)


recipes = [
    {
        "time": "5 минут",
        "number_of_ingredients": 3,
        "ingredients": ["банан", "какао", "разрыхритель теста", "яйцо", "сахар"],
        "proportions": {
            "банан": "1 штука",
            "какао": "3 ложки",
            "разрыхритель теста": "1 чайная ложка",
            "яйцо": "1 штука",
            "сахар": "1 ч. ложка",
        },
        "equipment": "микроволновая печь, керамическая глубокая тарелка, вилка",
        "description_of_the_dish": "Простая и быстрая сладость, которая поднимает вам настроение - шоколадное пироженое с бананом!",
        "name_of_the_dish": "Шоколадно-банановое пироженое",
        "cooking_method": "Подготовьте необходимые ингредиенты и оборудование. Разбейте яйцо в тарелку, добавьте какао и перемешайте до однородности, добавьте разрыхритель теста и поставьте в микроволновку на 3 минуты!",
    },
    {
        "time": "10 минут",
        "number_of_ingredients": 5,
        "ingredients": ["мука", "сахар", "яйцо", "масло", "ванильный сахар"],
        "proportions": {
            "мука": "2 стакана",
            "сахар": "1 стакан",
            "яйцо": "2 штуки",
            "ванильный сахар": "1 чайная ложка",
            "масло": "100 г",
        },
        "equipment": "миска, венчик, форма для выпечки",
        "description_of_the_dish": "Вкусные домашние кексы с ванильным ароматом и нежным тестом.",
        "name_of_the_dish": "Ванильные кексы",
        "cooking_method": "Смешайте муку, сахар, ванильный сахар. Добавьте яйцо и масло. Тщательно перемешайте. Выложите тесто в форму и выпекайте в предварительно разогретой духовке при 180 градусах в течение 20 минут.",
    },
    {
        "time": "15 минут",
        "number_of_ingredients": 4,
        "ingredients": ["курица", "картошка", "лук", "соль"],
        "proportions": {
            "курица": "500 г",
            "картошка": "4 штуки",
            "лук": "1 штука",
            "соль": "по вкусу",
        },
        "equipment": "сковорода, нож, тарелка",
        "description_of_the_dish": "Простое и сытное блюдо из куриного филе с картошкой и луком.",
        "name_of_the_dish": "Курица с картошкой",
        "cooking_method": "Нарежьте курицу, картошку и лук. Обжаривайте курицу в сковороде до золотистой корки, затем добавьте картошку и лук. Тушите под крышкой на среднем огне до готовности. Приправьте солью по вкусу.",
    },
]


def create_json_recipes():
    with open("recipes.json", "w", encoding="utf-8") as outfile:
        json.dump(recipes, outfile, ensure_ascii=False, indent=4)
    
print(os.path.exists("recipes.json"))

if os.path.exists("recipes.json"):
    print("Здесь уже есть рецепты")
else:
    create_json_recipes()




print_menu()



