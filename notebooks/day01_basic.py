print ("Hello, Nudge!")

a = 10
b = 3

print(a+b)
print(a*b)

age = 23
print("내 나이는",age,"살입니다 !")
print("내 나이는"+str(age)+"살입니다 !")
print(f"내 나이는 {age}살입니다 !")
print("내 나이는",age,"살입니다 !",sep="")

value = 10
print(f"{value * 3}")

print(f"내 나이는 {age:05d}살입니다")

age = int(input("나이를 입력하세요: "))
print(f"당신의 나이는 {age}살입니다.")

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

print(type(10))
print(type("10"))
print(type(10.5))