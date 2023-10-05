def fac(n):
    factorial = n
    for i in range(2, n):
        factorial *= i
    result = []
    for i in range(factorial, 0, -1):
        factorial_i = i
        for j in range(2, factorial_i):
            factorial_i *= j
        result.append(factorial_i)
    return result

input_number = int(input("Введите натуральное целое число: "))
result_list = fac(input_number)
print(result_list)