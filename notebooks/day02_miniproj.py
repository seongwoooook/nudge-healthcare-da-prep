import random
answer= random.randint(1,10)

guess = int(input("숫자를 맞혀보세요: "))

is_correct = False
is_big = False

if guess == answer :
    is_correct = True
elif guess > answer :
    is_big = True

if is_correct :
    print("정답입니다 !")
else :
    if is_big:
        print("정답보다 큽니다 !")
    else :
        print("정답보다 작습니다 !")