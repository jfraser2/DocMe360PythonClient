'''
Created on Aug 17, 2025

@author: joe
'''

class UpdateTemplateFormDialog(object):
    from openapi_client.api.template_controller_api import TemplateControllerApi
    from openapi_client.models.update_template import UpdateTemplate
    import sys
    import traceback
    import re  # noqa: F401 
    import json   
        
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
        self.top.geometry("350x150")
        self.top.grab_set()  # Grabs all events until the dialog is closed
        
        # Create a Style object
        self.style = self.ttk.Style()
        # Configure a custom style for TLabel (the base style for ttk.Label)
        # You can name the style anything, e.g., 'Red.TLabel'
        self.style.configure('Red.TLabel', foreground='red') 
                
        # Center the dialog box
        self.center_window(self.top)        

        self.template_id_var = self.tk.StringVar()
        self.new_template_text_var = self.tk.StringVar()

        # Create form elements
        self.ttk.Label(self.top, text="Template Id:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.template_id_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.ttk.Label(self.top, text="New Template Text:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.new_template_text_var).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Error message Label
        self.field_error_label = self.ttk.Label(self.top, text="", style="Red.TLabel")
        self.field_error_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)        
        
        # Buttons
        self.ttk.Button(self.top, text="Submit", command=self.validate_form).grid(row=4, column=0, padx=5, pady=5)
        self.ttk.Button(self.top, text="Clear", command=self.clear_form).grid(row=4, column=1, padx=5, pady=5)
        self.ttk.Button(self.top, text="Cancel", command=self.cancel_dialog).grid(row=4, column=2, padx=5, pady=5)
        self.result = None  # To store the form data
        
    def validate_form(self):
        update_id = self.template_id_var.get()
#        new_text = self.new_template_text_var.get()

        if not update_id :
            self.field_error_label.configure(text="Template Id field cannot be empty.")
            return False
        
        # r before a string tells the Python interpreter to treat backslashes as a literal (raw) character.
        # not as an escape character
        if not self.re.match(r"[0-9]+", update_id) :
            self.field_error_label.configure(text="Template Id invalid. Only Numbers allowed.")
            return False

        # Clear any previous error messages
        self.field_error_label.configure(text="") 
        self.submit_form()
        return True
            
    def submit_form(self):
        
        request_body = self.UpdateTemplate(
            template_id = self.template_id_var.get(),
            new_template_text = self.new_template_text_var.get()
        )
        
        try :
            template_controller = self.TemplateControllerApi()
            response = template_controller.update_template_without_preload_content(request_body)
            self.result = response.read().decode('utf-8')
        except Exception as e :
            self.result = self.process_general_exception(e)        
        finally :           
            self.top.destroy()  # Close the dialog
            
    def clear_form(self):
        self.template_id_var.set("")        
        self.new_template_text_var.set("")
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
                
        return self.json.dumps(error_data, indent=4)          