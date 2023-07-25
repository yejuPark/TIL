 # git 

 버전 관리란?
 “버전 관리” 는 무엇이고 우리는 왜 이것을 알아야 할까? 버전 관리 시스템은 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템이다. 이 책에서는 버전 관리하는 예제로 소프트웨어 소스 코드만 보여주지만, 실제로 거의 모든 컴퓨터 파일의 버전을 관리할 수 있다.


## 중앙 집중식 버전 관리 (CVCS)
![DVCS](./assets/centralized.png)


## 분산 버전 관리 시스템 (DVCS)
 ![DVCS](./assets/distributed.png)



## 세가지 상태
 ![DVCS](./assets/areas.png)
- Committed란 데이터가 로컬 데이터베이스에 안전하게 저장됐다는 것을 의미한다.
- Modified는 수정한 파일을 아직 로컬 데이터베이스에 커밋하지 않은 것을 말한다.
- Staged란 현재 수정한 파일을 곧 커밋할 것이라고 표시한 상태를 의미한다.

## 세가지 위치
- working directory
- staging area = index
- .git directory


## A - github - B
- A/B > github : push
- A < github : pull
- B < github : clone




 ## 명령어

 ```shell
 git init
 ```

- `.git directory`를 생성하는 명령어

```shell
git add .
```

- `workding directory`에 있는 파일, 폴더를 `staging area`에 추가
- add 하기 전엔 파일이 저장이 되었는지 확인하기

```shell
git commit -m 'message'
```

- `staging area` 에 올라간 파일들을 저장

```shell
git remote add origin <remoteurl>
```
- 원격 저장소 주소를 `origin`이라는 별명으로 저장
- 한번 연결 이후에는 push 명령어만 사용하여 업로드

```shell
git push origin main
```

- main branch를 `origin` 원격 저장소로 업로드


```shell
git clone <remote url>
```
- 원격 저장소에 있는 레포를 현재 폴더에 복제


```shell
git pull origin main
```
- 원격 저장소에 마지막 코드 상태를 다운로드


```shell
git branch
```
- branch 목록 제시

```shell
git branch -c <pyj>
```
- <pyj>의 branch 생성 (c : create)

```shell
git switch <branch name>
```
- 해당 branch 로 이동

```shell
git merge <branch name>
```
- branch를 main/master 로 병합
