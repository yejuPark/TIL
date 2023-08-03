list = []
dict = {}

- 시작할때
```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    <> = map(int, input().split())
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