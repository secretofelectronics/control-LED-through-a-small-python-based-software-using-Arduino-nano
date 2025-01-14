import tkinter as tk
from tkinter import messagebox
import serial
import time

# Initialize the serial connection
try:
    arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port
    time.sleep(2)  # Wait for the connection to establish
except serial.SerialException:
    arduino = None
    messagebox.showerror("Error", "Arduino not found. Check the COM port and connection.")

# Functions to control the LED
def turn_on():
    if arduino:
        arduino.write(b"ON\n")
    else:
        messagebox.showerror("Error", "Arduino not connected!")

def turn_off():
    if arduino:
        arduino.write(b"OFF\n")
    else:
        messagebox.showerror("Error", "Arduino not connected!")

# Create the main window
app = tk.Tk()
app.title("LED Controller")
app.geometry("400x300")
app.configure(bg="#1e1e1e")  # Dark gray background

# Add a title label
title = tk.Label(
    app,
    text="LED Controller",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e1e",
    fg="#ffffff"  # White text
)
title.pack(pady=20)

# Add control buttons
on_button = tk.Button(
    app,
    text="Turn On",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",  # Green button
    fg="#ffffff",  # White text
    activebackground="#388E3C",  # Darker green when clicked
    activeforeground="#ffffff",  # White text when clicked
    relief="flat",  # Flat modern look
    command=turn_on
)
on_button.pack(pady=10, ipadx=10, ipady=5)

off_button = tk.Button(
    app,
    text="Turn Off",
    font=("Helvetica", 14, "bold"),
    bg="#F44336",  # Red button
    fg="#ffffff",  # White text
    activebackground="#D32F2F",  # Darker red when clicked
    activeforeground="#ffffff",  # White text when clicked
    relief="flat",  # Flat modern look
    command=turn_off
)
off_button.pack(pady=10, ipadx=10, ipady=5)

# Add an exit button
exit_button = tk.Button(
    app,
    text="Exit",
    font=("Helvetica", 14, "bold"),
    bg="#607D8B",  # Blue-gray button
    fg="#ffffff",  # White text
    activebackground="#455A64",  # Darker blue-gray when clicked
    activeforeground="#ffffff",  # White text when clicked
    relief="flat",  # Flat modern look
    command=app.quit
)
exit_button.pack(pady=10, ipadx=10, ipady=5)

# Run the app
app.mainloop()

# Close the serial connection when done
if arduino:
    arduino.close()
