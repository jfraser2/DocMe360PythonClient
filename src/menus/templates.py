'''
Created on Aug 14, 2025

@author: joe
'''

class TemplateMenu(object):
    import tkinter.font as tkFont    

    '''
    classdocs
    '''
    
    def __init__(self, frame, tk):
        self.frame = frame
        self.tk = tk
        self.link_font = self.tkFont.Font(family="TkDefaultFont", size=10, underline=True)

    def build(self):
        # clear the passed frame
        widgets_in_frame = self.frame.winfo_children()
        for widget in widgets_in_frame :
            widget.destroy()
        self.create_menu_items()    
            
    def create_menu_items(self):
        # Example menu items
        menu_items = [
            ("CreateTemplate", self.create_template),
            ("AllTemplates", self.all_templates),
            ("FindByTemplateId", self.find_by_id),
            ("UpdateTemplate", self.update_template)
        ]

        # .grid() makes the button appear
        for text, command in menu_items:
            self.tk.Button(self.frame,
                fg="#0000EE",  # Blue for unvisited link
                bg="lightblue",
                cursor="hand2",
                font=self.link_font,
                borderwidth=0,  # Remove button border
                highlightthickness=0, # Remove highlight border
                text=text,
                command=command).grid()
  
    def create_template(self):
        print("Create Template")
        # Add logic to change content or view

    def all_templates(self):
        print("Get All Templates")
        # Add logic to change content or view  
        
    def find_by_id(self):
        print("Find Template By Id")    
        # Add logic to change content or view
          
    def update_template(self):
        print("Create Template")
        # Add logic to change content or view
