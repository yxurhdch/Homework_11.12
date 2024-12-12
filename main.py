def parse_cook_book(file_path):

    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while line := file.readline().strip():
            dish_name = line
            num_ingredients = int(file.readline().strip())
            ingredients = []
            for _ in range(num_ingredients):
                ingredient_data = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропустить пустую строку

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):

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


file_path = 'recipes.txt'
cook_book = parse_cook_book(file_path)
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes, person_count)
print(result)
