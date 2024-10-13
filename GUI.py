import tkinter as tk
from tkinter import Label, Button, Entry, StringVar
from PIL import Image, ImageTk
import os
import random



# This finction is created to load the flag/county names to the txt fil.
def load_flag_names(file_path):
    flag_name_mapping = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            image_file = parts[0] + '.png' if not parts[0].endswith('.png') else parts[0]
            country_names = [name.strip().lower() for name in parts[1:]]  # All possible names in lowercase
            flag_name_mapping[image_file] = country_names
    return flag_name_mapping

def load_random_flag():
    global current_flag_file, current_flag_names
    if len(remaining_flags) == 0:
        flag_label.config(text="You've guessed all the flags correctly!")
        return

    current_flag_file = random.choice(remaining_flags)
    current_flag_names = flag_name_mapping[current_flag_file]


    img = Image.open(os.path.join(flags_dir, current_flag_file))
    img = img.resize((200, 150))
    img_tk = ImageTk.PhotoImage(img)

    flag_label.config(image=img_tk)
    flag_label.image = img_tk

def check_answer():
    user_guess = flag_name_var.get().strip().lower()
    if user_guess in current_flag_names:
        update_score(True)
        answered_flags.append(current_flag_file)
        remaining_flags.remove(current_flag_file)
    else:
        update_score(False)
    flag_name_var.set("")
    load_random_flag()

def update_score(is_correct):
    global correct_score, incorrect_score
    if is_correct:
        correct_score += 1
        correct_score_label.config(text=f"Correct: {correct_score}")
    else:
        incorrect_score += 1
        incorrect_score_label.config(text=f"Incorrect: {incorrect_score}")


root = tk.Tk()
root.title("Flag Predictor Game")


correct_score = 0
incorrect_score = 0
current_flag_names = []
answered_flags = []


flags_dir = 'Flags'
flag_name_file = 'Flag_names.txt'

flag_name_mapping = load_flag_names(flag_name_file)
flag_files = list(flag_name_mapping.keys())
remaining_flags = flag_files.copy()


flag_label = Label(root)
flag_label.pack(pady=20)


flag_name_var = StringVar()
flag_name_entry = Entry(root, textvariable=flag_name_var)
flag_name_entry.pack(pady=10)


submit_button = Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=5)


correct_score_label = Label(root, text=f"Correct: {correct_score}")
correct_score_label.pack(pady=5)

incorrect_score_label = Label(root, text=f"Incorrect: {incorrect_score}")
incorrect_score_label.pack(pady=5)


new_flag_button = Button(root, text="Show Random Flag", command=load_random_flag)
new_flag_button.pack(pady=10)

# So that random flags are loaded
load_random_flag()

root.mainloop()
