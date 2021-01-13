import time


class node_data:
    """
    This class represents the set of operations applicable on a
    node (vertex) in a directional weighted graph.
    @author Shlomo Glick
    """
    last_update = 0

    def __init__(self, key: int, pos: tuple = (0.0, 0.0, 0.0)):
        self.key = key
        self.set_tag(-1)
        self.pos = pos

    def get_key(self) -> int:
        """
        This method returns the key (id) associated with this node.
        :return: key
        """
        return self.key

    def get_location(self) -> tuple:
        """
         Returns the location of this node, if
        there's no location for the node return None.
        :return: pos -  (x, y, z)
        """
        return self.pos

    def get_tag(self) -> int:
        """
        :return: In case the tag is updated after the reset  returns -1
        else returns the tag value.
        """
        if self.update_time < self.last_update: return -1
        return self.tag

    def set_location(self, pos: tuple)-> None:
        """
        This method allows changing this node's location.
        :param pos: new location  (x,y,z) of this node.
        """
        self.pos = pos

    def set_tag(self, tag: int)-> None:
        """
        This method allows setting the "tag" value for temporal marking an node - common
         practice for marking by algorithms.
        :param tag: the new value of the tag
        """
        self.update_time = self.last_update
        self.tag = tag

    def reset_tag(self)-> None:
        """
        This method resets the tag of all vertices in the graph
        """
        self.__class__.last_update += 1

    def __lt__(self, other):
        return self.get_tag() < other.get_tag()

    def __eq__(self, other) -> bool:

        """
        This method is equals method between this node and a given node
        :param other:  is the node the method compare to this node
        :return: True in case they are equal
                False in case they are different
        """
        if type(other) != node_data: return False
        if self.get_key() != other.get_key(): return False
        if self.get_location() != other.get_location(): return False
        if self.get_tag() != other.get_tag(): return False
        return True

    def __str__(self) -> str:
        return f"key: {self.key} tag: {self.tag} pos:{self.pos}"

    def __repr__(self) -> str:
        return f"key: {self.key} tag: {self.tag} pos:{self.pos}"
