'''
Created on Aug 14, 2025

@author: joe
'''

# MainPanel inherits from the built-in object class
class MainPanel(object):
    import sys as system
      
    '''
        classdocs
    '''
    
    def __init__(self, appRoot, tk, ttk):
        self.appRoot = appRoot
        self.tk = tk
        self.ttk = ttk
        
    def on_exit_click(self):
        self.system.exit() 
           
    def build(self) :   
        # Configure row and column weights for expansion
        self.appRoot.grid_rowconfigure(0, weight=5) # Make the first Row Taller
        self.appRoot.grid_rowconfigure(1, weight=1)
        self.appRoot.grid_columnconfigure(0, weight=1)
        self.appRoot.grid_columnconfigure(1, weight=4) # Make second column wider
        
        # Create a Frame to act as a "panel"
        self.east_panel = self.tk.Frame(self.appRoot, bg="lightblue")
        # Sticky "nsew" makes it fill the cell
        self.east_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
     
        # Create a Notebook to act as a "tabbed panel"
        self.buildTabbedPanel()
        # Place the Notebook in the west Panel
        self.notebook.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    
        # Create a Frame to act as a "panel"
        self.south_panel = self.tk.Frame(self.appRoot, bg="white")
        # Sticky "nsew" makes it fill the cell
        self.south_panel.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    
    
        self.exit_button = self.tk.Button(self.south_panel, text="Exit", command=self.on_exit_click)
        self.exit_button.place(relx=0.5, rely=0.5, anchor=self.tk.CENTER) # Center the button
        
    def buildTabbedPanel(self) :
        
        self.notebook = self.ttk.Notebook(self.appRoot)

        # Create individual tab frames
        tab1 = self.ttk.Frame(self.notebook)
        tab2 = self.ttk.Frame(self.notebook)

        # Add Button to tab1
        self.tk.Button(tab1, text="Notifications")

        # Add Button to tab2
        self.tk.Button(tab2, text="Templates")

        # Add tabs to the Notebook
        self.notebook.add(tab1, text="Notifications")
        self.notebook.add(tab2, text="Templates")
                 
    
