import tkinter as tk
from tkinter import simpledialog
import hashlib
import os
import time

def log_attempt(success):
    with open(LOG_FILE, "a") as f:
        if success:
            f.write("SUCCESS LOGIN\n")
        else:
            f.write("FAILED LOGIN\n")
# ---------- CONFIG ----------
SALT = "X9@!locker"
PASSWORD_FILE = "password.txt"

# ---------- DATA ----------
FULL_REAL_DATA = """Account Holder : Jyothsna
ATM PIN        : 4589
Email Password : jyothsna@123
Balance        : ₹50,000
Phone          : 9XXXXXXXXX
Address        : Andhra Pradesh
"""

LIMITED_DECOY_DATA = """Account Holder : Jyothsna
ATM PIN        : 1245
Email Password : jyothsna_mail@456
Balance        : ₹12,000
"""

# ---------- FUNCTIONS ----------
if hash_password(pwd) == stored_hash:
    output_box.insert(tk.END, FULL_REAL_DATA)
    log_attempt(True)
else:
    output_box.insert(tk.END, LIMITED_DECOY_DATA)
    log_attempt(False)
def access_locker():
    pwd = password_entry.get()
    password_entry.delete(0, tk.END)

    time.sleep(0.5)  # same delay

    with open(PASSWORD_FILE, "r") as f:
        stored_hash = f.read()

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)

    if hash_password(pwd) == stored_hash:
        output_box.insert(tk.END, FULL_REAL_DATA)
    else:
        output_box.insert(tk.END, LIMITED_DECOY_DATA)

    output_box.config(state="disabled")

# ---------- FIRST RUN ----------
if not os.path.exists(PASSWORD_FILE):
    root = tk.Tk()
    root.withdraw()
    setup_password()
    root.destroy()

# ---------- GUI ----------
app = tk.Tk()
app.title("Secure Digital Locker")
app.geometry("420x350")
app.resizable(False, False)

tk.Label(app, text="🔐 Secure Digital Locker", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(app, text="Enter Password:").pack()
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(app, text="Access Locker", command=access_locker).pack(pady=10)

output_box = tk.Text(app, height=10, width=45, state="disabled")
output_box.pack(pady=10)

app.mainloop()
