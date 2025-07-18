import tkinter as tk
import random
import string

#for creating password the function which is used
def create_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            result_label.config(text="Please enter a valid length.")
            return
    except ValueError:
        result_label.config(text="Only numbers allowed.")
        return

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_chars = letters + numbers + symbols
    new_password = ''.join(random.choice(all_chars) for _ in range(length))

    result_label.config(text="Generated Password: " + new_password)
    
#GUI window
window = tk.Tk()
window.title("Password Creator")
window.geometry("400x200")
window.configure(bg= "#f0f0f0")

#heading
heading_label = tk.Label(window, text="Simple Password Generator", font=("Arial", 14, "bold"), bg= "#f0f0f0")
heading_label.pack(pady=10)

#input for length
length_label = tk.Label(window, text="Enter Password Length:", font=("Arial", 10), bg= "#f0f0f0")
length_label.pack()

entry_length = tk.Entry(window, font=("Arial", 10), width=10)
entry_length.pack(pady=10)

#button to generate

generate_button = tk.Button(window, text="Generate", command= create_password, font =("Arial,10"), bg= "#4caf50", fg= "white")
generate_button.pack(pady=10)

#output
result_label = tk.Label(window, text="", font=("Aril", 10), bg="#f0f0f0", fg="#333333")
result_label.pack()

#start the app
window.mainloop()