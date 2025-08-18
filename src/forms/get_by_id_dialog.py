'''
Created on Aug 15, 2025

@author: joe
'''
from openapi_client.exceptions import NotFoundException

class GetByIdFormDialog(object):
    from openapi_client.api.notification_controller_api import NotificationControllerApi
    from openapi_client.api.template_controller_api import TemplateControllerApi
    import sys
    import traceback    
    
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
        
        # Create a Style object
        self.style = self.ttk.Style()
        # Configure a custom style for TLabel (the base style for ttk.Label)
        # You can name the style anything, e.g., 'Red.TLabel'
        self.style.configure('Red.TLabel', foreground='red')         
        
        # Center the dialog box
        self.center_window(self.top)        

        self.id_var = self.tk.StringVar()

        # Create form elements
        self.ttk.Label(self.top, text="Id:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ttk.Entry(self.top, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Error message Label
        self.id_error_label = self.ttk.Label(self.top, text="", style="Red.TLabel")
        self.id_error_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)        

        # Buttons
        self.ttk.Button(self.top, text="Submit", command=self.validate_form).grid(row=3, column=0, padx=5, pady=5)
        self.ttk.Button(self.top, text="Cancel", command=self.cancel_dialog).grid(row=3, column=1, padx=5, pady=5)
        self.result = None  # To store the form data

    def validate_form(self):
        search_id = self.id_var.get()

        if not search_id :
            self.id_error_label.configure(text="id field cannot be empty.")
            return False

        # Clear any previous error messages
        self.id_error_label.configure(text="") 
        self.submit_form()
        return True        
        
    def submit_form(self):
        search_id =  self.id_var.get()
        
        try :
            if self.selected_menu_item == "FindByNotificationId" :
                notification_controller = self.NotificationControllerApi()
                response = notification_controller.find_by_notification_id_without_preload_content(search_id)
                self.result = response.read().decode('utf-8')
#                print(self.result);
            else :
                template_controller = self.TemplateControllerApi()
                response = template_controller.find_by_template_id_without_preload_content(search_id)
                self.result = response.read().decode('utf-8')
        except Exception as e :
            self.result = self.process_general_exception(e)        
        finally :           
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