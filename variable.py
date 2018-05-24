import keyword

# 변수 이름은 문자, 숫자, _ 로 구성된다.
friend = 1
a = 10
my_name = "안대혁"
myName = "안대혁"
_yourName = "둘리"
member1 = "도우넛"

# 에러: 다른 구성의 변수 이름은 사용할 수 없다.
# friend$ = 1
# a! = 10
# 1abc = 10

# 에러: 예약어는 변수이름으로 사용할 수 없다.
# def = 10

print(keyword.kwlist)
print(len(keyword.kwlist))

# 한글이름의 변수도 사용 가능하다
가격1 = 2000
print(가격1-200)
