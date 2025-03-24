from dataclasses import dataclass, asdict

@dataclass
class User:
    name: str
    age: int
    email: str

    def to_dict(self):
        return asdict(self)
