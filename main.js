const contacts = []; //holds a list of phone numbers. 
const contactMap = new Map();

const addNumber = (name, phonenumber, email)=>{
    if(contactMap.has(phonenumber))
    {
        throw Error("The phone number already exists")
    }
    const phone = {
        name,
        phonenumber,
        email,
        dateCreated: new Date()
    }

    contacts.push([phonenumber]);
    contactMap.set(phonenumber, phone);
}

const getPhoneNumber = (phonenumber)=>{
    if(contactMap.has(phonenumber))
        return contactMap.get(phonenumber);
    return null
}

const getAllNumbers = ()=>{
    return contacts;
}


addNumber("John","1234","john@doe.com") 
//addNumber("John","1234","john@doe.com") Throws error since it's a duplicate
addNumber("Jane","12345","jane@doe.com")
console.log(getAllNumbers()) // returns [ [ '1234' ], [ '12345' ] ]
console.log(getPhoneNumber("12345")) // returns { name: 'Jane', phonenumber: '12345', email: 'jane@doe.com', dateCreated: 2021-12-28T13:51:45.553Z }