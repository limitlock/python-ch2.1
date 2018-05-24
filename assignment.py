# 치환문 예
a = 1
b = a + 1
print(a, b)

# 변수값 할당 오류
# 1 + a = c

# 세미콜론으로 치환문을 구분할 수 있다.
e = 3.5; f = 5.3
print(e, f)

# 여러 개를 한 번에 치환
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 할당할 때
x = y = z = 10
print(x, y, z)

# C 스타일은 지원 안한다.
# x = (y = 10)

# 값 교환
f, e = e, f
print(e, f)

# 동적 타이핑: 변수에 새로운 값이 할당되면 기존의 값을 버리고
# 새로운 값으로 치환된다.
a = 1
print(type(a))

a = "hello"
print(type(a))

# 확장 치환문
a = 10
a += 10
print(a)

a -= 3
print(a)

