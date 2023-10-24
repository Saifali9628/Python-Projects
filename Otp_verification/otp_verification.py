import random
import smtplib
import tkinter as tk
from tkinter import messagebox

def send_otp(receiver_email):
    sender_email = "test@gmail.com"
    sender_password = "ajkfjsjadjdlk"

    subject = "OTP Verification"
    otp = str(random.randint(100000, 999999))
    message = f"Subject: {subject}\n\nYour OTP is: {otp}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Replace with your SMTP server details
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print("OTP sent successfully!")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        server.quit()
    
    return otp

def verify_otp():
    user_input = otp_entry.get()
    if user_input == otp:
        messagebox.showinfo("OTP Verification", "OTP Verified!")
    else:
        messagebox.showerror("OTP Verification", "Invalid OTP. Verification failed.")

def send_otp_and_change_ui():
    receiver_email = email_entry.get()
    global otp
    otp = send_otp(receiver_email)
    
    email_label.destroy()
    email_entry.destroy()
    send_otp_button.destroy()

    otp_label = tk.Label(window, text="Enter the OTP you received:")
    otp_label.pack(pady=10)

    otp_entry.pack(pady=5)
    verify_button.pack(pady=10)

window = tk.Tk()
window.title("OTP Verification")

email_label = tk.Label(window, text="Enter your email:")
email_label.pack(pady=10)

email_entry = tk.Entry(window)
email_entry.pack(pady=5)

send_otp_button = tk.Button(window, text="Send OTP", command=send_otp_and_change_ui, bg="blue", fg="white")
send_otp_button.pack(pady=10)

otp_entry = tk.Entry(window)
verify_button = tk.Button(window, text="Verify OTP", command=verify_otp, bg="blue", fg="white")

window.mainloop()
