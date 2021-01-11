import time


class node_data:
    last_update = 0

    def __init__(self, key: int, pos: tuple = (0.0, 0.0, 0.0)):
        self.key = key
        self.set_tag(-1)
        self.pos = pos

    def get_key(self) -> int:
        return self.key

    def get_location(self) -> tuple:
        return self.pos

    def get_tag(self) -> int:
        if self.update_time < self.last_update: return -1
        return self.tag

    def set_key(self, key: int) -> None:
        self.key = key

    def set_location(self, pos: tuple)-> None:
        self.pos = pos

    def set_tag(self, tag: int)-> None:
        self.update_time = self.last_update
        self.tag = tag

    def reset_tag(self)-> None:
        self.__class__.last_update += 1

    def __lt__(self, other):
        return self.get_tag() < other.get_tag()

    def __eq__(self, other) -> bool:
        if type(other) != node_data: return False
        if self.get_key() != other.get_key(): return False
        if self.get_location() != other.get_location(): return False
        if self.get_tag() != other.get_tag(): return False
        return True

    def __str__(self) -> str:
        return f"key: {self.key} tag: {self.tag} pos:{self.pos}"

    def __repr__(self) -> str:
        return f"key: {self.key} tag: {self.tag} pos:{self.pos}"
