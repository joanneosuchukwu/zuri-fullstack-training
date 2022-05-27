class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, track: list, score: float):
        self.name:str = name
        self.age:int = age
        self.track:list = track
        self.score:float = score

    def change_name(self, name):
        self.name = name
        return str(self.name)

    def change_age(self, age):
        self.age = age
        return int(self.age)

    def add_track(self, track):
        self.track.append(track)
        print(self.track)

    def get_score(self):
        return self.score 
        
Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
