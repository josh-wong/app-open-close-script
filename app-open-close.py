import os
import time

for i in range(1):
    # Open Command Prompt, then open the app by using its URI.
    os.system("start /wait cmd /c start "" <INSERT APP URI>")
    # Wait XX seconds before closing the app.
    time.sleep(XX)
    # Close the app.
    os.system("TASKKILL /F /IM <INSERT APP NAME>.exe")
    # Indicate that the process was a success.
    print(f"Success! <INSERT DETAILED MESSAGE ABOUT WHY THIS APP WAS OPENED AND CLOSED>.")
    # Wait 10 seconds before closing the Python program.
    time.sleep(10)
    # Close the Python program.
    exit()