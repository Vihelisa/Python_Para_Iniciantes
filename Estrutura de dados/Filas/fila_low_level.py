

from typing import Any
from typing import Any

EMPTY_NODE_VALUE = 'EMPTY_NODE_VALUE'

class Node: #nó da fila, ele quem manda EQUIVALE A CADA ELEMENTO DE UMA LISTA
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node
    
    def __repr__(self) -> str: #Quando printar o valor na tela, vira apenas o valor nada mais
        return f'{self.value}'

    def __bool__(self) -> str:
        return bool(self.value != EMPTY_NODE_VALUE)

class Queue: # equivale a nossa lista 
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE) #valor nulo para o primeiro elemento
        self.last: Node = Node(EMPTY_NODE_VALUE)  #valor nulo para o ultimo elemento
        self.count = 0

    def append(self, node_value: Any) -> Node:
        new_node = Node(node_value)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.count +=1