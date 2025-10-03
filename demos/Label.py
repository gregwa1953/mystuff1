import sys
import os
import tkinter as tk

# Add the parent directory to the path to find the bwidget module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bwidget import Label

if __name__ == '__main__':
    root = tk.Tk()
    root.title("BWidget Label Demo")

    label = Label(root, text="This is a BWidget Label")
    label.pack(pady=10, padx=10)

    root.mainloop()