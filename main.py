from pprint import pprint

k = 'files/recipes.txt'

def read_file(path_file):
    with open(path_file, 'rt', encoding='utf-8') as file:
        full_dish = {}
        for line in file:
            dish_name = line.strip()
            ingrid_count = int(file.readline().strip())
            components = []
            for i in range(ingrid_count):
                ingridient, count, unit = file.readline().strip().split(' | ')
                components.append({'ingridient': ingridient,'count': count, 'unit': unit})
            file.readline()
            full_dish[dish_name] = components
    return full_dish

cook_book = read_file(k)
pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    list_to_buy = {}
    for dish in dishes:
        for dish_item in cook_book[dish]:
            new_shop = {'measure':dish_item['unit'], 'quantity': int(dish_item['count'])*person_count}
            if dish_item['ingridient'] not in list_to_buy:
                list_to_buy[dish_item['ingridient']] = new_shop
            else:
                list_to_buy[dish_item['ingridient']]['quantity'] = int(list_to_buy[dish_item['ingridient']]['quantity']) + new_shop['quantity']
    return list_to_buy




dishes = ['Омлет', 'Фахитос']
person_count = 3

pprint(get_shop_list_by_dishes(dishes, person_count))

