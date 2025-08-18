'''
Created on Aug 18, 2025

@author: joe
'''

class CreateNotificationFormDialog(object):
    from openapi_client.api.notification_controller_api import NotificationControllerApi
    from openapi_client.models.create_notification import CreateNotification
    import sys
    import traceback
    import re  # noqa: F401
        
    '''
    classdocs
    '''

    def __init__(self, app_root, tk, ttk, title):
        self.app_root = app_root
        self.tk = tk
        self.ttk = ttk
        self.title = title
        
    def build(self):
        self.top = self.tk.Toplevel(self.app_root)
        self.top.title(self.title)
        self.top.transient(self.app_root)  # Makes the dialog dependent on the parent window
        self.top.geometry("350x200")
        self.top.grab_set()  # Grabs all events until the dialog is closed
        
        # Create a Style object
        self.style = self.ttk.Style()
        # Configure a custom style for TLabel (the base style for ttk.Label)
        # You can name the style anything, e.g., 'Red.TLabel'
        self.style.configure('Red.TLabel', foreground='red') 
                
        # Center the dialog box
        self.center_window(self.top)        

        self.phone_number_var = self.tk.StringVar()
        self.personalization_var = self.tk.StringVar()
        self.template_id_var = self.tk.StringVar()
        self.template_text_var = self.tk.StringVar()

        # Create form elements
        self.ttk.Label(self.top, text="Phone Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.phone_number_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.ttk.Label(self.top, text="Personalization:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.personalization_var).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        self.ttk.Label(self.top, text="Template Id:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.template_id_var).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.ttk.Label(self.top, text="Template Text:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.template_text_var).grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        # Error message Label
        self.field_error_label = self.ttk.Label(self.top, text="", style="Red.TLabel")
        self.field_error_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)        
        
        # Buttons
        self.ttk.Button(self.top, text="Submit", command=self.validate_form).grid(row=6, column=0, padx=5, pady=5)
        self.ttk.Button(self.top, text="Clear", command=self.clear_form).grid(row=6, column=1, padx=5, pady=5)
        self.ttk.Button(self.top, text="Cancel", command=self.cancel_dialog).grid(row=6, column=2, padx=5, pady=5)
        self.result = None  # To store the form data
        
    def validate_form(self):
        phone_number = self.phone_number_var.get()

        # r before a string tells the Python interpreter to treat backslashes as a literal (raw) character.
        # not as an escape character
        if not self.re.match(r"^\d{3}[- .]?\d{3}[- .]?\d{4}$", phone_number) :
            self.field_error_label.configure(text="Phone Number Format is invalid. Example 123-456-7890")
            return False

        # Clear any previous error messages
        self.field_error_label.configure(text="") 
        self.submit_form()
        return True
            
    def submit_form(self):
        
        request_body = self.CreateNotification(
            phone_number = self.phone_number_var.get(),
            personalization = self.personalization_var.get(),
            template_id = self.template_id_var.get(),
            template_text = self.template_text_var.get()
        )
        
        try :
            notification_controller = self.NotificationControllerApi()
            response = notification_controller.create_notification_without_preload_content(request_body)
            self.result = response.read().decode('utf-8')
        except Exception as e :
            self.result = self.process_general_exception(e)        
        finally :           
            self.top.destroy()  # Close the dialog
            
    def clear_form(self):
        self.phone_number_var.set("")
        self.personalization_var.set("")
        self.template_id_var.set("")        
        self.template_text_var.set("")
        # Clear any previous error messages
        self.field_error_label.configure(text="") 

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
        
    def process_general_exception(self, exception) :
#        print(exception)
        exc_type, exc_value, exc_traceback = self.sys.exc_info()
        formatted_traceback = "".join(self.traceback.format_exception(exc_type, exc_value, exc_traceback))

        error_data = {
            "error_type": exc_type.__name__,
            "error_message": str(exc_value),
            "traceback": formatted_traceback
        }
                
        return error_data                 