import tkinter as tk
import customtkinter as ctk
import pyotp

# Lists to store previous OTP codes and keys
previous_codes = []
previous_keys = []

def generate_totp():
    user_otp = entry.get()
    totp = pyotp.TOTP(user_otp)
    current_code = totp.now()
    result_label.configure(text=f"Current code: {current_code}")
    previous_codes.append(current_code)
    previous_keys.append(user_otp)

def generate_hotp():
    user_otp = entry.get()
    custom = entry_custom.get()
    try:
        custom = float(custom)
    except ValueError:
        custom = 0
    hotp = pyotp.HOTP(user_otp)
    current_code = hotp.at(custom)
    result_label.configure(text=f"Current code: {current_code}")
    previous_codes.append(current_code)
    previous_keys.append(user_otp)

def show_difference():
    difference_text = """
    TOTP (Time-Based One-Time Password) is generated based on the current time.
    HOTP (HMAC-Based One-Time Password) is generated based on a counter.
    TOTP Is much more common and is used for most applications.
    """
    result_label.configure(text=difference_text)

def show_previous_entries():
    previous_entries_text = "Previous OTP Codes and Keys:\n"
    for code, key in zip(previous_codes, previous_keys):
        previous_entries_text += f"Code: {code}, Key: {key}\n"
    result_label.configure(text=previous_entries_text)

root = ctk.CTk()
root.geometry("400x500")
root.title("Stellar Escape OTP 2FA Auth")

entry_label = ctk.CTkLabel(root, text="Enter OTP key:")
entry_label.pack(pady=10)
entry = ctk.CTkEntry(root)
entry.pack()

custom_label = ctk.CTkLabel(root, text="Custom counter (used for HOTP):")
custom_label.pack()
entry_custom = ctk.CTkEntry(root)
entry_custom.pack(pady=10)

totp_button = ctk.CTkButton(root, text="Generate TOTP", command=generate_totp)
totp_button.pack(pady=10)

hotp_button = ctk.CTkButton(root, text="Generate HOTP", command=generate_hotp)
hotp_button.pack()

difference_button = ctk.CTkButton(root, text="What's the difference?", command=show_difference)
difference_button.pack(pady=10)

previous_entries_button = ctk.CTkButton(root, text="Show Previous Entries", command=show_previous_entries)
previous_entries_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", wraplength=350)
result_label.pack(pady=10)

root.mainloop()
