list = []
dict = {}

- str 뒤집기 : `my_string[::-1]`

- 시작할때
```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    <> = map(int, input().split())
```

- `numbers = [list(map(int, input().split())) for _ in range(N)]``
```python
numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)
```

- {'':0} 모두 기입시 for 구문만
- _dict={} 정의시 for + if 구문\

- 짝수, 홀수 구할때 range(n, m, 2) 
- inx [-1] 은 맨 마지막 자리

- `list.reverse()` = `list[::-1]` = `answer.insert(0, num)`

- 문자열 제거 : `string.replace(cha,'')`

```python
counter = [0 for _ in range(10)]
counter = [0,0,0,0,0,0,0,0,0,0]
counter = [0]*10
```

- 가로 합
```python
for row in range(len(matrix)):
    temp = 0
    for col in range(len(matrix[0])):
        temp += matrix[row][col]
```

- 세로 합
```python
for col in range(len(matrix[0])):
    temp = 0
    for row in range(len(matrix)):
        temp += matrix[row][col]
```

- 대각선 \
```python
temp = 0
for i in range(len(matrix)):
    temp += matrix[i][i]
```

- 대각선 /
```python
temp = 0
for i in range(len(matrix)):
    temp += matrix[i][(len(matrix)-1)-i]
```

- 10 x 10 배열
```python
board = [[0 for _ in range(10)] for _ in range(10)]
```

- 'str'.join()
```python
result = ' '.join(map(str, temp[0:10]))
```

- Tree 구조 알고리즘
```python
nodes = lsit(map(int, input().split()))

left_node = [0] * (E+2)  # E : 간선의 개수
right_node = [0] * (E+2)

for i in range(0, E*2, 2): # 리스트 1개를 2개로   
    parent = nodes[i]
    child = nodes[i+1]

    if left_node[parent] == 0 :
        left_node[parent] = child  # 왼쪽이 비어있으면 왼쪽부터 채우기
    else:
        right_node[parent] = child
```

- if/elif => {} (programmers_옷가게할인)
```python
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rates in discount_rates.items():
        if price > discount_price:
            return int(price * discount_rates)
```

- array 에 주어진 데이터보다 크거나 작은 데이터의 갯수 구할때
```python
def solution(array, data):
    array.append(data)
    array.sort(reverse=True)
    return array.index(data)
```
```python
def solution(array, data):
    return sum(1 for a in array if a > data)
```

- sort() : 기존 리스트 변경
 / sorted() : 새로운 리스트 반환

 - n * (2**t) = n << t