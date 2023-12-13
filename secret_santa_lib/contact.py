class Contact:
    def __init__(self, name: str, email: str):
        self.__name: str = name
        self.__email: str = email
    
    def name(self) -> str:
        return self.__name
    
    def email(self) -> str:
        return self.__email
    
    def to_string(self) -> str:
        return f'{self.name()} ({self.email()})'
