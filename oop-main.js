class PhoneBook{
    constructor (){
        //Initialize contacts and hashmap
        this.contacts = []
        this.contactMap = new Map()
    }

    addNumber(name, phonenumber, email){
        //Check for uniqueness
        if(this.contactMap.has(phonenumber))
        {
            throw Error("The phone number already exists")
        }
        const phone = {
            name,
            phonenumber,
            email,
            dateCreated: Date.now()
        }
        //Store phone number  
        this.contacts.push([phonenumber]);
        this.contactMap.set(phonenumber,phone);
    }
    
    getPhoneNumber (phonenumber){
        if(this.contactMap.has(phonenumber))
            return this.contactMap.get(phonenumber);
        return null
    }
    
    getAllNumbers (){
        return this.contacts;
    }
    
}

const phonebook = new PhoneBook();

phonebook.addNumber("John","1234","john@doe.com") 
phonebook.addNumber("Jane","12345","jane@doe.com")
console.log(phonebook.getAllNumbers()) // returns [ [ '1234' ], [ '12345' ] ]
console.log(phonebook.getPhoneNumber("12345")) // returns { name: 'Jane', phonenumber: '12345', email: 'jane@doe.com', dateCreated: 1640700031962 }
//phonebook.addNumber("John","1234","john@doe.com")