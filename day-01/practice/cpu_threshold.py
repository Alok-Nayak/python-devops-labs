# Take CPU threshold as input from user and print it
# Find current CPU usage and compare it with the threshold. If current CPU usage is greater than threshold, print a warning message.
# And email the warning message to the user. (You can use smtplib module to send email)

import psutil

def get_cpu_threshold():
    user_input = input("Please enter the CPU threshold (in percentage): ")
    current_cpu_usage = psutil.cpu_percent(interval=1)
    if current_cpu_usage > float(user_input):
        print(f"Warning: Current CPU usage is {current_cpu_usage}%, which is above the threshold of {user_input}%.")
        print("Sending email to the user...")
    else:
        print(f"Current CPU usage is {current_cpu_usage}%, which is below the threshold of {user_input}%.")

def memory_threshold():
    user_input = input("Please enter the Memory threshold (in percentage): ")
    current_memory_usage = psutil.virtual_memory().percent
    if current_memory_usage > float(user_input):
        print(f"Warning: Current Memory usage is {current_memory_usage}%, which is above the threshold of {user_input}%.")
        print("Sending email to the user...")
    else:
        print(f"Current Memory usage is {current_memory_usage}%, which is below the threshold of {user_input}%.")
        print("Sending email to the user...")
        
def disk_threshold():
    user_input = input("Please enter the Disk threshold (in percentage): ")
    current_disk_usage = psutil.disk_usage('/').percent
    if current_disk_usage > float(user_input):
        print(f"Warning: Current Disk usage is {current_disk_usage}%, which is above the threshold of {user_input}%.")
        print("Sending email to the user...")
    else:
        print(f"Current Disk usage is {current_disk_usage}%, which is below the threshold of {user_input}%.")

get_cpu_threshold()
memory_threshold()
disk_threshold()
