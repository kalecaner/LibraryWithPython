from datetime import datetime
class Book:
    def __init__(self,Name,Author,ReleaseDate=None,PageAmount=None):
        self.Name = Name
        self.Author= Author
        if ReleaseDate==None:
            self.ReleaseDate = datetime.now()
        else:
            self.ReleaseDate = ReleaseDate

        self.PageAmount=PageAmount


