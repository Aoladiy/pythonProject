import math

t = 'ячейка_лист_таблица_книга'
lst1 = sorted(set(t))
print(f'lst1 >>> {lst1}')
lst2 = [t.count(i) for i in lst1]
print(f'lst2 >>> {lst2}')
lst3 = [i / sum(lst2) for i in lst2]
print(f'lst3 >>> {lst3}')
lst4 = [abs(i * math.log(i)) for i in lst3]
print(f'lst4 >>> {lst4}')
entropy = sum(lst4)
print(f'entropy >>> {entropy}')
print()


def get_depth(list_):
    return 1 + max(get_depth(itm) for itm in list_) if type(list_) == list else 0


def divider(lst):
    lst = sorted(lst)
    check = []
    check1 = []
    for i in range(len(lst)):
        first = sum(lst[:i])
        # print(f'first {first}')
        second = sum(lst[i:])
        # print(f'second {second}')
        # print()
        check.append((first, second, i))
    for i in range(len(check)):
        check1.append(abs(check[i][0] - check[i][1]))
    # print(lst)
    # print(check)
    # print(check1)
    # print(min(check1))
    # print(check1.index(min(check1)))
    # print(check[check1.index(min(check1))])
    # print(lst[:11])
    return lst[:check1.index(min(check1))], lst[check1.index(min(check1)):]


def shennon_fano(lst, result=[]):
    # result = [[] for i in range(len(lst))]
    




print(shennon_fano(lst3))