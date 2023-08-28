# Django

## MVC 패턴 (Model-View-Controller)
- model : database
- view : display(UI), html과 같은 인터페이스
- controller : 데이터와 인터페이스 간 다리역할, 이벤트를 처리하는 부분
### MTV 
- model
- template (view)
- view (controller)

-----------------

## 프로젝트 구조 및 CRUD 로직
[CRUD](https://github.com/yejuPark/crud)

## HTTP status code
- 200 : OK
- 30X : redirect
- 4XX : client error
    - 401 : Unauthorized
    - 403 : Forbidden
    - 404 : Not Found
- 500 : server error


    
-----------------

### Form vs ModelForm
- Form
```python
class Form(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.TextField
```
직접 field 정의, 입력폼 html 생성 => form fields는 html form field 들을 파이썬 클래스화

```python
GET : 빈 form 보여줌
POST : 입력된 값 검증 후 저장 (.is_valid())
```

- ModelForm
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'  # ('username', )
        # exclude = ('articles', )
```
form 자동 형성, 유효성 검사는 추가 적용(field 만), model fields는 database field 들을 파이썬 클래스화, (create, update)

### 1-N
- ForeignKey : 다른 테이블의 id로, N에 해당하는 모델에 입력
```python
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```