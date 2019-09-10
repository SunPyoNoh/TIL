# R



> - R은 객체지향 프로그래밍 언어 - 데이터, 함수, 차트등 모든 데이터는 객체 형태로 관리
> - R은  통계 분석과 data의 시각화를 소프트웨어 환경
> - R은 데이터 분석에 필요한 최신 알고리즘, 방법론등의 패키지의 집합이다.
> - R은 data의 시각화를 위한 다양한 그래픽 도구를 제공
> - R은 모든 객체는 메모리로 로딩되어 고속으로 처리되고 재사용 가능



###  R 기본 명령어



※ R 패키지 개수 확인 : dim(available.packages())

※ R session은 사용자가 R프로그램을 시작한 후 R콘솔 시작 ~ 종료까지의 수행된 정보 : sessioninfo()

※ R 프로그램 버전, 운영체제 정보, 다국어 지원현황, 기본 설치된 R패키지 정보 출력함

※ 설치된 R패키지 목록 확인 : installed.packages()

※ R 패키지 설치 
			install.packages("stringr")
			//update.packages("stringr")
			remove.packages("stringr")

※ 설치된 패키지를 사용하기 위해서 메모리에 로드 : library(stringr) or require(stringr)

※ 메모리에 로드된 패키지 검색 : search(stringr)

※ 기본 데이터 셋 보기 : data()



※ 빈도수 히스토그램



※ 빈도수 히스토그램 :

``` R
hist(Nile)
```

※ 밀도 기분 히스토그램 

```R
 hist(Nile, freq=F)
```

※ 분포곡선 그리기 

```R
lines(density(Nile))
```

※ Plots영역에 표시할 그래프 개수 설정

```R
par(mfrow=c(1,1))
```

※ 파일 출력 경로

```R
pdf("c:/workspaceR/smaple.pdf")
```

※ 정규분포를 따르는 난수 20개 생성해서 히스토그램 생성

```R
hist(rnorm(20))
```

※ 출력 파일 닫기

```R
dev.off()
```



※ 변수 선언

- 첫문자는 영문자로 시작
- 두번째 문자부터는 숫자, _ , . 사용가능
- 대소문자 구분
- 예약어 사용 불가
- 변수에 저장된 값은 불변

> ```R
> x <- 3
> tracemem(x) # "<000000000FCD5C00>" 
> x <- 'a'
> tracemem(x) # "<00000000123B9470>"
> ```

- R은 변수를 선언할 때 자료형(Type)을 선언하지 않습니다.



※ 데이터 타입

- Scalar 변수 - 단일 값(하나의 값)을 저장하는 변수

```R
age <- 30
# age변수는 하나의 값을 저장하고 잇는 벡터 타입
```

- Vector - 하나 이상의 여러 개의 자료를 저장할 수 있는 1차원의 선형 자료 구조

  ```R
  class(age) # numeric
  age <- "29"
  class(age) # character
  age <- TRUE # 상수 객체(TRUE, FALSE)
  class(age) # logical
  
  #T변수에 TRUE 저장, F변수에 FALSE 저장
  age <- F
  class(age) # logical
  
  age <- NA  #결측치 (Not Available)
  class(age+10) # numeric
  age <- NULL # NULL
  class(age+10) # numeric
  ```

- 결측치 처리

```R
sum(10, 20, 30) # 60
sum(10, 20, 30, NA) # NA
sum(10, 20, 30, NA, na.rm=T) # 60
```



※ R Session에서 생성한 변수 목록 확인

```R
ls()
```

※ 자료형 확인

```R
is.numeric(변수)
is.logical(변수)
is.character()
is.na()
is.list(객체)
is.data.frame()
is.array()
is.matrix()
```

※ 자료형 형변환

```R
as.numeric(변수)
as.logical(변수)
as.character(변수)
as.na(변수)
as.list(객체)
as.data.frame(객체)
as.array(객체)
as.matrix(객체)
as.integer(변수)
as.double(변수)
as.complex(변수) # 복소수
as.factor(객체)
as.Date(객체)
```

```R
x <- c("1", "2", "3")
result <- x *3
print(result) # 3 6 9 
result <- as.numeric(x) *3
print(result) # 3 6 9
result <- as.integer(x) * 3
print(result) # 3 6 9
```

```R
z <- 5.3 - 3i #복소수 자료형 생성
class(z) # "complex"
Re(z) # 실수부만 반환  "5.3"
Im(z) # 허수부만 반환  "-3"
is.complex(z) # TRUE
as.complex(5.3) # 5.3+0i
```

※ class(변수) 는 자료구조의 Type을 반환

※ mod(변수) 는 자료의 Type을 반환

```R
age <- 29.5
mode(age) # "numeric"
age <- "29"
mode(age) # "character"
age <- TRUE
mode(age) # "logical"
age <-F
mode(age) # "logical"
```

※ 변수 설정

```R
objects( ) # 생성한 모든 변수 확인
rm(list=ls()) # 모든 변수들을 삭제
rm(var3) # 변수 삭제
```



※ 연산자

```R
/ 나누기 (실수 가능)
%/% 정수 나누기
%% 나머지 구하기
^, ** 승수 구하기
```

※ 진리값

