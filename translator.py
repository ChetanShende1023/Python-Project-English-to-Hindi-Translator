import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator

class HindiTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("En-Hi Translator")
        self.root.geometry("400x300")

        # UI Elements
        tk.Label(root, text="English Word:", font=("Segoe UI", 12)).pack(pady=10)
        self.entry = tk.Entry(root, font=("Segoe UI", 14), width=30)
        self.entry.pack(pady=5)

        self.btn = tk.Button(root, text="Translate", command=self.process_translation, 
                             bg="#007acc", fg="white", width=15)
        self.btn.pack(pady=20)

        self.result_var = tk.StringVar()
        tk.Label(root, textvariable=self.result_var, font=("Arial", 18, "bold"), fg="#28a745").pack(pady=10)

    def process_translation(self):
        word = self.entry.get().strip()
        if not word:
            messagebox.showwarning("Input Error", "Please type a word!")
            return
        
        try:
            # Translation logic
            translated = GoogleTranslator(source='en', target='hi').translate(word)
            self.result_var.set(translated)
        except Exception:
            messagebox.showerror("Error", "Check your internet connection.")

if __name__ == "__main__":
    app = tk.Tk()
    HindiTranslator(app)
    app.mainloop()
