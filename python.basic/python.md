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
### 자료구조
# 시퀀스 자료형
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


# 시퀀스가 아닌 자료형
1. `{Set}` : mutable
- 수학 집합과 동일하게 처리 (중복 값 없음)
2. `{Dict: ionary}` : mutable
```
변수이름 = {key1: value1, key2: value2, ...}
```
- 접근 : `변수이름[key]`
- key (immutable한 모든 것_불변값:str,integer...) 와 value (모든 데이터_list, dict도 가능) 의 쌍으로 이루어짐

---

# 제어문

## 조건문 (if)
: `if` 문은 반드시 참/거짓을 명시할 수 있는 `조건식`과 함께 사용
```
if <조건식>:
```
- 조건식이 `참`인 경우 실행
```
else:
```
- 조건식이 `거짓`인 경우 실행

```
elif <조건식>:
```
- elif 조건이 `참`인 경우 실행

#### 조건표현식
```
true_value if <조건식> else false_value
```

