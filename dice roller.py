import tkinter as tk
from tkinter import ttk
import random

def roll_dice():
    dice_value = random.randint(1, 6)
    result_label.config(text=f"Dice rolled: {dice_value}")

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Create and place the roll button
roll_button = ttk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=20)

# Create and place the result label
result_label = ttk.Label(root, text="Dice rolled: ")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
