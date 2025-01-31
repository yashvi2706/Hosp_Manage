from tkinter import *
from tkinter import messagebox,ttk
import csv
import os
from datetime import datetime, timedelta
from file_manager import *
from doctor_manager import *
from system_logic import *
from patient_manager import *

def center_window(window, width=400, height=300):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

def HOMEUI():
    home_window = Tk()
    home_window.title("Hospital Management System")
    home_window.geometry('400x300')
    center_window(home_window, 400, 300)

    home_window.configure(bg='#f0f8ff')

    title_label = Label(home_window, text="Welcome to Artemis Hospital", font=("Helvetica", 16, "bold"), bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

    whoyoulabel = Label(home_window, text='Who are you?', font=("Arial", 14), bg='#f0f8ff')
    whoyoulabel.grid(row=1, column=0, columnspan=3, pady=10)

    patientbutton = Button(home_window, text='Patient', font=("Arial", 12), pady=10, padx=20, relief=RAISED,
                           bg='#d1e7dd', command=openpatientwindow)
    patientbutton.grid(row=2, column=0, padx=20, pady=10)

    doctorbutton = Button(home_window, text='Doctor', font=("Arial", 12), pady=10, padx=20, relief=RAISED,
                          bg='#ffdfba', command=opendoctorselectionwindow)
    doctorbutton.grid(row=2, column=1, padx=20, pady=10)

    adminbutton = Button(home_window, text='Admin', font=("Arial", 12), pady=10, padx=20, relief=RAISED,
                         bg='#ffccd5', command=adminpasswordwindow)
    adminbutton.grid(row=2, column=2, padx=20, pady=10)

    exit_button = Button(home_window, text="Exit", font=("Arial", 10), pady=5, padx=20, bg='#e9ecef', command=home_window.quit)
    exit_button.grid(row=3, column=0, columnspan=3, pady=20)
    home_window.mainloop()

def openpatientwindow():
    patientwindow = Toplevel()
    patientwindow.title("Patient Portal")
    patientwindow.geometry('440x300')
    center_window(patientwindow, 440, 300)
    patientwindow.configure(bg='#f0f8ff')

    title_label = Label(patientwindow, text="Patient Portal", font=("Helvetica", 16, "bold"), bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

    makeappointmentbutton = Button(patientwindow, text='Make Appointment', font=("Arial", 12), pady=10, padx=20,
                                   bg='#d1e7dd', relief=RAISED, command=makeappointmentwindow)
    makeappointmentbutton.grid(row=1, column=0, padx=20, pady=10)

    searchappointmentbutton = Button(patientwindow, text='Search Appointment', font=("Arial", 12), pady=10, padx=20,
                                     bg='#ffdfba', relief=RAISED, command=make_patient_window_for_search)
    searchappointmentbutton.grid(row=1, column=1, padx=20, pady=10)

    close_button = Button(patientwindow, text="Close", font=("Arial", 10), pady=5, padx=20, bg='#e9ecef',
                          command=patientwindow.destroy)
    close_button.grid(row=3, column=0, columnspan=2, pady=20)
    patientwindow.mainloop()

def makesearchappointmentwindow(appointment_id):
    makesearchappointmentwindow = Toplevel()
    makesearchappointmentwindow.title("Search Appointment")
    makesearchappointmentwindow.geometry('250x200')
    center_window(makesearchappointmentwindow, 400, 300)

    makesearchappointmentwindow.configure(bg='#f0f8ff')

    title_label = Label(makesearchappointmentwindow, text="Appointment Details", font=("Helvetica", 16, "bold"),
                        bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

    try:
        with open('hospital.csv', mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['Appointment ID'] == appointment_id:
                    Label(makesearchappointmentwindow, text=f"Patient Name: {row['Patient Name']}", font=("Arial", 12),
                          bg='#f0f8ff').grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
                    Label(makesearchappointmentwindow, text=f"Doctor Name: {row['Doctor Name']}", font=("Arial", 12),
                          bg='#f0f8ff').grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
                    Label(makesearchappointmentwindow, text=f"Date: {row['Date']}-{row['Month']}-{row['Year']}",
                          font=("Arial", 12), bg='#f0f8ff').grid(row=3, column=0, columnspan=2, padx=10, pady=5,
                                                                 sticky="w")
                    Label(makesearchappointmentwindow, text=f"Timeslot: {row['Timeslot']}", font=("Arial", 12),
                          bg='#f0f8ff').grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")
                    Label(makesearchappointmentwindow, text=f"Status: {row['Status']}", font=("Arial", 12),
                          bg='#f0f8ff').grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")
                    return row

            Label(makesearchappointmentwindow, text="Appointment ID not found.", fg="red", font=("Arial", 12),
                  bg='#f0f8ff').grid(row=6, column=0, columnspan=2, pady=10)
            return None
    except FileNotFoundError:
        Label(makesearchappointmentwindow, text="The hospital.csv file was not found.", fg="red", font=("Arial", 12),
              bg='#f0f8ff').grid(row=6, column=0, columnspan=2, pady=10)
        return None

def makeappointmentwindow():
    appointmentwindow = Toplevel()
    appointmentwindow.title("Make Appointment")
    appointmentwindow.geometry('400x300')
    center_window(appointmentwindow, 400, 300)
    appointmentwindow.configure(bg='#f0f8ff')

    title_label = Label(appointmentwindow, text="Make Appointment", font=("Helvetica", 16, "bold"), bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

    bookbydatebutton = Button(appointmentwindow, text='Book by Date', font=("Arial", 12), pady=10, padx=20,
                              bg='#ffdfba', relief=RAISED, command=makebookbydatewindow)
    bookbydatebutton.grid(row=1, column=0, padx=20, pady=20)

    bookbydoctorbutton = Button(appointmentwindow, text='Book by Doctor', font=("Arial", 12), pady=10, padx=20,
                                bg='#d1e7dd', relief=RAISED, command=makebookbydoctorwindow)
    bookbydoctorbutton.grid(row=1, column=1, padx=20, pady=20)

    close_button = Button(appointmentwindow, text="Close", font=("Arial", 10), pady=5, padx=20, bg='#e9ecef',
                          command=appointmentwindow.destroy)
    close_button.grid(row=2, column=0, columnspan=2, pady=20)



def makebookbydoctorwindow():
    bookbydoctor_window = Toplevel()
    bookbydoctor_window.title("Book Appointment by Doctor")
    bookbydoctor_window.geometry('300x400')
    center_window(bookbydoctor_window, 300, 400)
    bookbydoctor_window.configure(bg='#f0f8ff')

    doctor_dict = load_doctor_dict()

    title_label = Label(bookbydoctor_window, text="Book by Doctor", font=("Helvetica", 16, "bold"), bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    chooseDoctorlabel = Label(bookbydoctor_window, text='Choose Doctor', font=("Arial", 12), bg='#f0f8ff')
    chooseDoctorlabel.grid(row=1, column=0, padx=20, pady=10, sticky=W)

    available_doctors_combobox = ttk.Combobox(bookbydoctor_window, value=list(doctor_dict.keys()), width=25)
    available_doctors_combobox.grid(row=2, column=0, padx=20, pady=10)

    available_timeslot_combobox = ttk.Combobox(bookbydoctor_window, width=25)
    available_timeslot_combobox.grid(row=3, column=0, padx=20, pady=10)

    selected_date_label = Label(bookbydoctor_window, text="", font=("Arial", 10), bg='#f0f8ff', fg='#ff4500')
    selected_date_label.grid(row=4, column=0, padx=20, pady=10)

    def store_doctor_selection(event):
        doctor_selected = available_doctors_combobox.get()
        selected_year = 2024
        if doctor_selected:
            current_date = datetime.now()

            if selected_year > 2024:
                current_date = current_date.replace(year=2025, month=1, day=1)

            available_days = [day for day in doctor_dict[doctor_selected].keys()]
            next_available_date = None

            for day_offset in range(0, 7):
                potential_date = current_date + timedelta(days=day_offset)
                if potential_date.year > selected_year:
                    break
                if potential_date.weekday() in available_days:
                    next_available_date = potential_date
                    break

            if next_available_date:
                day_of_week = next_available_date.weekday()
                selected_date_label['text'] = f"Next Available: {next_available_date.strftime('%A, %d %B %Y')}"
                available_timeslot_combobox['values'] = doctor_dict[doctor_selected][day_of_week]
                available_timeslot_combobox.current(0)
            else:
                selected_date_label['text'] = "No available dates found."
                available_timeslot_combobox['values'] = []

    available_doctors_combobox.bind("<<ComboboxSelected>>", store_doctor_selection)

    namelabel = Label(bookbydoctor_window, text='Enter Your Name', font=("Arial", 12), bg='#f0f8ff')
    namelabel.grid(row=5, column=0, padx=20, pady=10, sticky=W)
    nameentry = Entry(bookbydoctor_window, width=30)
    nameentry.grid(row=6, column=0, padx=20, pady=10)

    submit_button = Button(bookbydoctor_window, text="Confirm", font=("Arial", 12), bg='#90ee90', padx=10, pady=5,
                           command=lambda: check_appointment(nameentry, available_doctors_combobox,
                                                             available_timeslot_combobox, selected_date_label))
    submit_button.grid(row=7, column=0, padx=20, pady=20)

    close_button = Button(bookbydoctor_window, text="Close", font=("Arial", 10), bg='#e9ecef', padx=10, pady=5,
                          command=bookbydoctor_window.destroy)
    close_button.grid(row=8, column=0, padx=20, pady=10)

def makebookbydatewindow():
    booking_window = Toplevel()
    booking_window.geometry('350x450')
    center_window(booking_window, 350, 450)
    booking_window.configure(bg='#f0f8ff')

    label_style = {'font': ('Arial', 10), 'bg': '#f0f8ff'}
    combobox_style = {'font': ('Arial', 10), 'width': 10}
    button_style = {'bg': '#ffdfba', 'font': ('Arial', 10), 'relief': 'solid', 'padx': 10, 'pady': 5}

    current_date = datetime.now()

    year_label = Label(booking_window, text="Select Year:", **label_style)
    year_label.grid(row=0, column=0, padx=10, pady=5)

    future_years = [year for year in range(current_date.year, 2026)]
    year_combobox = ttk.Combobox(booking_window, values=future_years, **combobox_style)
    year_combobox.grid(row=0, column=1, padx=10, pady=5)
    year_combobox.current(0)

    month_label = Label(booking_window, text="Select Month:", **label_style)
    month_label.grid(row=1, column=0, padx=10, pady=5)

    def get_future_months(selected_year):
        if int(selected_year) == current_date.year:
            return list(range(current_date.month, 13))
        else:
            return list(range(1, 13))

    month_combobox = ttk.Combobox(booking_window, values=get_future_months(current_date.year), **combobox_style)
    month_combobox.grid(row=1, column=1, padx=10, pady=5)

    available_dates_label = Label(booking_window, text="Available Dates:", **label_style)
    available_dates_label.grid(row=3, column=0, padx=10, pady=5)

    date_combobox = ttk.Combobox(booking_window, **combobox_style)
    date_combobox.grid(row=3, column=1, padx=10, pady=5)

    def show_available_dates():
        selected_year = int(year_combobox.get())
        selected_month = int(month_combobox.get())

        first_date = datetime(selected_year, selected_month, 1)
        if selected_month < 12:
            last_date = datetime(selected_year, selected_month + 1, 1) - timedelta(days=1)
        else:
            last_date = datetime(selected_year + 1, 1, 1) - timedelta(days=1)

        available_dates = set()

        if selected_year == current_date.year and selected_month == current_date.month:
            first_date = current_date

        doctor_dict = load_doctor_dict()
        for day in range(first_date.day, last_date.day + 1):
            current_day = first_date.replace(day=day)
            day_of_week = current_day.weekday()
            for doctor, schedule in doctor_dict.items():
                if day_of_week in schedule:
                    available_dates.add(current_day.day)

        date_combobox['values'] = sorted(list(available_dates))

    def update_months(event):
        selected_year = int(year_combobox.get())
        month_combobox['values'] = get_future_months(selected_year)
        month_combobox.current(0)
        show_available_dates()

    year_combobox.bind("<<ComboboxSelected>>", update_months)

    def update_dates(event):
        show_available_dates()

    month_combobox.bind("<<ComboboxSelected>>", update_dates)


    doctors_label = Label(booking_window, text="Doctors Available:", **label_style)
    doctors_label.grid(row=4, column=0, padx=10, pady=5)

    doctor_combobox = ttk.Combobox(booking_window, **combobox_style)
    doctor_combobox.grid(row=4, column=1, padx=10, pady=5)

    timeslots_label = Label(booking_window, text="Available Timeslots:", **label_style)
    timeslots_label.grid(row=5, column=0, padx=10, pady=5)

    timeslot_combobox = ttk.Combobox(booking_window, **combobox_style)
    timeslot_combobox.grid(row=5, column=1, padx=10, pady=5)

    def on_date_selected(event):
        selected_date = date_combobox.get()
        selected_year = int(year_combobox.get())
        if selected_date:
            month = int(month_combobox.get())
            date = int(selected_date)
            booking_date = datetime(selected_year, month, date)
            day_of_week = booking_date.weekday()
            doctor_dict = load_doctor_dict()
            available_doctors = [doctor for doctor in doctor_dict if day_of_week in doctor_dict[doctor]]
            doctor_combobox['values'] = available_doctors
            if available_doctors:
                doctor_combobox.current(0)
                on_doctor_selected()

    date_combobox.bind("<<ComboboxSelected>>", on_date_selected)

    def on_doctor_selected(event=None):
        selected_doctor = doctor_combobox.get()
        selected_date = date_combobox.get()
        selected_year = int(year_combobox.get())
        if selected_doctor and selected_date:
            month = int(month_combobox.get())
            date = int(selected_date)
            booking_date = datetime(selected_year, month, date)
            day_of_week = booking_date.weekday()
            doctor_dict = load_doctor_dict()
            if selected_doctor in doctor_dict and day_of_week in doctor_dict[selected_doctor]:
                timeslot_combobox['values'] = doctor_dict[selected_doctor][day_of_week]
                timeslot_combobox.current(0)

    doctor_combobox.bind("<<ComboboxSelected>>", on_doctor_selected)

    namelabel = Label(booking_window, text='Enter Your Name:', **label_style)
    namelabel.grid(row=6, column=0, padx=10, pady=5)
    nameentry = Entry(booking_window)
    nameentry.grid(row=6, column=1, padx=10, pady=5)

    submit_button = Button(booking_window, text="Confirm",
                           command=lambda: confirm_booking(nameentry, doctor_combobox, timeslot_combobox, date_combobox,
                                                           month_combobox, year_combobox), **button_style)
    submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def make_patient_window_for_search():
    patient_pw_window = Toplevel()
    patient_pw_window.title("Enter Appointment ID")
    patient_pw_window.geometry('400x300')
    center_window(patient_pw_window, 400, 300)

    patient_pw_window.configure(bg='#f0f8ff')

    title_label = Label(patient_pw_window, text="Patient Search Window", font=("Helvetica", 16, "bold"), bg='#f0f8ff')
    title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

    id_label = Label(patient_pw_window, text="Enter Appointment ID:", font=("Arial", 12), bg='#f0f8ff')
    id_label.grid(row=1, column=0, padx=10, pady=10)
    id_entry = Entry(patient_pw_window, font=("Arial", 12))
    id_entry.grid(row=1, column=1, padx=10, pady=10)


    def submit_login():
        appointment_id = id_entry.get()

        if not appointment_id:
            messagebox.showerror("Error", "Please enter Appointment ID.")
            return


        patient_pw_window.destroy()
        makesearchappointmentwindow(appointment_id)

    Button(patient_pw_window, text="Submit", font=("Arial", 12), pady=10, padx=20, relief=RAISED, bg='#d1e7dd'
           , command=submit_login).grid(row=3, column=0, columnspan=2, pady=20)


def passwordwindow(doctor_object):
    """This function creates a password window for the selected doctor."""
    password_window = Toplevel()
    password_window.title("Doctor Password")
    password_window.geometry('300x150')
    center_window(password_window, 300, 150)
    password_window.configure(bg='#f0f8ff')
    doctor = doctor_object.name
    password_label = Label(password_window, text=f"Enter Password for {doctor}:", font=("Helvetica", 12, "bold"), bg='#f0f8ff')
    password_label.grid(row=0, column=0, padx=10, pady=10)

    password_entry = Entry(password_window, show="*")
    password_entry.grid(row=1, column=0, padx=10, pady=10)

    def check_password():
        entered_password = password_entry.get()
        if check_doctor_password(doctor, entered_password):
            messagebox.showinfo("Access Granted", f"Password correct for {doctor}!")
            password_window.destroy()
            opendoctorwindow(doctor_object)
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Try again!")

    submit_button = Button(password_window, text="Submit", font=("Arial", 12), pady=10, padx=20, relief=RAISED, bg='#d1e7dd',
                           command=check_password)
    submit_button.grid(row=2, column=0, padx=10, pady=10)

    cancel_button = Button(password_window, text="Cancel", font=("Arial", 10), pady=5, padx=20, bg='#e9ecef',
                           command=password_window.destroy)
    cancel_button.grid(row=3, column=0, padx=10, pady=10)

def opendoctorwindow(doctor_object):
    doctorwindow = Toplevel()
    doctorwindow.title("Doctor's Dashboard")
    doctorwindow.geometry('320x540')
    center_window(doctorwindow, 320, 540)
    doctorwindow.configure(bg='#f0f8ff')
    doctor = doctor_object.name
    button_width = 25
    button_height = 2

    changestatusbutton = Button(doctorwindow, text='Change Status', font=("Arial", 12), width=button_width,
                                height=button_height,
                                relief=RAISED, bg='#d1e7dd', command=lambda: makechangestatuswindow(doctor_object))
    changestatusbutton.grid(row=0, column=0, pady=10, padx=10)

    viewpendingbutton = Button(doctorwindow, text='View Pending Appointments', font=("Arial", 12), width=button_width,
                               height=button_height,
                               relief=RAISED, bg='#ffdfba', command=lambda: view_pending_appointments(doctor_object))
    viewpendingbutton.grid(row=1, column=0, pady=10, padx=10)

    viewcancelledbutton = Button(doctorwindow, text='View Cancelled Appointments', font=("Arial", 12),
                                 width=button_width, height=button_height,
                                 relief=RAISED, bg='#ffccd5', command=lambda:view_cancelled_appointments(doctor_object))
    viewcancelledbutton.grid(row=2, column=0, pady=10, padx=10)

    viewapprovedbutton = Button(doctorwindow, text='View Approved Appointments', font=("Arial", 12), width=button_width,
                                height=button_height,
                                relief=RAISED, bg='#d1e7dd', command=lambda:view_approved_appointments(doctor_object))
    viewapprovedbutton.grid(row=3, column=0, pady=10, padx=10)

    viewcompletedbutton = Button(doctorwindow, text='View Completed Appointments', font=("Arial", 12),
                                 width=button_width, height=button_height,
                                 relief=RAISED, bg='#ffdfba', command=lambda:view_completed_appointments(doctor_object))
    viewcompletedbutton.grid(row=4, column=0, pady=10, padx=10)

    viewallbutton = Button(doctorwindow, text='View All Appointments', font=("Arial", 12), width=button_width,
                           height=button_height,
                           relief=RAISED, bg='#ffccd5', command=lambda:view_all_appointments(doctor_object))
    viewallbutton.grid(row=5, column=0, pady=10, padx=10)

    changepasswordbutton = Button(doctorwindow, text='Change Password', font=("Arial", 12), width=button_width,
                                height=button_height,
                                relief=RAISED, bg='#d1e7dd', command=lambda:makechangepasswordwindow(doctor_object))
    changepasswordbutton.grid(row=6, column=0, pady=10, padx=10)

    exit_button = Button(doctorwindow, text="Exit", font=("Arial", 10), width=6, height=1, bg='#e9ecef',
                         command=doctorwindow.destroy)
    exit_button.grid(row=7, column=0, pady=20)

def opendoctorselectionwindow():
    doctorselectionwindow = Toplevel()
    doctorselectionwindow.title("Doctor Selection")
    doctorselectionwindow.geometry('350x450')
    center_window(doctorselectionwindow, 350, 450)
    doctorselectionwindow.configure(bg='#f0f8ff')

    chooseDoctorlabel = Label(doctorselectionwindow, text='Select your Doctor', font=("Helvetica", 14, "bold"), bg='#f0f8ff')
    chooseDoctorlabel.grid(row=0, column=0, padx=100, pady=20)

    doctor_dict = load_doctor_dict()

    doctor_combobox = ttk.Combobox(doctorselectionwindow, value=list(doctor_dict.keys()), width=20)
    doctor_combobox.grid(row=1, column=0, pady=10)

    def submit_doctor():
        selected_doctor = doctor_combobox.get()
        if selected_doctor:
            doctor_object = DoctorManager(selected_doctor)
            passwordwindow(doctor_object)
        else:
            messagebox.showerror("Error", "Please select a doctor!")

    submit_button = Button(doctorselectionwindow, text="Submit", font=("Arial", 12), pady=10, padx=20,
                           relief=RAISED, bg='#d1e7dd', command=submit_doctor)
    submit_button.grid(row=2, column=0, pady=20)

    exit_button = Button(doctorselectionwindow, text="Cancel", font=("Arial", 10), pady=5, padx=20, bg='#e9ecef',
                         command=doctorselectionwindow.destroy)
    exit_button.grid(row=3, column=0, pady=10)


def makechangestatuswindow(doctor_object):
    changestatuswindow = Toplevel()
    changestatuswindow.title("Change Appointment Status")
    changestatuswindow.geometry('400x330')
    center_window(changestatuswindow, 400, 330)
    changestatuswindow.configure(bg='#f0f8ff')
    doctor = doctor_object.name
    doctor_label = Label(changestatuswindow, text=f"Selected Doctor: {doctor}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    status_label = Label(changestatuswindow, text="Select Status:", font=("Arial", 12), bg='#f0f8ff')
    status_label.pack(pady=5)
    status_combobox = ttk.Combobox(changestatuswindow, values=["Pending", "Approved"], font=("Arial", 10))
    status_combobox.pack(pady=5)

    appointment_label = Label(changestatuswindow, text="Select Appointment ID:", font=("Arial", 12), bg='#f0f8ff')
    appointment_label.pack(pady=5)
    appointment_combobox = ttk.Combobox(changestatuswindow, font=("Arial", 10))
    appointment_combobox.pack(pady=5)

    new_status_label = Label(changestatuswindow, text="Change Status To:", font=("Arial", 12), bg='#f0f8ff')
    new_status_label.pack(pady=5)
    new_status_combobox = ttk.Combobox(changestatuswindow, font=("Arial", 10))
    new_status_combobox.pack(pady=5)

    change_status_button = Button(changestatuswindow, text="Change Status", font=("Arial", 12), pady=10, padx=20,
                                  bg='#d1e7dd', relief=RAISED,
                                  command=lambda: on_status_change(doctor_object, appointment_combobox, new_status_combobox))
    change_status_button.pack(pady=20)

    status_combobox.bind("<<ComboboxSelected>>",
                         lambda event: on_doctor_status_selected(doctor_object, status_combobox, appointment_combobox, new_status_combobox))


def view_pending_appointments(doctor_object):
    pending_window = Toplevel()
    pending_window.geometry('400x500')
    center_window(pending_window, 400, 500)
    pending_window.title("Pending Appointments")
    pending_window.configure(bg='#f0f8ff')

    doctor_label = Label(pending_window, text=f"Selected Doctor: {doctor_object.name}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    appointments = doctor_object.view_appointments("Pending")

    if appointments:
        for appt in appointments:
            frame = Frame(pending_window, relief=RIDGE, borderwidth=2, bg='#ffffff')
            frame.pack(pady=5, padx=5, fill=X)
            Label(frame, text=f"Appointment ID: {appt['Appointment ID']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Patient Name: {appt['Patient Name']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Date: {appt['Date']}/{appt['Month']}/{appt['Year']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Timeslot: {appt['Timeslot']}", font=("Arial", 12), bg='#ffffff').pack()
    else:
        Label(pending_window, text="No pending appointments", font=("Arial", 12), bg='#f0f8ff').pack(pady=10)


def view_cancelled_appointments(doctor_object):
    cancelled_window = Toplevel()
    cancelled_window.geometry('400x500')
    center_window(cancelled_window, 400, 500)
    cancelled_window.title("Cancelled Appointments")
    cancelled_window.configure(bg='#f0f8ff')

    doctor_label = Label(cancelled_window, text=f"Selected Doctor: {doctor_object.name}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    appointments = doctor_object.view_appointments("Cancelled")

    if appointments:
        for appt in appointments:
            frame = Frame(cancelled_window, relief=RIDGE, borderwidth=2, bg='#ffffff')
            frame.pack(pady=5, padx=5, fill=X)
            Label(frame, text=f"Appointment ID: {appt['Appointment ID']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Patient Name: {appt['Patient Name']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Date: {appt['Date']}/{appt['Month']}/{appt['Year']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Timeslot: {appt['Timeslot']}", font=("Arial", 12), bg='#ffffff').pack()
    else:
        Label(cancelled_window, text="No cancelled appointments", font=("Arial", 12), bg='#f0f8ff').pack(pady=10)


def view_approved_appointments(doctor_object):

    approved_window = Toplevel()
    approved_window.geometry('400x500')
    center_window(approved_window, 400, 500)
    approved_window.title("Approved Appointments")
    approved_window.configure(bg='#f0f8ff')

    doctor_label = Label(approved_window, text=f"Selected Doctor: {doctor_object.name}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    appointments = doctor_object.view_appointments("Approved")

    if appointments:
        for appt in appointments:
            frame = Frame(approved_window, relief=RIDGE, borderwidth=2, bg='#ffffff')
            frame.pack(pady=5, padx=5, fill=X)
            Label(frame, text=f"Appointment ID: {appt['Appointment ID']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Patient Name: {appt['Patient Name']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Date: {appt['Date']}/{appt['Month']}/{appt['Year']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Timeslot: {appt['Timeslot']}", font=("Arial", 12), bg='#ffffff').pack()
    else:
        Label(approved_window, text="No approved appointments", font=("Arial", 12), bg='#f0f8ff').pack(pady=10)

def view_completed_appointments(doctor_object):

    completed_window = Toplevel()
    completed_window.geometry('400x500')
    center_window(completed_window, 400, 500)
    completed_window.title("Completed Appointments")
    completed_window.configure(bg='#f0f8ff')  # Consistent background color

    doctor_label = Label(completed_window, text=f"Selected Doctor: {doctor_object.name}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    appointments = doctor_object.view_appointments("Completed")

    if appointments:
        for appt in appointments:
            frame = Frame(completed_window, relief=RIDGE, borderwidth=2, bg='#ffffff')
            frame.pack(pady=5, padx=5, fill=X)
            Label(frame, text=f"Appointment ID: {appt['Appointment ID']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Patient Name: {appt['Patient Name']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Date: {appt['Date']}/{appt['Month']}/{appt['Year']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Timeslot: {appt['Timeslot']}", font=("Arial", 12), bg='#ffffff').pack()
    else:
        Label(completed_window, text="No completed appointments", font=("Arial", 12), bg='#f0f8ff').pack(pady=10)

def view_all_appointments(doctor_object):

    all_window = Toplevel()
    all_window.geometry('400x500')
    center_window(all_window, 400, 500)
    all_window.title("All Appointments")
    all_window.configure(bg='#f0f8ff')  # Consistent background color

    doctor_label = Label(all_window, text=f"Selected Doctor: {doctor_object.name}",
                         font=("Helvetica", 14), bg='#f0f8ff')
    doctor_label.pack(pady=10)

    appointments = doctor_object.view_appointments()

    if appointments:
        for appt in appointments:
            frame = Frame(all_window, relief=RIDGE, borderwidth=2, bg='#ffffff')
            frame.pack(pady=5, padx=5, fill=X)
            Label(frame, text=f"Appointment ID: {appt['Appointment ID']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Patient Name: {appt['Patient Name']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Date: {appt['Date']}/{appt['Month']}/{appt['Year']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Timeslot: {appt['Timeslot']}", font=("Arial", 12), bg='#ffffff').pack()
            Label(frame, text=f"Status: {appt['Status']}", font=("Arial", 12), bg='#ffffff').pack()
    else:
        Label(all_window, text="No appointments found", font=("Arial", 12), bg='#f0f8ff').pack(pady=10)





def makechangepasswordwindow(doctor_object):
    mydoctor = doctor_object.name
    changepasswordwindow = Toplevel()
    password_dict = load_password_dict()
    changepasswordwindow.geometry('350x150')
    center_window(changepasswordwindow, 350, 150)
    changepasswordwindow.configure(bg='#f0f8ff')

    password_label = Label(changepasswordwindow, text=f"Enter New Password for Doctor {mydoctor}:", font=("Arial", 12), bg='#f0f8ff')
    password_label.grid(row=0, column=0, padx=10, pady=10)

    password_entry = Entry(changepasswordwindow)
    password_entry.grid(row=1, column=0, padx=10, pady=10)

    def updatepassword():
        try:
            tentative_password = password_entry.get()
            if tentative_password == '':
                raise ValueError('Enter a proper password')

            password_dict[mydoctor] = tentative_password
            save_password_dict(password_dict)
            messagebox.showinfo('Success', 'Password has been updated.')

        except ValueError as ve:
            messagebox.showerror('Error', str(ve))

        except Exception as e:
            messagebox.showerror('Error', f"An unexpected error occurred: {str(e)}")


    submit_button = Button(changepasswordwindow, text="Submit", font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                           bg='#e9ecef', command=updatepassword)
    submit_button.grid(row=2, column=0, padx=10, pady=10)


def adminpasswordwindow():
    password_window = Toplevel()
    password_window.geometry('300x150')
    center_window(password_window, 300, 150)
    password_window.configure(bg='#f0f8ff')

    password_label = Label(password_window, text="Enter Admin Password:", font=("Arial", 12), bg='#f0f8ff')
    password_label.grid(row=0, column=0, padx=10, pady=10)

    password_entry = Entry(password_window, show="*")
    password_entry.grid(row=1, column=0, padx=10, pady=10)

    def check_password():
        entered_password = password_entry.get()
        correct_password = load_admin_password()

        if entered_password == correct_password:
            messagebox.showinfo("Access Granted", "Password correct!")
            password_window.destroy()
            openadminwindow()
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Try again!")

    submit_button = Button(password_window, text="Submit", font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                           bg='#e9ecef', command=check_password)
    submit_button.grid(row=2, column=0, padx=10, pady=10)

def openadminwindow():
    admin_window = Toplevel()
    admin_window.geometry('280x400')
    center_window(admin_window, 280, 400)
    admin_window.configure(bg='#f0f8ff')

    adddoctor_button = Button(admin_window, text='Add a Doctor', font=("Arial", 12), pady=20, padx=20, relief=RAISED,
                              bg='#d1e7dd', command=makeadddoctorwindow)
    adddoctor_button.grid(row=1, column=0, padx=20, pady=20)

    removedoctor_button = Button(admin_window, text='Remove Doctor', font=("Arial", 12), pady=20, padx=20, relief=RAISED,
                                 bg='#ffdfba', command=makeremovedoctorwindow)
    removedoctor_button.grid(row=2, column=0, padx=20, pady=20)

    changeadminpwwindowbutton = Button(admin_window, text='Change Admin Password', font=("Arial", 12), pady=20, padx=20,
                                 relief=RAISED,
                                 bg='#ffccd5', command=makechangeadminpwwindow)
    changeadminpwwindowbutton.grid(row=3, column=0, padx=20, pady=20)


def makeadddoctorwindow():
    temp_new_doc = ''
    adddoctorwindow = Toplevel()
    adddoctorwindow.geometry('400x500')
    center_window(adddoctorwindow, 400, 500)
    adddoctorwindow.title("Add Doctor")
    adddoctorwindow.configure(bg='#f0f8ff')

    label1 = Label(adddoctorwindow, text='Doctor Name', font=("Arial", 12), bg='#f0f8ff')
    label1.grid(row=0, column=0, padx=10, pady=10)

    text_box1 = Text(adddoctorwindow, height=1, width=15)
    text_box1.grid(row=0, column=1, padx=10, pady=10)

    label3 = Label(adddoctorwindow, text='Doctor Password', font=("Arial", 12), bg='#f0f8ff')
    label3.grid(row=1, column=0, padx=10, pady=10)

    password_entry = Text(adddoctorwindow, height=1, width=15)
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    def submit_doctor():
        nonlocal temp_new_doc
        password_dict = load_password_dict()
        new_doctor = text_box1.get("1.0", "end-1c").strip()
        password = password_entry.get("1.0", "end-1c").strip()

        if new_doctor and password:
            temp_new_doc = new_doctor
            password_dict[new_doctor] = password
            save_password_dict(password_dict)
            messagebox.showinfo("Info", f"Doctor name '{new_doctor}' and password accepted.")
        else:
            messagebox.showwarning("Warning", "Doctor name and password cannot be empty.")

    submit_button = Button(adddoctorwindow, text='Add Doctor', font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                           bg='#d1e7dd', command=submit_doctor)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    label2 = Label(adddoctorwindow, text='Add Date and Timeslots (e.g., 0@1:00pm;1@2:00pm,4:00pm):',
                   font=("Arial", 10), bg='#f0f8ff')
    label2.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    text_box2 = Text(adddoctorwindow, height=5, width=30)
    text_box2.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def submittimeslots():
        nonlocal temp_new_doc
        input_str = text_box2.get("1.0", "end-1c")
        result_dict = {}
        entries = input_str.split(';')

        for entry in entries:
            try:
                key, times = entry.split('@')
                key = int(key)

                if key < 0 or key > 6:
                    raise ValueError("Day index must be between 0 and 6.")

                time_slots = set(times.split(','))
                if not time_slots:
                    raise ValueError("At least one time slot must be provided.")

                result_dict[key] = time_slots

            except ValueError as e:
                print(f"Error: {e}")

        doctor_dict = load_doctor_dict()
        password_dict = load_password_dict()
        doctor_dict[temp_new_doc] = result_dict
        save_doctor_dict(doctor_dict)
        save_password_dict(password_dict)
        text_box1.delete("1.0", END)
        password_entry.delete("1.0", END)
        text_box2.delete("1.0", END)
        messagebox.showinfo('Info', 'Doctor Added: ' + temp_new_doc)

    submit_button1 = Button(adddoctorwindow, text='Submit Timeslots', font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                            bg='#ffdfba', command=submittimeslots)
    submit_button1.grid(row=5, column=0, columnspan=2, pady=10)


def makeremovedoctorwindow():
    removedoctorwindow = Toplevel()
    removedoctorwindow.geometry('310x250')
    center_window(removedoctorwindow, 310, 250)
    removedoctorwindow.configure(bg='#f0f8ff')

    chooseDoctorlabel = Label(removedoctorwindow, text='Choose Doctor', font=("Arial", 12), bg='#f0f8ff')
    chooseDoctorlabel.grid(row=0, column=0, padx=100, pady=10)

    doctor_dict = load_doctor_dict()
    password_dict = load_password_dict()
    available_doctors_combobox = ttk.Combobox(removedoctorwindow, value=list(doctor_dict.keys()), width=20)
    available_doctors_combobox.grid(row=1, column=0, padx=10, pady=10)
    available_doctors_combobox.current(0)

    def remove_doctor():
        a = available_doctors_combobox.get()
        del doctor_dict[a]
        del password_dict[a]
        save_doctor_dict(doctor_dict)
        save_password_dict(password_dict)
        messagebox.showinfo('Info', 'Doctor: ' + a + ' has been removed')

    submit_button = Button(removedoctorwindow, text='Remove Doctor', font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                           bg='#ffccd5', command=remove_doctor)
    submit_button.grid(row=2, column=0, columnspan=2, pady=20)

def makechangeadminpwwindow():
    changeadminpasswordwindow = Toplevel()
    admin_correct_password = load_admin_password()
    changeadminpasswordwindow.geometry('300x150')
    center_window(changeadminpasswordwindow, 300, 150)
    changeadminpasswordwindow.configure(bg='#f0f8ff')

    password_label = Label(changeadminpasswordwindow, text="Enter New Password:", font=("Arial", 12), bg='#f0f8ff')
    password_label.grid(row=0, column=0, padx=10, pady=10)

    password_entry = Entry(changeadminpasswordwindow)
    password_entry.grid(row=1, column=0, padx=10, pady=10)

    def updatepassword():
        try:
            tentative_password = password_entry.get()
            if tentative_password == '':
                raise ValueError('Enter a proper password')

            save_admin_password(tentative_password)
            messagebox.showinfo('Success', 'Password has been updated.')

        except ValueError as ve:
            messagebox.showerror('Error', str(ve))

        except Exception as e:
            messagebox.showerror('Error', f"An unexpected error occurred: {str(e)}")

    submit_button = Button(changeadminpasswordwindow, text="Submit", font=("Arial", 10), pady=5, padx=20, relief=RAISED,
                           bg='#e9ecef', command=updatepassword)
    submit_button.grid(row=2, column=0, padx=10, pady=10)