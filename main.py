from datetime import datetime

class Contact(object):
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.number = number
        self.date_created = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    def asdict(self):
        return { 'name': self.name, 'email': self.email, 'number': str(self.number), 'date_created': self.date_created }

class PhoneBook(object):
    def __init__(self):
        self.contacts = []

    def getContact(self, number):
        #Get unique phone details using the given number
        for contact in self.contacts:
            if contact['number'] == str(number):
                return contact
        return None
    
    def removeContact(self, phone_number):
        contact = self.getContact(phone_number)
        if contact is None:
            return False
        self.contacts.remove(contact)
        return True

    def addContact(self, contact) -> None:
        c = self.getContact(contact['number'])
        #Ensure it's storing a unique number
        if c is None:
            self.contacts.append(contact)
            return 'New contact added'
        else:
            return 'Contact already exists in this phonebook.'
    
    def getAllContacts(self) -> None:
        return [ contact['number'] for contact in self.contacts]

#it is easier to save the phone  num as a 
#string in the contact object to avoid int overflow
#Then parse it into a number or long int later

c1 = Contact('John', 'john@doe.com', 1234) #Creates new contact
c2 = Contact('Jane', 'jane@doe.com', 5678)
pb1 = PhoneBook() #Create new phonebook
pb2 = PhoneBook()

print(pb1.addContact(c1.asdict())) #New contact added
print(pb2.addContact(c2.asdict())) #New contact added
print(pb1.getContact(1234)) #{'name': 'John', 'email': 'john@doe.com', 'number': '1234', 'date_created': '2021-12-28-14:16:52'}
print(pb2.getContact(5678)) #{'name': 'Jane', 'email': 'jane@doe.com', 'number': '5678', 'date_created': '2021-12-28-14:16:52'}
print(pb2.removeContact(5678)) #True
print(pb1.getAllContacts()) #['1234']
print(pb2.getAllContacts()) #[]