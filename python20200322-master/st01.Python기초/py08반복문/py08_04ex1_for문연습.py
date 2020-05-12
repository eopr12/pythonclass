
# 500과 1000 사이에 있는 홀수의 합계를 구하시오
# 출력 예시) 500과 1000 사이에 있는 홀수의 합계 : 187500



# 0과 100 사이에 있는 7의 배수의 합계를 구하시오
# 출력 예시) 0과 100 사이에 있는 7의 배수의 합계 : 735


# 정수 값을 입력받고 
# 1부터 입력 받은 정수까지의 합계를 구하시오.
# 출력 예시) 
# 값을 입력하세요: 100
# 1에서 100 까지의 합계 : 5050



# 시작값, 끝값 그리고 증가값을 입력받고 
# "시작값"부터 "끝값"까지 합계를 구하시오.
# 출력 예시) 
# 시작값을 입력하세요: 2
# 끝값을 입력하세요: 300
# 증가값을 입력하세요: 3
# 1에서 300 까지 3씩 증가시킨 값의 합계 : 15050
시작값 = input( "시작값을 입력하세요: ")
끝값  = input( "끝값을 입력하세요: ")
증가값 = input( "증가값을 입력하세요: ")

시작값 = int( 시작값)
끝값   = int( 끝값  )
증가값 = int( 증가값)

sum = 0
for i in range( 시작값, 끝값+1, 증가값):
    sum = sum + i

# 1에서 300 까지 3씩 증가시킨 값의 합계 : 15050
print ( "%s에서 %s 까지 %s씩 증가시킨 값의 합계 : %s" % (시작값, 끝값, 증가값, sum) )


# "1에서 300" 까지 라는 문자열을 만드시오
str1 = "1에서 300"
print( str1 )  # 1에서 300


시작값 = 1 
끝값 = 300
str2 = str(시작값) + "에서" + str(끝값)+ "까지" 
print( str2) # 1에서 300

str2 = "%s에서 %s까지"  % ( 시작값, 끝값 )
print( str2) # 1에서 300


