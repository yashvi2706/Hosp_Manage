import csv

class Patient_Manager:
    def __init__(self, csv_file='hospital.csv'):
        self.csv_file = csv_file
        self.appointment_id = None
        self.patient_name = None
        self.doctor_name = None
        self.date = None
        self.month = None
        self.year = None
        self.timeslot = None
        self.status = None
        self.load_last_appointment()

    def load_last_appointment(self):
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)

                if len(rows) > 1:
                    last_appointment = rows[-1]

                    self.appointment_id = last_appointment[0]
                    self.patient_name = last_appointment[1]
                    self.doctor_name = last_appointment[2]
                    self.date = last_appointment[3]
                    self.month = last_appointment[4]
                    self.year = last_appointment[5]
                    self.timeslot = last_appointment[6]
                    self.status = last_appointment[7]

                    self.print_appointment()
                else:
                    print("No appointments found in the file.")

        except FileNotFoundError:
            print(f"The file {self.csv_file} does not exist.")

    def print_appointment(self):
        print('An appointment was just created')
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient Name: {self.patient_name}")
        print(f"Doctor Name: {self.doctor_name}")
        print(f"Date: {self.date}/{self.month}/{self.year}")
        print(f"Timeslot: {self.timeslot}")
        print(f"Status: {self.status}")