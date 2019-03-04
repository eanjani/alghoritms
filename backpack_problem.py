from collections import OrderedDict

items= {} #(weight, value)
items["iphone"] = (1, 2000)
items["gitarre"] = (2, 1000)
items["laptop"] = (3, 3000)
items["stereo"] = (1, 2500)

backpack_capacity = 4


taken_items = {}
items_sorted = OrderedDict(sorted(items.items()))

for weight in range(1,backpack_capacity+1):
    total_weight = 0
    print("max weight: ", weight)
    taken_items[weight] = []
    selected_items = set(items.keys()) - set(taken_items[weight])
    for item in selected_items:
            print("checking ", item)
            if items[item][0] <= weight - total_weight:
                taken_items[weight].append(item)
                total_weight += items[item][0]
    print(taken_items)
