import tkinter as tk
import pyautogui
import time
char_num = 1
def on_button_click():
    global text
    text = text_input.get("1.0", "end-1c")
    label.config(text="Writing...")
    root.after(500, root.destroy)  # Close the window after a short delay

def on_text_input_click(event):
    text_input.delete("1.0", "end")
    text_input.tag_remove("placeholder", "1.0", "end")

root = tk.Tk()
root.title("Auto-Write Text")

# Set the initial size of the window
root.geometry("600x400")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter your text:")
label.pack()

# Use the Text widget with a custom width and height
text_input = tk.Text(frame, width=60, height=15, font=("Arial", 12))
text_input.pack(pady=20)

# Add placeholder text to the Text widget
placeholder = "Enter your text here..."
text_input.insert("1.0", placeholder)
text_input.tag_add("placeholder", "1.0", "end")
text_input.tag_config("placeholder", foreground="grey")
text_input.bind("<FocusIn>", on_text_input_click)

# Increase the width and font size of the button, and place it in the middle
button = tk.Button(frame, text="Submit", command=on_button_click, width=16, height=4, font=("Arial", 12))
button.pack(pady=20)

root.mainloop()

# Typewrite the submitted text using pyautogui
time.sleep(4)  # Wait for 2 seconds before typing
for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.0004)
    char_num += 1
if char_num == 10 :
    time.sleep(1000)
