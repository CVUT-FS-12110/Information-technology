import json

class PhoneNumber:
    """Represents a phone number with a country prefix and local number."""
    def __init__(self, prefix: str, local_number: str):
        self.prefix = prefix
        self.local_number = local_number

    def get_full_number(self) -> str:
        return f"{self.prefix} {self.local_number}"

    def __str__(self):
        return self.get_full_number()


class Address:
    """Represents a physical address."""
    def __init__(self, street: str, city: str, zip_code: str):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.zip_code} {self.city}"


class Person:
    """Represents a person with name, address, and phone numbers."""
    def __init__(self, first_name: str, last_name: str, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_numbers = []

    def add_phone_number(self, phone_number: PhoneNumber):
        self.phone_numbers.append(phone_number)

    def display_contact(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Address: {self.address}")
        if self.phone_numbers:
            print("Phone Numbers:")
            for pn in self.phone_numbers:
                print(f"  - {pn}")
        else:
            print("No phone numbers available.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# --- Program with prepopulated data ---
def load_contacts_from_json():
    """
    [
        {
            "first_name": "John",
            "last_name": "Doe",
            "address": {
                "street": "123 Main St",
                "city": "Prague",
                "zip_code": "11000"
            },
            "phone_numbers": [
                { "prefix": "+000", "local_number": "777123456" },
                { "prefix": "+000", "local_number": "602987654" }
            ]
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "address": {
                "street": "456 Oak St",
                "city": "Brno",
                "zip_code": "60200"
            },
            "phone_numbers": [
                { "prefix": "+000", "local_number": "601555333" }
            ]
        }
    ]
    """
    data = json.loads(load_contacts_from_json.__doc__)
    contacts = []

    for person_data in data:
        address = Address(**person_data["address"])
        person = Person(person_data["first_name"], person_data["last_name"], address)

        for pn_data in person_data["phone_numbers"]:
            phone_number = PhoneNumber(**pn_data)
            person.add_phone_number(phone_number)

        contacts.append(person)

    return contacts


if __name__ == "__main__":
    contacts = load_contacts_from_json()

    # List all contacts
    print("Available contacts:")
    for idx, person in enumerate(contacts, start=1):
        print(f"{idx}. {person}")

    # Ask user which one to display
    try:
        choice = int(input("\nEnter the number of the contact to display: "))
        if 1 <= choice <= len(contacts):
            contacts[choice - 1].display_contact()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
