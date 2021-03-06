# 미국으로 여행을 떠났다.
# 파이썬을 이용하여 총 소요 경비를 계산하는 프로그램을 작성하시오.
# 1. 비행기 예약 - 4인가족(성인2명/소아1명/유아1명)
# 2. 인천-샌프란시스코 왕복 953,200원(유아는 10%차지)
# 3. 호텔 예약(5박) - 1박에 $125.00(리조트 $45.00 + tax 5.5% 추가)
# 4. 달러 환전 - 3,000불(금일 환율 1달러에 1,147) + 은행수수료 0.45%
# 5. 첫날 저녁 식대 - $135.52(tax 6.75% + tip 15%)
# 6. 주차비 - 최초 30분 $2.50 매 15분 마다 $1.25씩 추가
# 7. 3시간 20분 주차했을 때 주차비 계산

성인 = int(input("성인이 총 몇명입니까?"))
소아 = int(input("소아가 총 몇명입니까?"))
유아 = int(input("유아가 총 몇명입니까?"))
몇박 = int(input("총 몇박 머무르실 생각입니까?"))
환율 = 1230
인샌왕복성인 = 953200*성인
인샌왕복유아 = 인샌왕복성인*1/10*유아+소아
호텔 = 125*환율*몇박  # 현재 환산 기준 1달러 = 1230원
환전 = (3000*환율) + (3000*45/100*환율)
첫날저녁식대 = 135.52*환율
주차비 = 2.5*환율*((24*60*몇박)/15)
총경비 = 인샌왕복성인 + 인샌왕복유아 + 호텔 + 환전 + 첫날저녁식대 + 주차비
print("총 경비는" + str(총경비) + "원 입니다. 즐거운 여행 되세요.")
