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
    
    # function back():
    # if back_stack is empty:
    #     print "No pages to go back to"
    #     return current_page

    # push current_page to forward_stack

    # current_page = pop from back_stack

    # return current_page



    # function forward():
    # if forward_stack is empty:
    #     print "No pages to go forward to"
    #     return current_page

    # push current_page to back_stack

    # current_page = pop from forward_stack

    # return current_page


    # function get_current_page():
    # return current_page



    # function print_state():
    # print "Back:", back_stack
    # print "Current:", current_page
    # print "Forward:", forward_stack