class Document:

    #constrcutor
    def _init_(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    # get methods
    def get_title(self):
        return self.title
    
    def get_body(self):
        return self.body

    def get_author(self):
        return self.author

    