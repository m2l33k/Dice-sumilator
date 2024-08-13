import tkinter as tk
from tkinter import messagebox
import random


class DiceSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulator")
        self.root.geometry("300x300")

        self.create_widgets()

    def create_widgets(self):
        # Number of Dice Entry
        self.num_dice_label = tk.Label(self.root, text="Number of Dice:", font=('Helvetica', 12))
        self.num_dice_label.pack(pady=10)

        self.num_dice_var = tk.IntVar(value=1)
        self.num_dice_entry = tk.Entry(self.root, textvariable=self.num_dice_var, font=('Helvetica', 14))
        self.num_dice_entry.pack(pady=10)

        # Roll Button
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=20)

        # Dice Result Display
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

    def roll_dice(self):
        try:
            num_dice = self.num_dice_var.get()
            if num_dice < 1:
                raise ValueError("Number of dice must be at least 1.")

            results = [random.randint(1, 6) for _ in range(num_dice)]
            result_text = ", ".join(f"Die {i + 1}: {result}" for i, result in enumerate(results))
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showwarning("Invalid Input", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulatorApp(root)
    root.mainloop()
