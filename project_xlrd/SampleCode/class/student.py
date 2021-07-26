class Student:
    # 객체 내부의 변수
    name, address, phone = '','',''

    # 생성자 정의 (필수는 아님)
    def __init__(self, iname, iaddress, iphone):
        self.name, self.address, self.phone = iname, iaddress, iphone

    def info_print(self):
        str = "이름 : {}, 주소 : {}, 연락처 : {}"
        print(str.format(self.name, self.address, self.phone))

# 객체를 생성
학생 = Student('리턴제로', '인천시 연수구', '010-1234-5678')

# 객체의 함수를 호출
학생.info_print()

# 객체의 변수 접근
print(학생.name)