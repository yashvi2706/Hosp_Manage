from file_manager import *
from ui import HOMEUI

if not os.path.exists('admin_password.csv'):
    print("Admin Password CSV file not found. Creating the initial password_dict CSV...")
    save_initial_admin_password()

if not os.path.exists('password_dict.csv'):
    print("Password CSV file not found. Creating the initial password_dict CSV...")
    save_initial_password_dict()

if not os.path.exists('doctor_dict.csv'):
    print("CSV file not found. Creating the initial doctor_dict CSV...")
    save_initial_doctor_dict()

HOMEUI()
