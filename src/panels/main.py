'''
Created on Aug 14, 2025

@author: joe
'''

# MainPanel inherits from the built-in object class
class MainPanel(object):
      
    '''
        classdocs
    '''
    
    def __init__(self, appRoot, tk):
        self.appRoot = appRoot
        self.tk = tk
        
    def build(self) :   
        # Configure row and column weights for expansion
        self.appRoot.grid_rowconfigure(0, weight=3) # Make the first Row Taller
        self.appRoot.grid_rowconfigure(1, weight=1)
        self.appRoot.grid_columnconfigure(0, weight=1)
        self.appRoot.grid_columnconfigure(1, weight=3) # Make second column wider
        
        # Create a Frame to act as a "panel"
        self.east_panel = self.tk.Frame(self.appRoot, bg="lightblue")
        # Sticky "nsew" makes it fill the cell
        self.east_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
     
        # Create a Frame to act as a "panel"
        self.west_panel = self.tk.Frame(self.appRoot, bg="lightblue")
        # Sticky "nsew" makes it fill the cell
        self.west_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
        # Create a Frame to act as a "panel"
        self.south_panel = self.tk.Frame(self.appRoot, bg="white")
        # Sticky "nsew" makes it fill the cell
        self.south_panel.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    
    
        self.exit_button = self.tk.Button(self.south_panel, text="Exit")
        self.exit_button.place(relx=0.5, rely=0.5, anchor=self.tk.CENTER) # Center the button
    
