def fib_loop(n):
    result = [1,1]

    for i in range(1,n):
        end1 = result[-1]
        end2 = result[-2]
        fib_num = end1 + end2

        result.append(fib_num)

    return result

print(fib_loop(7))


