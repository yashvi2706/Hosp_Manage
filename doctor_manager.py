import csv
from tkinter import messagebox

class DoctorManager:
    def __init__(self, name):
        self.name = name

    def load_appointments(self):
        appointments = []
        try:
            with open('hospital.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    appointments.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "The hospital.csv file was not found.")
        return appointments

    def save_appointments(self, appointments):
        with open('hospital.csv', mode='w', newline='') as file:
            fieldnames = ['Appointment ID', 'Patient Name', 'Doctor Name', 'Date', 'Month', 'Year', 'Timeslot', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(appointments)

    def update_status(self, appointment_id, new_status):
        appointments = self.load_appointments()
        for appointment in appointments:
            if appointment['Appointment ID'] == appointment_id:
                appointment['Status'] = new_status
        self.save_appointments(appointments)

    def get_appointments(self, status=None):
        appointments = self.load_appointments()
        filtered_appointments = [appt for appt in appointments if appt['Doctor Name'] == self.name]

        if status:
            filtered_appointments = [appt for appt in filtered_appointments if appt['Status'] == status]

        return filtered_appointments

    def update_appointment_status(self, appointment_id, new_status):
        self.update_status(appointment_id, new_status)

    def view_appointments(self, status=None):
        return self.get_appointments(status)

    def check_if_already_booked(self,myappt):
        appointments = self.load_appointments()
        for appt in appointments:
            if (appt['Doctor Name'] == myappt['Doctor Name'] and appt['Date'] == myappt['Date'] and
                appt['Month'] == myappt['Month'] and appt['Year'] == myappt['Year'] and
                 appt['Timeslot'] == myappt['Timeslot']):
                return True
        return False
