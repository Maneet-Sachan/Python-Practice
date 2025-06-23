import tkinter as tk

# List of basic daily life words (added more words)
WORDS = [
    "apple", "table", "chair", "water", "phone", "house", "bread", "light",
    "clock", "shirt", "money", "music", "plant", "glass", "mouse", "paper",
    "pen", "book", "door", "car", "window", "bottle", "pencil", "mirror",
    "pillow", "blanket", "remote", "candle", "spoon", "fork", "knife",
    "plate", "cup", "bag", "shoes", "watch", "radio", "purse", "wallet",
    "key", "bed", "sofa", "fan", "lamp", "brush", "comb", "soap", "towel"
]
import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

class WordScrambleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Scramble Game")
        self.score = 0
        self.current_word = ""
        self.scrambled_word = ""
        self.create_widgets()
        self.next_word()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="", font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.master, font=("Arial", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.check_button = tk.Button(self.master, text="Check", command=self.check_word)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(self.master, text="Next Word", command=self.next_word)
        self.next_button.pack(pady=5)

    def next_word(self):
        self.current_word = random.choice(WORDS)
        self.scrambled_word = scramble_word(self.current_word)
        while self.scrambled_word == self.current_word:
            self.scrambled_word = scramble_word(self.current_word)
        self.word_label.config(text=self.scrambled_word)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.entry.config(state="normal")
    def check_word(self, event=None):
        guess = self.entry.get().strip().lower()
        if self.entry.cget("state") == "disabled":
            return
        if guess == self.current_word:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
    def check_word(self, event=None):
        guess = self.entry.get().strip().lower()
        if self.entry.cget("state") == "disabled":
            return
        if guess == self.current_word:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
            self.entry.config(state="disabled")
            self.check_button.config(state="disabled")
        else:
            self.result_label.config(text=f"Wrong! The word was '{self.current_word}'", fg="red")
            self.entry.config(state="disabled")
            self.check_button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.score}")
