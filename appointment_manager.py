import os
import csv

class Appointment_Manager:
    def __init__(self, appointment_id, patient_name, doctor_name, date, month, year, timeslot, status="Pending"):
        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.month = month
        self.year = year
        self.timeslot = timeslot
        self.status = status

    def save_to_csv(self):

        file_exists = os.path.isfile('hospital.csv')

        appointment_id = 1
        if file_exists:
            with open('hospital.csv', mode='r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    if row:
                        appointment_id = int(row[0]) + 1
        clean_timeslot = self.timeslot.replace("'", "").replace('"', "")

        with open('hospital.csv', mode='a', newline='') as csvfile:
            fieldnames = ['Appointment ID', 'Patient Name', 'Doctor Name', 'Date', 'Month', 'Year', 'Timeslot', 'Status']
            appointment_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                appointment_writer.writeheader()
            appointment_writer.writerow({
                'Appointment ID': appointment_id,
                'Patient Name': self.patient_name,
                'Doctor Name': self.doctor_name,
                'Date': self.date,
                'Month': self.month,
                'Year': self.year,
                'Timeslot': clean_timeslot,
                'Status': self.status
            })

        self.appointment_id = appointment_id
        return appointment_id

    def __str__(self):
        return (f"Appointment ID: {self.appointment_id}, "
                f"Patient Name: {self.patient_name}, "
                f"Doctor: {self.doctor_name}, "
                f"Date: {self.date}/{self.month}/{self.year}, "
                f"Timeslot: {self.timeslot}, "
                f"Status: {self.status}")