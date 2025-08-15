'''
Created on Aug 15, 2025

@author: joe
'''

class GetAllFormDialog(object):
    '''
    classdocs
    '''
    
    def __init__(self, frame, tk, selected_menu_item, out_text_area, title):
        self.frame = frame
        self.tk = tk
        self.selected_menu_item = selected_menu_item
        self.out_text_area = out_text_area
        self.title = title
        
    def build(self):
        print("Build")
        # TODO complete method    
