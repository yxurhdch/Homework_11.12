def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция принимает список блюд и количество персон,
    возвращает словарь с суммарным количеством ингредиентов.
    """
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ],
        'Фахитос': [
            {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
            {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
        ]
    }

    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов.")

    return shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes, person_count)
print(result)
