class Node:

    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
        
    def __repr__(self) -> str:
        left = repr(self.__left) if self.__left else None
        right = repr(self.__right) if self.__right else None
        if left and right:
            return f'({left} {self.__value} {right})'
        elif left:
            return f'({left} {self.__value})'
        elif right:
            return f'({self.__value} {right})'
        return f'({self.__value})'


def print_tree(tree_node):
    if tree_node.get_left() is not None:
        print_tree(tree_node.get_left())
    print(tree_node.get_value(), end=" ")
    if tree_node.get_right() is not None:
        print_tree(tree_node.get_right())


def sum_tree(node: Node) -> int:
    if node is None:
        return 0
    node.set_value(node.get_value()
                   + sum_tree(node.get_left())
                   + sum_tree(node.get_right()))
    return node.get_value()



def sum_paths_to_leaves(node:Node, sum_so_far:int = 0) -> None:
    if node is None:
        return
    if node.get_left() is None and node.get_right() is None:
        node.set_value(sum_so_far + node.get_value())
        return
    sum_paths_to_leaves(node.get_left(), sum_so_far + node.get_value())
    sum_paths_to_leaves(node.get_right(), sum_so_far + node.get_value())

