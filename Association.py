class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor

# Example Usage
if __name__ == "__main__":
    doc = Doctor("Dr. House")
    patient = Patient("John Doe")
    patient.assign_doctor(doc)
    print(f"[Association] {patient.name} is treated by {patient.doctor.name}")