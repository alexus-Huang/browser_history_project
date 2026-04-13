class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None
    
    def visit(self, url):
        if self.current_page is not None:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
    
    def back(self):
        if not self.back_stack:
            return None
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        return self.current_page

    def forward(self):
        if not self.forward_stack:
             return None
        
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        return self.current_page

    def get_current_page(self):
        return self.current_page
    
    def print_state(self):
        print(f"Back: {self.back_stack}\nCurrent: {self.current_page}\nForward: {self.forward_stack}")