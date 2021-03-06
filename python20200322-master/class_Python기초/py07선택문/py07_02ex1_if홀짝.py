# 정수를 입력을 받습니다.
# 입력 받은 문자열을 정수로 바꿉니다.
입력 = input("정수를 입력하세요: ")

# 숫자로 변환하기
정수 = int(입력)


#######################################
# 홀수, 짝수 판별법
# 방법1. 나머지를 사용하는 방법
# 방법2. 문자열을 사용하는 방법
#######################################


#######################################
# 방법1. 나머지를 사용하여 짝수 , 홀수 판별하는 방법
#######################################
# 짝수 확인
if 정수 % 2 == 0:
    print("짝수입니다")

# 홀수 확인
if 정수 % 2 == 1:
    print("홀수입니다")


#######################################
# 방법2. 문자열을 사용하는 방법
#######################################
# 마지막 자리 숫자를 추출
마지막글자 = 입력[-1]

# 숫자로 변환하기
마지막숫자 = int(마지막글자)


if 마지막숫자 == 0 \
   or 마지막숫자 == 2 \
   or 마지막숫자 == 4 \
   or 마지막숫자 == 6 \
   or 마지막숫자 == 8:
    print("짝수") 

if 마지막숫자 == 1 \
   or 마지막숫자 == 3 \
   or 마지막숫자 == 5 \
   or 마지막숫자 == 7 \
   or 마지막숫자 == 9:
    print("홀수")
