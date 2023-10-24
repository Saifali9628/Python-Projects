import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten the URL
def shorten_url():
    long_url = entry_long_url.get()
    if long_url:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        entry_short_url.delete(0, tk.END)
        entry_short_url.insert(0, short_url)
    else:
        messagebox.showwarning("Warning", "Please enter a URL to shorten.")

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Labels and Entry widgets
label_long_url = tk.Label(root, text="Enter Long URL:")
label_long_url.pack(padx=10, pady=10, anchor='w')

entry_long_url = tk.Entry(root, width=50)
entry_long_url.pack(padx=10, pady=5)

label_short_url = tk.Label(root, text="Shortened URL:")
label_short_url.pack(padx=10, pady=10, anchor='w')

entry_short_url = tk.Entry(root, width=50)
entry_short_url.pack(padx=10, pady=5)

# Shorten button
button_shorten = tk.Button(root, text="Shorten", command=shorten_url, bg="blue", font=("Arial", 14))
button_shorten.pack(padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
