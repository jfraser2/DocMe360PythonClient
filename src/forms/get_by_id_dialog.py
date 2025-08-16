'''
Created on Aug 15, 2025

@author: joe
'''

class GetByIdFormDialog(object):
    '''
    classdocs
    '''

    def __init__(self, app_root, tk, ttk, selected_menu_item, title):
        self.app_root = app_root
        self.tk = tk
        self.ttk = ttk
        self.selected_menu_item = selected_menu_item
        self.title = title
        
    def build(self):
        self.top = self.tk.Toplevel(self.app_root)
        self.top.title(self.title)
        self.top.transient(self.app_root)  # Makes the dialog dependent on the parent window
        self.top.geometry("250x150")
        self.top.grab_set()  # Grabs all events until the dialog is closed
        
        # Center the dialog box
        self.center_window(self.top)        

        self.id_var = self.tk.StringVar()

        # Create form elements
        self.ttk.Label(self.top, text="Id:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Buttons
        self.ttk.Button(self.top, text="Submit", command=self.submit_form).grid(row=2, column=0, padx=5, pady=5)
        self.ttk.Button(self.top, text="Cancel", command=self.cancel_dialog).grid(row=2, column=1, padx=5, pady=5)
        self.result = None  # To store the form data

    def submit_form(self):
        self.result = {
            "id": self.id_var.get()
        }
        self.top.destroy()  # Close the dialog

    def cancel_dialog(self):
        self.result = None
        self.top.destroy() # Close the dialog

    def show(self):
        self.top.wait_window()  # Wait until the dialog is closed
        return self.result
    
    def center_window(self, window):
        """Centers a Tkinter window on the screen."""
        window.update_idletasks()  # Ensure geometry information is up-to-date

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = window.winfo_reqwidth()
        window_height = window.winfo_reqheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry(f"+{x}+{y}")