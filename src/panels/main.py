'''
Created on Aug 14, 2025

@author: joe
'''

# MainPanel inherits from the built-in object class
class MainPanel(object):
    from menus.notifications import NotificationMenu
    from menus.templates import TemplateMenu
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
        self.appRoot.grid_columnconfigure(1, weight=6) # Make second column wider
        
        # Create a Frame to act as a "panel"
        self.east_panel = self.tk.Frame(self.appRoot, bg="lightblue")
        
        self.notification_menu = self.NotificationMenu(self.east_panel, self.tk)
        # Notifications is the initial Tab        
        self.notification_menu.build()
        self.notifications_tab_text = "Notifications"
        self.last_tab_clicked = self.notifications_tab_text
        # Sticky "nsew" makes it fill the entire grid cell
        self.east_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
            
        self.template_menu = self.TemplateMenu(self.east_panel, self.tk)
        self.templates_tab_text = "Templates"
        
        # Create a Notebook to act as a "tabbed panel"
        self.buildTabbedPanel()
        # Place the Notebook in the west Panel, Sticky "nsew" makes it fill the entire grid cell
        self.notebook.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    
        # Create a Frame to act as a "panel"
        self.south_panel = self.tk.Frame(self.appRoot, bg="white")
        # Sticky "nsew" makes it fill the entire grid cell
        self.south_panel.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    
    
        self.exit_button = self.tk.Button(self.south_panel, text="Exit", command=self.on_exit_click)
        self.exit_button.place(relx=0.5, rely=0.5, anchor=self.tk.CENTER) # Center the button
        
    def buildTabbedPanel(self) :
        
        self.notebook = self.ttk.Notebook(self.appRoot)

        # Create individual tab frames
        tab1 = self.ttk.Frame(self.notebook)
        tab2 = self.ttk.Frame(self.notebook)

        # Add Read-only Text Area to tab1
        self.notification_text_area = self.tk.Text(tab1, wrap="word")
        self.notification_text_area.config(state="disabled")
        
        # Add Read-only Text Area to tab1
        self.template_text_area = self.tk.Text(tab2, wrap="word")
        self.template_text_area.config(state="disabled")

        # Add tabs to the Notebook
        self.notebook.add(tab1, text="Notifications")
        self.notebook.add(tab2, text="Templates")
        
        # Bind the event handler
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)        
                 
    def on_tab_changed(self, event):
        
        # 'event.widget' refers to the ttk.Notebook instance that triggered the event
        notebook_instance = event.widget
        
        # You can now use notebook_instance to access properties or methods
        # of the notebook, just like you would with 'self.notebook'
        selected_tab_id = notebook_instance.select()
        selected_tab_text = notebook_instance.tab(selected_tab_id, "text")
        
        if self.notifications_tab_text == selected_tab_text and self.notifications_tab_text != self.last_tab_clicked :
            self.notification_menu.build()
            self.last_tab_clicked = self.notifications_tab_text
            self.notification_text_area.config(state="normal")
            self.notification_text_area.delete("1.0", self.tk.END) # Delete from the first character to the end
            self.notification_text_area.config(state="disabled")
            
        if self.templates_tab_text == selected_tab_text and self.templates_tab_text != self.last_tab_clicked :
            self.template_menu.build()
            self.last_tab_clicked = self.templates_tab_text        
            self.template_text_area.config(state="normal")
            self.template_text_area.delete("1.0", self.tk.END) # Delete from the first character to the end
            self.template_text_area.config(state="disabled")
