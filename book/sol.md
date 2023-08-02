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