```R
 TRUE & TRUE # TRUE
 TRUE & FALSE # FALSE
 TRUE | TRUE # TRUE
 TRUE | FALSE # TRUE
 !TRUE # FALSE
 !FALSE # TURE
 T <- FALSE 
 TRUE <- FALSE # Eroor
 c(TRUE, TRUE) & c(TRUE, FALSE) # TRUE FALSE
 c(TRUE, TRUE) && c(TRUE, FALSE) # TRUE
```

※ 날짜와 시간

```R
Sys.Date() # 날짜만 보여주는 함수
Sys.time() # 날짜와 시간을 보여주는 함수
date() # 미국식 날짜와 시간을 출력하는 함수
as.Date(‘2017-12-01’) # 문자형태의 날짜를 날짜타입으로 변환해주는 함수
as.Date('2017/07/04')
as.Date('04-07-2017') #오류
as.Date(‘2017-12-01’ , format=‘%d-%m-%Y’)
as.Date(10, origin=‘2017-12-01’) #주어진 날짜 기준으로 10일후의 날짜
as.Date(-10, origin=‘2017-12-01’) #주어진 날짜 기준으로 10일 이전 날짜
```

- 날짜 format

```R
%d 일자를 숫자로 인식
%m 월 을 숫자로 인식
%b 월을 영어 약어로 인식
%B 월을 전체 이릉으로 인식
%y 년도를 숫자 두 자리로 인식
%Y 년도를 숫자 네 자리로 인식
```



※ 작업 디렉토리설정

```R
getwd()
setwd("c:/workspace")
getwd()
```



※ Sys.setlocale(category="LC_ALL", locale="언어_국가")

※ 현재 로케일 정보 전체 확인

```R
Sys.setlocale(category="LC_ALL", locale="")
Sys.getlocale()

Sys.setlocale(category="LC_ALL", locale="Korean_Korea")
Sys.getlocale()

Sys.setlocale(category="LC_ALL", locale="English_US")
Sys.getlocale()

Sys.setlocale(category="LC_ALL", locale="Japanese_Japan")
Sys.getlocale()
```



※ R 에서 제공하는 기본 함수 사용 예제 보기

```R
example(seq)
```

※ R 에서 제공하는 함수의 파라미터 형식 보기

```R
args(max)
```



※ 도움말

```R
help(mean)
?mean
??mean
```





### FACT 형


- 여러 번 중복으로 나오는 데이터들을 각 값으로 모아서 대표 값을 출력해 주는 형태
- stringsAsFactors=FALSE 옵션은 대표값으로 정리하지 않고 중복되는 상태 그대로 사용하게 해 줍니다.
- 범주형Categorical 데이터(자료)를 표현하기 위한 데이터 타입
- 범주형 데이터 - 데이터가 사전에 정해진 특정 유형으로만 분류되는 경우
- 범주형 데이터는 또 다시 명목형(Nominal)과 순서형(Ordinal)으로 구분
- 명목형 데이터는 값들 간에 크기 비교가 불가능한 경우
- 순서형 데이터는 대, 중, 소와 같이 값에 순서를 둘 수 있는 경우

```R

gender <- c("man","woman","woman","man","man")
plot(gender) # 차트는 수치 데이터만 가능하므로 오류
class(gender) # "character"
mode(gender) # "character"

ngender <- as.factor(gender) # 범주의 순서가 알파벳 순서로 정렬됨
class(ngender) #"factor"
mode(ngender) # "numeric"
table(ngender)
plot(ngender)
is.factor(ngender) # TRUE
ngender # Levels속성에서 범주를 확인 (알파벳 순서?)

args(factor) # factor()함수의 매개변수 확인
ogender <- factor(gender, levels <- c("woman" , "man"), ordered=T)
ogender  # 범주의 순서 확인

par(mfrow = c(1,2))
plot(ngender)
plot(ogender)
```





### Vector

> R에서 가장 기본이 되는 자료 구조, 1차원, 선형구조

- 요소의 접근 변수[ index첨자 ]로 접근, 첨자 index는 1부터 시작합니다.

- 동일한 데이터타입만 저장 가능

- 벡터 생성 함수

  ```R
  c()
  seq()
  rep()
  ```

- 벡터 자료 처리 함수 

  ```R
  union()
  setdiff()
  intersect()
  ```

```R
c(1:20)
1:20
c(1,2,3,3,3,4,5,5,5,5)
seq(1,20)
seq(1, 20, 2) #순차적으로 값을 증감 시켜서 벡터 자료 구조 생성
rep(1:3, 3)
rep(1:3, each=3)

a<-c(1:5)
b<-a+1 # 2 3 4 5 6
b<-a*2 # 2 4 6 8 10


a<-c(1:5)
d<- rep(1:3, 3)
union(a, d) # 1 2 3 4 5 
setdiff(a, d) # 4 5 
intersect(a, d) # 1 2 3

f <- c(33, -5, "4" , 5:9) # 자료형이 혼합된 경우, 문자열이 포함된 경우 자동으로 형변환
class(f)
mode(f)

a<- c(1:20)
a[3:10] # 벡터의 요소에 접근
a[c(3, 10)] # 벡터의 요소에 접근
a[-c(2:18)] # 벡터의 첨자에 -를 지정하면 해당 위치의 원소는 제외

```

