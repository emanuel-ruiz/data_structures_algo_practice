"""Write a function that finds all common items"""
#Returns all items in common
def items_in_common(list1, list2):
    comp_dict = {};
    items = [];
    for i in range(len(list1)):
        comp_dict[list1[i]] = True;

    for i in range(len(list2)):
        if list2[i] in comp_dict:
            items.append(list2[i]);
    return items;

def is_any_common(list1, list2):
    comp_dict = {};
    for i in range(len(list1)):
        comp_dict[list1[i]] = True;

    for i in range(len(list2)):
        if list2[i] in comp_dict:
            return True;
    return False;

list1 = [2, 6, 93, 856, 12];
list2 = [4,146,83,36,21,23054];

print(items_in_common(list1, list2));