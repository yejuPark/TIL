#  HTML
<태그이름>내용</태그이름>
[W3school](https://www.w3schools.com/)
<br>
[mdn](https://developer.mozilla.org/ko/)
<hr/>

#### 풀스택 프로그래밍
- Web - World Wide Web의 줄임말

- HTML : Hyper Text / Markup / Language

- CSS(Cascading Style Sheet) : 사람이 보기 좋게 만드는 스타일 언어

- HTTP : HTML 을 주고받는 프로토콜 (요청<—>응답)

- get : client가 server에게 ‘—주세요’ 요청 (server가 정보 제공)

- Post : client가 server에게 ‘—해주세요’ 요청 (client가 정보 제공)

- Client : 웹 브라우저 (크롬, 사파리, 엣지, 파이어폭스….)
<hr/>
<hr/>


### ! tap키
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```
## head
: 문서 정보들을 담는 공간

## body
* 브라우저 화면에 나타나는 정보들을 담는 공간

* `<태그이름 속성명="속성값" 속성명2="속성값2">내용</태그이름>`

```html
<form action="">
    <label for=""></label>
    <input type="text" id="" name="">

    <input type="" name="" id="" value="">
    <label for=""></label>

    <input type="submit" value="확인">
</form>
```
Name-value / id-for 

<hr/>
<hr/>

# CSS
### 적용방법 3가지 
- 인라인
```html
<h1 style="color: red;">hello</h1>
```
- 내부 스타일 시트
```html
<head>
    <style>
        선택자 {
            속성명: 속성값;
            속성명2: 속성값2;
        }
    </style>
</head>
```
- 외부 스타일 시트
```html
<head>
    <link rel="stylesheet" href="./style.css">
</head>
```

### 외부 스타일 시트
- style.css
- `#id {}`
- `.class {}`


### layout
- justify-content
    * flex-start: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
    * flex-end: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
    * center: 요소들을 컨테이너의 가운데로 정렬합니다.
    * space-between: 요소들 사이에 동일한 간격을 둡니다.
    * space-around: 요소들 주위에 동일한 간격을 둡니다

- align-items
    * flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
    * flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
    * center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
    * baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
    * stretch: 요소들을 컨테이너에 맞도록 늘립니다.

- align-content
    * flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
    * flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
    * center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
    * space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
    * space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
    * stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.


- flex-direction
    * row: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
    * row-reverse: 요소들을 텍스트의 반대 방향으로 정렬합니다.
    * column: 요소들을 위에서 아래로 정렬합니다.
    * column-reverse: 요소들을 아래에서 위로 정렬합니다.

- flex-wrap
    * nowrap: 모든 요소들을 한 줄에 정렬합니다.
    * wrap: 요소들을 여러 줄에 걸쳐 정렬합니다.
    * wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

- flex-flow: flex-direction flex-wrap
