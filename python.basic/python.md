# Intro
## 단축키
- ctrl + enter : 현재 셀 실행
- shift + enter : 현재 셀 실행 후 아래로 이동


# 변수
### 변수이름 = 값
- 영어, 숫자, _ 이용해 선언
- keyword는 사용 불가능 
```shell
import keyword
keyword.kwlist
```
---

# 연산자
### 산술
- `+, -, *, /, **`
- `//` : 몫 출력
- `%` : 나머지 출력
- `divmod()` : 몫, 나머지 한번에 출력

### 비교
- `>, <, >=, <=`
- `== , !=`


### 논리
- `and` : 양쪽 모두 True 일때, True 
- `or` : 양쪽 모두 False 일때, False
- `not` : 값을 반대로 전환


### 기타
- concatenation (연결) : 합집합 , 문자열로 연결 가능
- containment `in` : 문자열에 원하는 문자가 있는지 , list에 원하는 데이터가 있는지 알려줌
- identity `is` : ==과 비슷하게 동작하지만 값이 아닌 메모리 주소 

#### 우선순위 : `()` > `**` > `*,/` > `+,-` > `in, is` > `not` > `and` > `or`


#### 단축평가 
- and : 선 데이터가 True면 후 데이터 값 제시 / 선 데이터가 F면 F 값 제시

- or : 선 데이터가 T면 선 데이터 값 제시 / 선 데이터가 F면 후 데이터 값 제시

- and는 T면 지나가고 or는 F면 멈춤

# 형변환

### 암시적
- 0 : `False`
- 1 이상 모두 `True`

### 명시적
- `int()` : string, float > int 
- `float()` : string, int > float 
- `str()` : int, float 등 > string 
- `bool()` : int, list 등 > boolean 

# 데이터 타입
## 1. Number
- `int` : 정수
- `float` : 소수/실수
- `complex` : 허수가 있는 복소수
(imag: 허수 , real: 실수)


## 2. Boolean 
- True / False

## 3. String : 문자열
- \ : escape
- \n : new line
- \t : tap
- end
- sep
- interpolation (f-string)

---
# 자료구조
## 시퀀스 자료형
 : 데이터의 순서대로 나열된 자료구조. (`순서대로` 와 `정렬된 것`은 다름)
1. `[list]` : mutable
2. `(Tuple)` : immutable
3. range() : immutable
- `range(n)` : 0 ~ (n-1)
- `range(n,m)` : n ~ (m-1)
- `range(n,m,s)` : n ~ (m-1) 까지 +s 만큼 증가
4. `'String'` : immutable

#### 시퀀스에서 활용가능한 연산/함수
- indexing `[int]` : 내가 원하는 값 하나에 접근
- slicing 
```
[int : int'] : 범위 출력 (두번째 숫자 미만)
[int : int : int] : 위와 동일 + 세번째 숫자 간격으로 
```
- `in` keyword
- `concatenation`
- `*`
- `len` : length
    `min` : minimum
    `max` : maximum
    `count` : 몇 번 나오는지


## 시퀀스가 아닌 자료형
1. `{Set}` : mutable
- 수학 집합과 동일하게 처리 (중복 값 없음)
2. `{Dict: ionary}` : mutable
```python
변수이름 = {key1: value1, key2: value2, ...}
```
- 접근 : `변수이름[key]`
- key (immutable한 모든 것_불변값:str,integer...) 와 value (모든 데이터_list, dict도 가능) 의 쌍으로 이루어짐

---

# 제어문

## 조건문 (if)
: `if` 문은 반드시 참/거짓을 명시할 수 있는 `조건식`과 함께 사용
```python
if <조건식>:
```
- 조건식이 `참`인 경우 실행
```python
else:
```
- 조건식이 `거짓`인 경우 실행

```python
elif <조건식>:
```
- elif 조건이 `참`인 경우 실행

#### 조건표현식
```python
true_value if <조건식> else false_value
```

---
# 반복문

### while 문
```python
while <조건식>:
    실행 코드
```

### for 문
```python
for variable in sequence:
    code
```

### dictionary 반복
```python
for key in dict:
```
```python
for key in dict.keys():
```
```python
for value in dict.values():
```
```python
for key, value in dict.items():
```

