from collections import defaultdict


class ContactBook:
    """Class for implementing contact book"""
    def __init__(self) -> None:
        """Initialize contact book object """
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str = None) -> None:
        """Adds a new contact to the contact book

        :param name: The name of the contact 
        :param phone: The phone number of the contact 
        :param email: The email address of the contact 
        """
        if name in self.contacts:
            print('Contact already exist!')
            return
        
        self.contacts[name] = {'phone': phone, 'email': email}
        print('Contact added successfully!')

    def view_contacts(self) -> None:
        """Display all contacts in the contact book"""
        for name, info in self.contacts.items():
            print(f'Name: {name}')
            print(f'Phone: {info["phone"]}')
            print(f'Email: {info["email"]}')
            print('-' * 30)            

    def delete_contact(self, name: str) -> None:
        """Delete a contact from contact book

        :param name: The name of the contact to delete
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} deleted successfully!')
        else:
            print('Contact not found!')

    def update_contact(self, name: str, phone: str = None, email: str = None) -> None:
        """Edit an existing contact in the contact book

        :param name: The name of the contact to edit
        :param phone: The new phone nmber of the contact
        :param email: The new email address of the contact
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print('Contact updated successfully!')
            return
        
        print('Contact not found')

