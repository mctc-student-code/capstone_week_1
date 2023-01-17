"""
• Create a new class called Author
• An Author has a name, and a list of books published
• When you create a new Author, they don't have any books. So create an empty
books list attribute in __init__
• Your Author class should have a publish method, which takes the title of a
book as an argument. Add the title of this book to this object's books list
• Add a __str__ method that returns a String with the author's name, and
the names of all of their book's titles
• Write a main function to test your class, create some example authors,
and publish some example books

different concept:

data = a or b
if a is truthy, data will be set to a
If a is falsy, then var will be set to b
In Python, empty lists, empty
strings, None, 0 and False are falsy
Does the same as this

"""

class Author:
    def __init__(self, name):
        self.name = name
        self.book_list = []
    
    def publish(self, title):
        book_list_lowercase = [ book.lower() for book in self.book_list ] # gets all book in lower case
        if title.lower() in book_list_lowercase:
            print(f'Warning * The book titled {title} already exists in the list of books for author {self.name}')
        else:
            self.book_list.append(title) # adds the title of the book to the list of books of the author
    
    def __str__(self):
        # if self.book_list:
        #     book_names = ', '.join(self.book_list)
        # else:
        #     book_names = 'No books'

        book_names = ', '.join(self.book_list) or 'No Published books' 
        # if first operation returns a falsy value,i.e. when joining book list is empty, returns the value 'No Published books'
        return f'Name: {self.name}. Published Books: {book_names}'

def main():
    chetan_sharma = Author('Chetan Sharma')
    chetan_sharma.publish("Half GirlFriend")
    chetan_sharma.publish("Two States")
    chetan_sharma.publish("two States")
    print(chetan_sharma)

    dalai_lama = Author('His Holiness The 14th Dalai Lama')
    dalai_lama.publish('My Land And My People')
    dalai_lama.publish('The Art of Living and Dying')
    dalai_lama.publish('The Book Of Joy')
    print(dalai_lama)

    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    minleg = Author('Minleg')
    print(minleg)

main()

        

