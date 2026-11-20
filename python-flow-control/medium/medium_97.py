# 도형 종류에 따라 필요한 값을 입력받으세요.
shape = input()

# 원 넓이 공식
if shape == "원":
    radius = int(input())
    result = radius * radius * 3.14
    print(f"넓이: {result:.2f}")

# 삼각형 공식
elif shape == "삼각형":
    width = int(input())
    height  = int(input())
    result = width * height  / 2
    print(f"넓이: {result}")

# 사각형 공식
elif shape == "사각형":
    width = int(input())
    height = int(input())
    result = width * height
    print(f"넓이: {result}")