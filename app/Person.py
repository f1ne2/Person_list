from typing import Optional


class Person:

    def __init__(self, name: Optional[str], address: Optional[str],
                 phone: Optional[str], identification: Optional[str]):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = identification

    def __eq__(self, other):
        if self.name == other.name and self.address == other.address and \
                self.phone == other.phone and self.id == other.id:
            return True
        return False
