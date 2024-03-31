from tkinter import *
from textblob import TextBlob

def clear_output():
    # Destroy the previous output labels
    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) > 4:  # Skip the first 4 labels (headings and input)
            label.grid_forget()

def check_spelling():
    clear_output()  # Clear previous output
    input_text = spell_check.get()
    if input_text.strip():  # Check if input is not empty
        corrected_text = TextBlob(input_text).correct()
        spell = Label(window, text="The Correct Spelling is : ", font=("Arial", 24, "bold"), bg="gray")
        spell.grid(row=4, column=0, pady=(20, 0))
        correct_text = Label(window, text=str(corrected_text), font=("Arial", 35, "bold"), bg="blue")
        correct_text.grid(row=5, column=0, pady=(10, 0))
    else:
        error_label = Label(window, text="Please enter a word or sentence!", font=("Arial", 20), fg="red")
        error_label.grid(row=4, column=0, pady=(20, 0))

window = Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background="lightblue")

text_heading = Label(window, text="Spelling Checker", font=("Arial", 50, "bold"), bg="darkblue", fg="white")
text_heading.grid(row=0, column=0, pady=(10, 0))

text_check = Label(window, text="Enter the Spelling", font=("Arial", 26,), bg="white", fg="black")
text_check.grid(row=1, column=0, pady=(20, 0))

spell_check = Entry(window, font=("Arial", 32), width=40, bg="lightgrey")
spell_check.grid(row=2, column=0, pady=(10, 0))

Check_button = Button(window, text="Check!", font=("Arial", 25, "bold"), fg="white", bg="red", command=check_spelling)
Check_button.grid(row=3, column=0, pady=(20, 0))

window.mainloop()
