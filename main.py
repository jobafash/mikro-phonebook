from datetime import datetime

class PhoneBook(object):
    phone_book = dict() 
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number
        self.date_created = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.contacts = []
        self.phone_book[str(number)]['name'] = name
        self.phone_book[str(number)]['email'] = email
        self.phone_book[str(number)]['date_created'] = self.date_created
        self.size = 0

    def get(self, key: int) -> int:
        #Add lines 11 - 14 under add method
        if key in self.contacts:
            return self.phone_book[str(key)]
        else:
            return -1

    def add(self) -> None:
        if self.number in self.contacts:
            return False
        self.contacts.append(str(self.number))
        self.size += 1
    
    def getAll(self) -> None:
        return self.contacts


num = PhoneBook('John', 'john@doe.com', 1234)
#print(PhoneBook.get(1234))
#print(PhoneBook.put('John', 'john@doe.com', 1234))
[
'234': {
    name,
    email,
    date
}
]
#For every add, do
#self.book = dict('234')
#book.add(name) then email and date