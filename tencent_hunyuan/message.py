from dataclasses import dataclass

@dataclass
class Message:
    def __init__(self, role, content):
        self.Role = role
        self.Content = content
    Role: str
    Content: str
    

        

    