import tkinter as tk
from tkinter import messagebox
import pandas as pd
import time
import logging
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simple reversible encoding for demonstration purposes
def encode_data(data):
    return ''.join(chr(ord(char) + 3) for char in data)

def decode_data(data):
    return ''.join(chr(ord(char) - 3) for char in data)

# Initialize global variables
mouse_movements = []
key_press_times = []
users_data = []
behavior_data_list = []
user_id_counter = 1  # Initialize a counter for user IDs
session_start_time = None

# Function to track mouse movement
def track_mouse(event):
    mouse_movements.append((event.x, event.y, time.time()))

# Function to track key press
def track_key(event):
    key_press_times.append(time.time())

# Function to calculate cursor speed
def calculate_cursor_speed():
    speeds = []
    for i in range(1, len(mouse_movements)):
        x1, y1, t1 = mouse_movements[i - 1]
        x2, y2, t2 = mouse_movements[i]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        time_diff = t2 - t1
        if time_diff > 0:
            speeds.append(distance / time_diff)
    return sum(speeds) / len(speeds) if speeds else 0

# Function to calculate typing speed
def calculate_typing_speed():
    if len(key_press_times) < 2:
        return 0
    total_time = key_press_times[-1] - key_press_times[0]
    return len(key_press_times) / total_time if total_time > 0 else 0

# Enhanced the app to include more behavior metrics, session tracking, and export functionality for machine learning datasets

def save_user_data(name, email, phone, age, address):
    global user_id_counter

    # Ensure unique ID for behavior data
    try:
        existing_ids = set()
        with open('behavior_data.csv', 'r') as file:
            for line in file:
                try:
                    row = line.strip().split(',')
                    if len(row) >= 1:  # Ensure the row has at least one column
                        existing_ids.add(int(row[0]))
                except ValueError:
                    logging.warning(f"Skipping invalid row in behavior_data.csv: {line.strip()}")
    except FileNotFoundError:
        logging.warning("behavior_data.csv not found. Proceeding with an empty ID set.")

    while user_id_counter in existing_ids:
        user_id_counter += 1

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    session_duration = end_session_timer()  # Calculate session duration

    user_data = {
        'ID': user_id_counter,
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Age': age,
        'Address': address,
        'Timestamp': current_time
    }

    cursor_speed = calculate_cursor_speed()
    typing_speed = calculate_typing_speed()
    is_human = cursor_speed > 0 and typing_speed > 0.5  # Example heuristic

    behavior_data = {
        'ID': user_id_counter,
        'Name': name,
        'Cursor Speed': cursor_speed,
        'Typing Speed': typing_speed,
        'Mouse Clicks': len(mouse_movements),
        'Key Presses': len(key_press_times),
        'Session Duration': session_duration,
        'Human or Robot': 'Human' if is_human else 'Robot',
        'Timestamp': current_time
    }

    users_data.append(user_data)
    behavior_data_list.append(behavior_data)

    # Increment user ID for the next user
    user_id_counter += 1

    mouse_movements.clear()
    key_press_times.clear()

    logging.info("User data saved successfully with enhanced behavior tracking")

# Add session timer
def start_session_timer():
    global session_start_time
    session_start_time = time.time()

def end_session_timer():
    session_duration = time.time() - session_start_time
    logging.info(f"Session duration: {session_duration:.2f} seconds")
    return session_duration

# Start the session timer
start_session_timer()

# Updated save_all_data to include history saving
def save_all_data():
    # Save user data to CSV, Excel, and JSON
    df_users = pd.DataFrame(users_data)
    df_users.to_csv('user_data.csv', index=False, mode='a', header=False)
    with pd.ExcelWriter('user_data.xlsx', mode='a', if_sheet_exists='overlay') as writer:
        df_users.to_excel(writer, index=False, sheet_name='Sheet1', header=False)
    df_users.to_json('user_data.json', orient='records', indent=4)

    # Save behavior data to CSV, Excel, and JSON
    df_behavior = pd.DataFrame(behavior_data_list)
    df_behavior.to_csv('behavior_data.csv', index=False, mode='a', header=False)
    with pd.ExcelWriter('behavior_data.xlsx', mode='a', if_sheet_exists='overlay') as writer:
        df_behavior.to_excel(writer, index=False, sheet_name='Sheet1', header=False)
    df_behavior.to_json('behavior_data.json', orient='records', indent=4)

    # Generate a comparison report
    comparison_report = "\n".join([
        f"| ID: {data['ID']:<5} | Name: {data['Name']:<20} | Cursor Speed: {data['Cursor Speed']:<10.2f} | Typing Speed: {data['Typing Speed']:<10.2f} | Human or Robot: {data['Human or Robot']:<10} | Timestamp: {data['Timestamp']} |"
        for data in behavior_data_list
    ])

    with open('comparison_report.txt', 'a') as report_file:
        report_file.write("+-----+----------------------+------------+------------+--------------+-------------------+\n")
        report_file.write("| ID  | Name                 | Cursor Speed | Typing Speed | Human or Robot | Timestamp         |\n")
        report_file.write("+-----+----------------------+------------+------------+--------------+-------------------+\n")
        report_file.write(comparison_report)
        report_file.write("\n+-----+----------------------+------------+------------+--------------+-------------------+")

    logging.info("All data and comparison report saved successfully")
    messagebox.showinfo("Success", "All data and comparison report saved successfully!")

# Function to export dataset for machine learning

def export_dataset():
    df_behavior = pd.DataFrame(behavior_data_list)
    df_behavior.to_csv('ml_behavior_dataset.csv', index=False)
    logging.info("Dataset exported successfully for machine learning")

# Create the main application window
root = tk.Tk()
root.title("User Details Form")

# Variables to store user input
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
age_var = tk.StringVar()
address_var = tk.StringVar()

# Create form labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=email_var).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=phone_var).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=age_var).grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Address:").grid(row=4, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=address_var).grid(row=4, column=1, padx=10, pady=10)

# Create buttons
tk.Button(root, text="Save User", command=lambda: save_user_data(name_var.get(), email_var.get(), phone_var.get(), age_var.get(), address_var.get())).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save All Data", command=save_all_data).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Export Dataset", command=export_dataset).grid(row=7, column=0, columnspan=2, pady=10)

# Bind mouse and keyboard events
root.bind('<Motion>', track_mouse)
root.bind('<KeyPress>', track_key)

# Run the application
root.mainloop()