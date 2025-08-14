'''
Created on Aug 14, 2025

@author: joe
'''

if __name__ == '__main__':
  from panels.main import MainPanel
  import tkinter as tk

  root = tk.Tk()  # This creates the main window instance.
  root.title("DocMe360 GUI App") # Sets the window title.
  root.geometry("400x300") # Sets the initial size of the window.  
  
  mainPanel = MainPanel(root, tk)
  mainPanel.build()
  
  # Start the Event Loop
  root.mainloop()
      
  pass