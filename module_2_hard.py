def password(n):
    pass_ = []
    pass_set = []
    result = ""
    for i in range(1, n):
        for j in range(2, n):
            if n % (i + j) == 0 and i != j:
                if [j, i] not in pass_:
                    pass_.append([i, j])
    for i in pass_:
        pass_set += i
    for i in pass_set:
        result += f"{i}"

    return result

n = int(input("Введите число от 3 до 20: "))
print(password(n))
