import datetime
import time
import os
import subprocess

notification_time = str(input("Input time of notification (DD/MM/YY HOUR:MINUTE:SECOND):"))
print(notification_time)
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")
print(formatted_time)
#This program is currently only available on MacOS
if os.name == 'posix':
    def run_command(command):
        try:
            # Run the command and capture the output and errors
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
        
            # Check if the command ran successfully
            if result.returncode == 0:
                print("Command executed successfully.")
                print(result.stdout)
            else:
                print("Error executing command:")
                print(result.stderr)
    
        except Exception as e:
            print(f"An error occurred: {e}")

    if __name__ == "__main__":
        message_title = input("Message title: ")
        message_body = input("Message: ")

        command = f"""osascript -e 'display notification "{message_body}" with title "{message_title}"'"""

        while True:
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")

            if formatted_time == notification_time:
                run_command(command)
                break

            time.sleep(1)
if os.name == 'nt':
    print("Sorry, this program is not supported on Windows.")
