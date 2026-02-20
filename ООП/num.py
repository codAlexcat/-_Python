def func(num, a, list):
    if num == 0:
        print(list)
        return
    for i in range(min(num, a), 0, -1):
        func(num - i, i, list + [i])

func(6, 6, [])
