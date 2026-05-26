class Books:
    def __init__(self):
        self.book_list= []
        print("Library Management System")
    
    def add_book(self,book):
        self.book_list.append(book)
        print("Book added to library")

    def issue_book(self,book):
        if book in self.book_list:
            print("book issued")
            self.book_list.remove(book)

        else:
            print("Book not available")

    def return_book(self,book):
        if book not in self.book_list:
            self.book_list.append(book)
            print("Book returned to library")
        else:
            print("Book already in library")

    def show_book(self):
        for book in self.book_list:
            print(book)

a1= Books()
a1.add_book("Python Programming")
a1.add_book("DSA Programming")
a1.issue_book("Python Programming")
a1.return_book("Python Programming")
a1.show_book()
