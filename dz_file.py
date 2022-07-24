cook_book = {}
with open('text.txt', encoding='utf-8') as file:
    for dish in file:
        dishes = dish.strip()
        ingredi = int(file.readline())
        dishes_list = []
        for ing in range(ingredi):
            ingredient_name, quantity, measure = file.readline().split("|")
            dishes_list.append({"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure})
            cook_book[dishes] = dishes_list
        file.readline()
    # print(cook_book)
di_list = {}
def get_shop_list_by_dishes(dishes, person_count):

    for dish in dishes:
        for item in cook_book[dish]:
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity' : int(item['quantity']) * person_count})])
            if di_list.get(item['ingredient_name']):
                extra_item = (int(di_list[item['ingredient_name']]['quantity']) + int(items_list[item['ingredient_name']]['quantity']))
                di_list[item['ingredient_name']]['quantity'] = extra_item
            else:
                di_list.update(items_list)
    print(di_list)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)
