def filter_even_numbers(ints):
    #return [i for i in ints if i%2 == 0]
    lista = []
    for i in ints:
        if i%2 == 0:
            lista.append(i)
    return lista

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {list}")
print(f"List with even numbers only: {filter_even_numbers(list)}")