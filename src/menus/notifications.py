'''
Created on Aug 14, 2025

@author: joe
'''

class NotificationMenu(object):
    import tkinter.font as tkFont    
    '''
    classdocs
    '''

    def __init__(self, frame, tk, out_text_area):
        self.frame = frame
        self.tk = tk
        self.out_text_area = out_text_area
        self.link_font = self.tkFont.Font(family="TkDefaultFont", size=10, underline=True)
       
    def build(self):
        
        # clear the passed frame
        for widget in self.frame.winfo_children() :
            widget.destroy()
        self.create_menu_items()
            
    def create_menu_items(self):
        # Example menu items
        menu_items = [
            ("CreateNotification", self.create_notification),
            ("AllNotifications", self.all_notifications),
            ("FindByNotificationId", self.find_by_id)
        ]

        # .grid() makes it fill the cell
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
  
    def create_notification(self):
        print("Create Notification")
        # Add logic to change content or view

    def all_notifications(self):
        print("Get All Notifications")
        # Add logic to change content or view  
        
    def find_by_id(self):
        print("Find Notification By Id")    
        # Add logic to change content or view
