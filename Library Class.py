class book_depot:
    def __init__(self, name, location, books = None, copies = None):
        self.name = name
        self.location = location
        if books is None:
            self.books = []
        else:
            self.books = books
        if copies is None:
            self.copies = []
        else:
            self.copies = copies
    def __str__(self):
        total = 0
        for i in self.copies:
            total += i
        str_total = str(total)
        return 'The library, %s, has a total of %s books'%(self.name, str_total)
    def acquire(self, book):
        if book in self.books:
            pos = self.books.index(book)
            total = self.copies[pos]
            total += 1
            self.copies[pos] = total
        else:
            self.books.append(book)
            self.copies.append(1)
    def checkout(self, book):
        if book in self.books:
            pos = self.books.index(book)
            total = self.copies[pos]
            if total == 0:
                print('That book is already checked out by someone else.')
            else:
                total -= 1
                self.copies[pos] = total
        else:
            print('That book isn\'t in this library.')
    def inventory(self):
        new_list = []
        print('This is the library\'s inventory:')
        for i in self.books:
            index = self.books.index(i)
            tmp_str = self.books[index]
            total = self.copies[index]
            if total < 1:
                tmp_str += ' (w)'
            else:
                tmp_str += ' (%d)'%(total)
            new_list.append(tmp_str)
        new_list.sort()
        pos = 1
        for x in new_list:
            print('%d. '%(pos) + x)
            pos += 1
    def find(self, book):
        if book in self.books:
            pos = self.books.index(book)
            total = self.copies[pos]
            print('True (%d)'%(total))
            return True
        else:
            return False
    def checkin(self, book):
        if book in self.books:
            pos = self.books.index(book)
            total = self.copies[pos]
            total += 1
            self.copies[pos] = total
        else:
            print('That book does not belong to this library.')
library = book_depot('Drake\'s Library', 'Columbus, Ohio')
print(library)
library.acquire('Deathly Hallows')
library.acquire('Alice\'s Adventures in Wonderland')
library.acquire('The Two Towers')
library.acquire('The Lightning Thief')
library.acquire('The Two Towers')
library.inventory()
print(library)
library.checkout('The Lightning Thief')
library.inventory()
library.checkin('The Lightning Thief')
library.inventory()
library.checkout('The Order of the Phoenix')
library.checkin('The Mark of Athena')
library.checkout('Deathly Hallows')
library.checkout('Deathly Hallows')
library.inventory()
