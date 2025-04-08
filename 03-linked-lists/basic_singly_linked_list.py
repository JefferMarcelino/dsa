class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def __str__(self):
    return " -> ".join(str(node.data) for node in self._iter_nodes())
  
  def _iter_nodes(self):
    current = self.head

    while current:
      yield current
      current = current.next
  
  def __len__(self):
    return sum(1 for _ in self._iter_nodes())
  
  def delete(self, position):
    if position < 0:
      raise IndexError("Position must be a non-negative integer")
    
    if self.head is None:
      raise IndexError("Delete operation cannot be performed on an empty list")
    
    if position == 0:
      current = self.head
      self.head = current.next
      return current.data
    
    current = self.head
    previous = None

    for _ in range(position):  
      if current is None:
        raise IndexError(f"Position {position} is out of range")
      
      previous = current
      current = current.next

    if current is None:
      raise IndexError(f"Position {position} is out of range")

    node_to_delete = previous.next
    previous.next = previous.next.next

    return node_to_delete.data
    

  def insert(self, data, position=0):
    if position < 0:
      raise IndexError("Position must be a non-negative integer")

    if position == 0:
      new_node = Node(data, self.head)
      self.head = new_node
      return data

    current = self.head
  
    for _ in range(position - 1):
      if current is None:
        raise IndexError(f"Position {position} is out of range")

      current = current.next

    new_node = Node(data, current.next if current else None)
    if current:
      current.next = new_node

    return data


linkedList = LinkedList()

linkedList.insert(5)
linkedList.insert(10)
linkedList.insert(15)

print(linkedList)

linkedList.delete(0)

print(linkedList)