def selection_sort(items, descending):
    for i in range (0, len(items) - 1):
        for j in range(i+1, len(items)):
            if(not descending):
                if items[i] > items[j]:
                    items[i], items[j] = items[j], items[i]
            else:
                if items[i] < items[j]:
                    items[i], items[j] = items[j], items[i]
           
    return items

def nested_selecion_sort(items, descending):

    def test_and_swap(first_index, second_index):
        if(not descending):
            if(items[first_index] > items[second_index]):
                items[first_index], items[second_index] = items[second_index], items[first_index]
        else:
            if(items[first_index] < items[second_index]):
                items[first_index], items[second_index] = items[second_index], items[first_index]

    for i in range(0, len(items) -1 ):
        for j in range(i + 1, len(items)):
            test_and_swap(i, j)
    return items

def recursive_selection_sort(items,descending, first_index = 0 ):
    if first_index < len(items) - 1:
        for second_index in range(first_index + 1, len(items)):

            if(not descending):
                if(items[first_index] > items[second_index]):
                    items[first_index], items[second_index] = items[second_index], items[first_index]
            else:
                if(items[first_index] < items[second_index]):
                    items[first_index], items[second_index] = items[second_index], items[first_index]

        recursive_selection_sort(items, descending, first_index + 1)
    return items
                    

print(selection_sort([3, 2, 1, 4], False))
print(selection_sort([5, -1, 8, -3, 0], True))

print(nested_selecion_sort([3, 2, 1, 4], False))
print(nested_selecion_sort([5, -1, 8, -3, 0], True))


print(recursive_selection_sort([3, 2, 1, 4], False))
print(recursive_selection_sort([5, -1, 8, -3, 0],True))