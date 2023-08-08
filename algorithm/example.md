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

# Stack


### DP (memoization)
- 피보나치 수열
```python
memo = [0,1]

def fibo(n):
    if n>=2 and len(memo)<=n:
        memo.append(fibo(n-1) + fibo(n-2))
        return memo[n]
```
### DFS
- 인접 행렬 (2차원 표)
```python
nodes = [[0]*(V+1) for _ in range(V+1)]

for line in range(E):
    nodes[start][end] = 1


check_list = [False] * (V+1)
stack = []

now = S
stack.append(now)

result = 0

while len(stack):
    now = stack.pop()
    check_list[now] = True

    for link in range(V+1):
        if nodes[now][link] == 1:
            if not check_list[link]:
                if link == G:
                    result = 1

                stack.append(link)
```

- 인접 리스트
```python
nodes = [[] for _ in range(V+1)]

for line in range(E):
    nodes[start].append(end)

check_list = [False]*(V+1)
stack = []

now = S
stack.append(now)
result = 0

while len(stack):
    now = stack.pop
    check_lsit[now] = True

    for link in nodes[now]:
        if not check_list[link]:
            if link == G:
                result = 1

            stack.append(link)
    
```

### 백트래킹
- 모든 경우의 수 탐색 (step 1)
```python
def def_name(row):
    if row >= N:
        print(result)
        return

    for col in range(N):
        result.append(numbers[row][col])
        def_name(row+1)

        result.pop()
```
- (step 2)
```python
def def_name(row, visited):
    if row >= N:
        print(result)
        return

    for col in range(N):
        if visited[col] == False:
            result.append(numbers[row][col])
            visited[col] = True
            def_name(row+1, visited)

            result.pop()
            visited[col] = False
```
- (sol)
```python
def def_name(row, visited, SUM):
    global MIN_SUM
    
    if row >= N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return

    if SUM > MIN_SUM:
        return

    for col in range(N):
        if visited[col] == False:
            SUM += numbers[row][col]
            visited[col] = True
            def_name(row+1, visited, SUM)

            SUM -= numbers[row][col]
            visited[col] = False
```

