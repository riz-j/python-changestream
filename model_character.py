class Character:
    name: str
    role: str
    city: str

    def __init__(self, name: str, role: str, city: str):
        self.name = name
        self.role = role
        self.city = city

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "city": self.city
        }
