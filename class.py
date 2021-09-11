class Person:
    def __init__(self, name, age):
        self.username = name
        # 여기서 name은 매개변수로 무언갈 넣어줬는데, 그걸 username에 넣어주겠다.
        # 여기서 usename이 Person이라는 클래스가 가지고 있는 것이다.
        self.age = age
        # 즉, Person 클래스는 username과 age값을 가지고 있다.

    def talk(self):
        print('말하는 중 입니다.')
    # 함수는 반드시 return 값을 가지지 않아도 된다.


person = Person('Lily', 99)
print(person.username)
person.username = 'Ella'  # Person의 username을 Lily에서 Ellas로 바꾸겠다.
person.talk()  # 함수호출
