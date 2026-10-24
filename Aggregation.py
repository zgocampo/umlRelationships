class Professor:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

# Example Usage
if __name__ == "__main__":
    prof = Professor("Dr. Alan Turing")
    dept = Department("Computer Science")
    dept.add_professor(prof)
    print(f"[Aggregation] Department {dept.name} has professor: {dept.professors[0].name}")