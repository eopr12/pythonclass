# 목적 :
#       국어, 수학, 영어, 과학 과목을 듣는 학생들의 총점과 평균을
#       구하는 성적 관리 프로그램 객체 지향 방식을 사용하여 만들어 보자.
#
# 테스트 데이터
#       {'이름': '윤인성', '국어': 87, '수학': 98, '영어': 88, '과학': 95},
#       {'이름': '연하진', '국어': 92, '수학': 98, '영어': 96, '과학': 98},
#       {'이름': '구지연', '국어': 76, '수학': 96, '영어': 94, '과학': 90},
#       {'이름': '나선주', '국어': 98, '수학': 92, '영어': 96, '과학': 92},
#       {'이름': '윤아린', '국어': 95, '수학': 98, '영어': 98, '과학': 98},
#       {'이름': '윤명월', '국어': 64, '수학': 88, '영어': 92, '과학': 92},
#       {'이름': '김미화', '국어': 82, '수학': 86, '영어': 98, '과학': 88},
#       {'이름': '김연화', '국어': 88, '수학': 74, '영어': 78, '과학': 92},
#       {'이름': '박아현', '국어': 97, '수학': 92, '영어': 88, '과학': 95},
#       {'이름': '서준서', '국어': 45, '수학': 52, '영어': 72, '과학': 78},
#
# 출력 결과 예시
#       이름    총점    평균
#       윤인성  368     92.0
#       연하진  384     96.0
#       구지연  356     89.0
#       나선주  378     94.5
#       윤아린  389     97.25
#       윤명월  336     84.0
#       김미화  354     88.5
#       김연화  332     83.0
#       박아현  372     93.0
#       서준서  247     61.75

# 작업 순서 
# 클래스를 선언합니다.
# 학생 리스트를을 선언합니다.
# Student 인스턴스의 속성에 접근하는 방법
# 학생을 한 명씩 반복합니다.
# 인스턴스 확인하기


# 코딩 하기 

# 클래스를 선언합니다.


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        print("{} - 생성 되었습니다".format(self.name))

    def __del__(self):
        print("{} - 파괴 되었습니다".format(self.name))

    def getsum(self):
        return self.korean + self.math +\
            self.english + self.science

    def getavg(self):
        return self.getsum() / 4

    def to_string(self):
        return "%s\t%s\t%s" % (self.name, self.getsum(), self.getavg())


# 학생 리스트를을 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
    Student("김미화", 82, 86, 98, 88),
    Student("김연화", 88, 74, 78, 92),
    Student("박아현", 97, 92, 88, 95),
    Student("서준서", 45, 52, 72, 78)
]


# Student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 출력합니다.
    print(student.to_string())


# 인스턴스 확인하기
print("isinstance(student, Student):", isinstance(student, Student))
