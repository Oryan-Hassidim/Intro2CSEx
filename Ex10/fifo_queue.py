

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple, Any

Coord = Tuple[int, int]


@dataclass
class Node:
    coordinate: Coord
    next: Optional[Any]


class Queue:

    def __init__(self, iterable=None) -> None:
        self.__head = None
        self.__tail = None
        self.__len = 0
        if iterable is not None:
            self.extend(iterable)

    def head(self):
        return self.__head.coordinate

    def add(self, coord: Coord):
        node = Node(coord, None)
        if self.__head is None:
            self.__head = node
            self.__tail = node
            return
        self.__head.next = node
        self.__head = node
        self.__len += 1

    def pop(self):
        if self.__tail is None:
            raise IndexError("pop from empty queue")
        last = self.__tail.coordinate
        self.__tail = self.__tail.next
        self.__len -= 1
        return last

    def extend(self, iterable):
        for item in iterable:
            self.add(item)

    def __len__(self):
        return self.__len

    def __getitem__(self, key):
        if not (-self.__len) <= key < self.__len:
            raise IndexError()
        if key == 0:
            return self.__head.coordinate
        if key < 0:
            key = -key - 1
        else:
            key = self.__len - key - 1
        for i, item in enumerate(self):
            if i == key:
                return item
        raise IndexError()

    def __iter__(self):
        return self.__gen()

    def __gen(self):
        res = self.__tail
        while res is not None:
            yield res.coordinate
            res = res.next

    def __repr__(self) -> str:
        return "[|" + ", ".join(repr(n) for n in self) + "|]"

    def __str__(self) -> str:
        return "[|" + ", ".join(str(n) for n in self) + "|]"
