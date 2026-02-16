# age = int(input("나이를 입력하세요 : "))
#
# if age >=20 :
#     print("성인입니다")
# elif age >=14 :
#     print("청소년입니다")
# else:
#     print("어린이입니다")

# age = int(input("나이를 입력하세요 : "))
# has_id = input("신분증이 있나요? (Y/N): ")
#
# if age>=20 and has_id =="Y" :
#     print("술집 입장이 가능합니다.")
# else:
#     print("술집 입장이 불가능합니다.")

# 키 140이상이고 나이가 10살 이상이어야 탑승 가능한 탑승 여부 프로그램을 만들어보자.
# 단, 보호자 동반이면 키 120이상도 가능

age = int(input("몇살이신가요? : "))
height = int(input("키가 어떻게 되시나요? : "))
guardian = input("보호자 동반인가요? (yes/no): ")


if guardian == "yes" :
    if age >= 10 and height >=120 :
        print("탑승 가능")
    else :
        print("탑승 불가능")
else:
    if age >=10 and height >=140 :
        print("탑승 가능")
    else:
        print("탑승 불가능")