# List
## 1차원
```python
numbers = input().split()

for number in numbers:
    int_num = int(number)
```
```python
numbers = list(map(int, input().split()))
```

## 2차원
```python
N, M = list(map(int, input().split()))
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

# 가로
for row in range(N):
    for col in range(M):
        print(matrix[row][col])

# 세로
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])
```

## 부분집합

- 부분집합의 모든 경우의 수
```python
for i in range(1 << len(numbers)):
    temp = []
    for j in range(len(numbers)):
        if i & (1<<j):
            temp.append(numbers[j])

```





## Sort

### 버블 정렬
```python
for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)

        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

            # temp = my_list[j]
            # my_list[j] = my_list[j+1]
            # my_list[j+1] = temp
print(my_list)
```


### 카운팅 정렬
```python
counter = [0 for i in range(10)]

for i in my_list:
    counter[i] += 1

result = []

for value, count in enumerate(counter):
    for i in range(count):
        result.append(value)

print(result)
```

# String

### 회문
- for 가로, for 세로 나눠서 회문 확인
```python 
# N : 배열 크기 , M : 회문 길이
# 가로
for row in range(N):
        for col in range(N-M+1):
            row_list = []
            for r in range(M):
                row_list.append(numbers[row][col+r])
            if row_list == row_list[::-1]:
                result.append(''.join(row_list))

# 세로
for row in range(N-M+1):
        for col in range(N):
            col_list = []
            for c in range(M):
                col_list.append(numbers[row+c][col])
            if col_list == col_list[::-1]:
                result.append(''.join(col_list))
```

- for 하나에 회문 확인
```python
for row in range(N):
    for col in range(N-M+1):
        temp_row = []
        temp_col = []
        for i in range(M):
            temp_row += numbers[row][col+i]
            temp_col += numbers[col+i][row]

        if temp_row == temp_row[::-1]:
            result.append(''.join(temp_row))
        if temp_col == temp_col[::-1]:
            result.append(''.join(temp_col))
```




