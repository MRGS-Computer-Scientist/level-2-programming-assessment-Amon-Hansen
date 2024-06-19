import tkinter as tk
from tkinter import messagebox

# Function to handle button click events
def select_sport(sport):
    messagebox.showinfo("Selection", f"You selected {sport}")

# Create the main window
root = tk.Tk()
root.title("Sportify - Sports Career Selection")
root.geometry("800x600")
root.configure(bg='#f9f9f9')

# Create a frame for the header
header_frame = tk.Frame(root, bg='white')
header_frame.pack(fill='x')

# Add the title and navigation buttons to the header
title_label = tk.Label(header_frame, text="Sportify", font=("Arial", 24), bg='white')
title_label.pack(side='left', padx=10, pady=10)

nav_frame = tk.Frame(header_frame, bg='white')
nav_frame.pack(side='right')

for text in ["Sports", "About", "Help", "Login"]:
    nav_button = tk.Button(nav_frame, text=text, font=("Arial", 12), bg='white', relief='flat')
    nav_button.pack(side='left', padx=5)

# Create the main content frame
main_frame = tk.Frame(root, bg='#f9f9f9')
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Add the main title
main_title = tk.Label(main_frame, text="Sports Career Selection", font=("Arial", 20), bg='#f9f9f9')
main_title.pack(pady=10)

# Create a frame for the sports grid
sports_frame = tk.Frame(main_frame, bg='#f9f9f9')
sports_frame.pack()

# List of sports
sports = ["Basketball", "Football", "Rugby", "Cricket"]

# Create buttons for each sport
for i, sport in enumerate(sports):
    frame = tk.Frame(sports_frame, bg='white', bd=1, relief='solid')
    frame.grid(row=i // 2, column=i % 2, padx=10, pady=10)
    
    label = tk.Label(frame, text=sport, font=("Arial", 16), bg='white')
    label.pack(pady=10)
    
    button = tk.Button(frame, text="Select", font=("Arial", 12), command=lambda s=sport: select_sport(s))
    button.pack(pady=10)

# Create a frame for the footer
footer_frame = tk.Frame(root, bg='white')
footer_frame.pack(fill='x', side='bottom', pady=10)

footer_label = tk.Label(footer_frame, text="Sportify", font=("Arial", 14), bg='white')
footer_label.pack(side='left', padx=10)

footer_nav_frame = tk.Frame(footer_frame, bg='white')
footer_nav_frame.pack(side='right')

for text in ["Topic", "Page", "Page", "Page"]:
    footer_nav_button = tk.Button(footer_nav_frame, text=text, font=("Arial", 12), bg='white', relief='flat')
    footer_nav_button.pack(side='left', padx=5)

# Run the application
root.mainloop()
