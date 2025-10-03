import sys
import os
import tkinter as tk

# Add the parent directory to the path to find the bwidget module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bwidget.arrowbutton import ArrowButton

if __name__ == '__main__':
    root = tk.Tk()
    root.title("BWidget ArrowButton Demo")

    # The ArrowButton widget does not take a 'text' argument.
    # It takes a 'type' argument which can be 'up', 'down', 'left', or 'right'.
    arrow_button = ArrowButton(root, type='right')
    arrow_button.pack(pady=10, padx=10)

    root.mainloop()