### break
- 반복문 종료

 ### continue
 - continue 이후의 코드를 실행하지 않고 다음 반복을 진행

 ### else
 - 끝까지 반복이 진행된 후 실행

 ### pass
 - class, 함수 구조 먼저 잡을때 임의로 사용

 ### match
 ```python
 match value:
    case 조건:
        code
    case 조건:
        code
    case _:
        code
 ```


---
 # 함수 (function)

 ### 선언 및 호출
 - 함수 선언
 ```python
 def func_name(parameter1, parameter2...):
    code1
    code2
    ...
    return value
 ```

 - 함수 호출(실행)
 ```python
 func_name(parameter1, parameter2)
 ```

 ### return
 - 함수가 return 을 만나면 해당 값을 반환하고 함수를 종료
 - 만약 return 이 없다면 None 을 자동으로 반환
 - return 은 오직 하나의 객체만 반환


 ## 함수의 인수

- 위치 인수
- 기본값 : `func(p1=v1)``
- 키워드 인자 : 함수 호출(실행)시, 내가 원하는 위치에 직접 특정인자 전달 가능
- 가변인자 리스트 : `func(*params)`
- 정의되지 않은 인자 처리 : `func(**kwargs)`
- dictionary를 인자로 넣기 (unpacking) : `func(p1, p2, p3...)`


#### lambda 표현식
```python
(lambda a, b: a + b) (num1, num2)
```
- lambda parameter: expression

#### 타입 힌트
- 주석 달기

#### 이름 공간 (scope)
 : 파이썬에서 사용되는 이름들 저장
- Local scope : 정의된 함수 내부
- Enclosed scope : 상위 함수
- Global scope : 함수 밖의 변수 혹은 import 된 모듈
- Built-in scope : 파이썬 기본 함수 혹수 변수


## 재귀 (recursive)
: 함수 내부에서 자기 자신을 호출
- 팩토리얼
- 피보나치 수열

# method

## 문자열
- `.capitalize()`
- `.title()`
- `.upper()`
- `.lower()`
- `''.join(iterable)`
- `.replace(old, new[, count])`
- `.strip([chars])`
- `.find(x)`
- `.index(x)`
- `.split(x)`
- `.count(x)`

## List
- `.append(x)`
- `.extend(iterable)`
- `.insert(idx,x)`
- `.remove(x)`
- `.pop([idx])`
- `.sort()` 
: `.sort(reverse=True)`는 역순
- `.reverse()`

### list copy
: origin_list = copy_list 후 copy_list[idx] 변경하면 origin_list 도 바뀜
```python
import copy
a = []
b = copy.deepcopy(a)
```

### list comprehension
: for, if 문 한줄로 만들기
```python
even_list = [i for i in numbers if i % 2 == 0]
```

## dictionary
- `.pop(key[, default])`
- `.update(key=value)`
- `.get(key[, default])`

### dict comprehension
```python
result = {k: v for k, v in dust.items() if v >= 50}
```


## Set
- `.add('x')`
- `.update()`
- `.remove()`
- `.pop()`


## map(), zip(), filter()
### map
```python
map(funtion, iterable)
```

### zip
```python
zip([a],[b])
```

### filter
```python
filter(function, iterable)
```
: filter 에 들어가는 function은 T/F를 반환해야 함


# module
```python
import 파일명
```

# Package
```python
myPackage/
    __init__.py
    math/
        __init__.py
        fibo.py
        formula.py
```
: 패키지 안에 `__init__.py` 파일이 있어야 패키지로 인식

- 패키지 폴더 전체 추가
```python
import myPackage
```

- 패키지에서 필요한 모듈 꺼내오기
```python
from myPackage.math import formula
```

- 경로에 있는 모듈 내 모든 변수, 함수 추가
```python
from myPackage.math.fibo import *
```


# Python 내장 패키지

## `math.`
- math.pi
- math.e
- math.ceil() : 소수점 올림
- math.floor() : 소수점 내림
- math.sqrt() : 루트
## `random.`
- random.randint(n1,n2)
- random.seed()
- random.shuffle()
- random.choice()
- random.sample(n1,n2)

## `datatime.`
```python
from datetime import datetime
```
- datetime.now()
- datetime.today()
- datetime.utcnow()
- now.strftime('%Y/%m/%d')
- now.weekday() : weekday => 0~6, 월~일
```python
from datetime improt timedelta
```
- 날짜 더하고 빼기 


