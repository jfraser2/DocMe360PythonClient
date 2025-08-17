'''
Created on Aug 14, 2025

@author: joe
'''

class TemplateMenu(object):
    from forms.get_all_dialog import GetAllFormDialog
    from forms.get_by_id_dialog import GetByIdFormDialog 
    import tkinter.font as tkFont    

    '''
    classdocs
    '''
    
    def __init__(self, menu_frame, tk, ttk, app_root, out_text_area):
        self.menu_frame = menu_frame
        self.tk = tk
        self.ttk = ttk
        self.app_root = app_root
        self.out_text_area = out_text_area
        self.link_font = self.tkFont.Font(family="TkDefaultFont", size=10, underline=True)

    def build(self):
        # clear the passed frame
        for widget in self.menu_frame.winfo_children() :
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

        # .grid() makes it fill the cell
        for text, command in menu_items:
            self.tk.Button(self.menu_frame,
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
        dialog = self.GetAllFormDialog(self.app_root, self.tk, self.ttk, "AllTemplates", "All Templates")
        dialog.build()
        data = dialog.show()
        if data :
            self.out_text_area.config(state="normal")
            self.out_text_area.delete("1.0", self.tk.END) # Delete from the first character to the end
            self.out_text_area.insert("1.0", data)
            self.out_text_area.config(state="disabled")
            self.out_text_area.grid()
        
    def find_by_id(self):
#        print("Find Template By Id")    
        dialog = self.GetByIdFormDialog(self.app_root, self.tk, self.ttk, "FindByTemplateId", "Find Template By Id")
        dialog.build()
        data = dialog.show()
        if data :
            self.out_text_area.config(state="normal")
            self.out_text_area.delete("1.0", self.tk.END) # Delete from the first character to the end
            self.out_text_area.insert("1.0", data)
            self.out_text_area.config(state="disabled")
            self.out_text_area.grid()
          
    def update_template(self):
        print("Create Template")
        # Add logic to change content or view
