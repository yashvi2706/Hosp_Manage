import os
import csv
from datetime import datetime,timedelta,date
from appointment_manager import Appointment_Manager
from tkinter import messagebox
from file_manager import load_doctor_dict
from patient_manager import Patient_Manager
from doctor_manager import DoctorManager

def save_appointment_to_csv(patient_name, doctor, date, month, year, timeslot, status="Pending"):
    file_exists = os.path.isfile('hospital.csv')

    appointment_id = 1
    if file_exists:
        with open('hospital.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row:
                    appointment_id = int(row[0]) + 1

    appointment = Appointment_Manager(appointment_id, patient_name, doctor, date, month, year, timeslot, status)

    appointment.save_to_csv()

    return appointment_id

def check_appointment(nameentry, doctor_combobox, timeslot_combobox, date_label):
    patient_name = nameentry.get()
    doctor_selected = doctor_combobox.get()

    date_text = date_label['text'].replace("Next Available: ", "").strip()
    date_object = datetime.strptime(date_text, "%A, %d %B %Y") if date_text else None
    selected_timeslot = timeslot_combobox.get()
    myappt = {}
    myappt['Doctor Name'] = doctor_selected
    myappt['Timeslot'] = selected_timeslot
    myappt['Date'] = str(date_object.day)
    myappt['Month'] = str(date_object.month)
    myappt['Year'] = str(date_object.year)
    mydoc_obj = DoctorManager(doctor_selected)
    if not patient_name or not doctor_selected or not selected_timeslot or not date_text:
        messagebox.showerror("Error", "All fields (Name, Doctor, Timeslot, and Date) must be filled!")
    elif mydoc_obj.check_if_already_booked(myappt) :
        messagebox.showerror('Error', 'Doctor not available, book through date or choose another doctor.')
    else:
        appointment = Appointment_Manager(None, patient_name, doctor_selected, date_object.day, date_object.month,
                                  date_object.year, selected_timeslot)

        appointment_id = appointment.save_to_csv()
        patient_obj = Patient_Manager('hospital.csv')
        patient_obj.print_appointment()
        messagebox.showinfo(
            "Success",
            f"Appointment booked successfully!\n"
            f"Appointment ID: {appointment_id}\n"
            f"Doctor: {doctor_selected}\n"
            f"Timeslot: {selected_timeslot}\n"
            f"Date: {date_object.strftime('%A, %d %B %Y')}\n"
            f"Patient Name: {patient_name}\n"
            f"Kindly note your Appointment ID.\n"
            f"It will be useful for searching your appt. details."

        )


def confirm_booking(nameentry, doctor_combobox, timeslot_combobox, date_combobox, month_combobox, year_combobox):
    patient_name = nameentry.get()
    doctor_selected = doctor_combobox.get()
    selected_timeslot = timeslot_combobox.get()
    selected_date = date_combobox.get()
    selected_month = month_combobox.get()
    selected_year = year_combobox.get()
    myappt = {}
    myappt['Doctor Name'] = doctor_selected
    myappt['Timeslot']=selected_timeslot
    myappt['Date'] = selected_date
    myappt['Month'] = selected_month
    myappt['Year'] = selected_year
    mydoc_obj = DoctorManager(doctor_selected)
    if not patient_name or not doctor_selected or not selected_timeslot or not selected_date or not selected_year:
        messagebox.showerror("Error", "All fields (Name, Doctor, Timeslot, Date, and Year) must be filled!")
    elif mydoc_obj.check_if_already_booked(myappt) :
        messagebox.showerror('Error', 'The date has already been booked. Choose another date.')
    else:
        booking_date = datetime(int(selected_year), int(selected_month), int(selected_date))

        # Save the appointment and calculate the new appointment ID
        appointment_id = save_appointment_to_csv(patient_name, doctor_selected, booking_date.day, booking_date.month, booking_date.year, selected_timeslot)
        patient_obj = Patient_Manager('hospital.csv')
        patient_obj.print_appointment()
        messagebox.showinfo(
            "Success",
            f"Appointment booked successfully!\n"
            f"Appointment ID: {appointment_id}\n"
            f"Doctor: {doctor_selected}\n"
            f"Timeslot: {selected_timeslot}\n"
            f"Date: {booking_date.strftime('%A, %d %B %Y')}\n"
            f"Patient Name: {patient_name}\n"
            f"Kindly note your Appointment ID.\n"
            f"It will be useful for searching your appt. details."
        )




def on_doctor_status_selected(doctor_object, status_combobox, appointment_combobox, new_status_combobox):
    selected_status = status_combobox.get()

    if doctor_object and selected_status:
        filtered_appointments = doctor_object.get_appointments(selected_status)
        appointment_ids = [appt['Appointment ID'] for appt in filtered_appointments]
        appointment_combobox['values'] = appointment_ids
        if selected_status == "Approved":
            new_status_combobox['values'] = ['Completed']
        else:
            new_status_combobox['values'] = ['Cancelled', 'Approved']

def on_status_change(doctor_object, appointment_combobox, new_status_combobox):
    selected_appointment_id = appointment_combobox.get()
    new_status = new_status_combobox.get()

    if selected_appointment_id and new_status:
        doctor_object.update_appointment_status(selected_appointment_id, new_status)
        messagebox.showinfo("Status Update", f"Status updated to {new_status} for Appointment ID {selected_appointment_id}")
    else:
        messagebox.showwarning("Selection Error", "Please select an appointment and a new status.")
