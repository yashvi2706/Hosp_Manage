import csv
import os

def save_initial_admin_password():
    with open('admin_password.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['admin', 'admin123'])
        print("Initial admin password saved.")

def save_admin_password(new_password):
    with open('admin_password.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['admin', new_password])
    print("Admin password updated.")

def load_admin_password():
    if os.path.exists('admin_password.csv'):
        with open('admin_password.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'admin':
                    return row[1]
    else:
        print("Admin password file not found.")
        return None

def save_password_dict(password_dict):
    try:
        print('password_dict updated')
        with open('password_dict.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Doctor', 'Password'])
            for doctor, password in password_dict.items():
                writer.writerow([doctor, password])
    except Exception as e:
        print(f"Error saving password_dict to CSV: {e}")

def save_initial_password_dict():
    print("Saving initial password dictionary...")
    password_dict = {
        'Dr.Sarathi': 'password_sarathi',
        'Dr.Taggar': 'password_taggar',
        'Dr.Jakhi': 'password_jakhi',
        'Dr.Kapoor': 'password_kapoor'
    }
    save_password_dict(password_dict)


def load_password_dict():
    password_dict = {}
    try:
        with open('password_dict.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                doctor = row['Doctor']
                password = row['Password']
                password_dict[doctor] = password
    except FileNotFoundError:
        print("Password CSV file not found. Returning empty dictionary.")
        return {}
    except Exception as e:
        print(f"Error loading password_dict from CSV: {e}")
    return password_dict

def check_doctor_password(doctor, entered_password):
    password_dict=load_password_dict()
    correct_password = password_dict.get(doctor)
    return entered_password == correct_password
def save_doctor_dict(doctor_dict):
    try:
        print('modified doctor_dict saved')
        with open('doctor_dict.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Doctor', 'Day', 'Times'])
            for doctor, schedule in doctor_dict.items():
                for day, times in schedule.items():
                    writer.writerow([doctor, day, ','.join(times)])
    except Exception as e:
        print(f"Error saving doctor_dict to CSV: {e}")

def save_initial_doctor_dict():
    print("Saving initial doctor dictionary...")
    doctor_dict = {
        'Dr.Sarathi': {0: ['1:00pm-2:00pm', '2:00pm-3:00pm'], 2: ['10:00am-11:00am', '3:00pm-4:00pm', '5:00pm-6:00pm']},
        'Dr.Taggar': {3: ['2:00pm-3:00pm'], 5: ['10:00am-11:00am', '5:00pm-6:00pm']},
        'Dr.Jakhi': {2: ['1:00pm-2:00pm', '2:00pm-3:00pm'], 6: ['11:00am-12:00am', '4:00pm-5:00pm']},
        'Dr.Kapoor': {1: ['1:00pm-2:00pm'], 4: ['10:00am-11:00am', '5:00pm-6:00pm']}
    }
    save_doctor_dict(doctor_dict)

def load_doctor_dict():
    doctor_dict = {}
    try:
        with open('doctor_dict.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                doctor = row['Doctor']
                day = int(row['Day'])
                times = row['Times'].split(',')

                if doctor not in doctor_dict:
                    doctor_dict[doctor] = {}

                doctor_dict[doctor][day] = times
    except FileNotFoundError:
        print("CSV file not found. Returning empty dictionary.")
        return {}
    except Exception as e:
        print(f"Error loading doctor_dict from CSV: {e}")
    return doctor_dict
