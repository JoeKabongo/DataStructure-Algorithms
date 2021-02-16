import string
HASH_TABLE_LENGHT = 2
class Node:
    """
    Node class,  Linkedlist
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node
        
class HashTable:
    """
        Hashable to store letters
    """
    def __init__(self):
        """ Array of nodes"""
        self.table = [None] * HASH_TABLE_LENGHT
    
    def insert(self, key, value):
        """ inserting a key and value"""
        index = hash(key) % HASH_TABLE_LENGHT
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
            return 
        if node.get_key() == key:
            node.set_value(value)
            return 
        
        while node.next and node.get_key() != key:  
            prev = node          
            node = node.get_next()
        
        #if there is a node with this key, update it 
        if node.get_key() == key:
            node.set_value(value)
        else:
            node.set_next(Node(key, value))

    def find(self, key):
        """ Value of key"""
        index = hash(key) % HASH_TABLE_LENGHT
        node = self.table[index]
        while node:
            #Node has been found, return it
            if node.get_key() == key:
                return node.get_value()
            node = node.next
        
        return None


    def remove(self, key):
        """ Remove key from hashtable"""

        index = hash(key) % HASH_TABLE_LENGHT
        head = self.table[index]
        #if the key is the head of the linkedlist, just set the linkedlist to next
        if head and head.get_key() == key:
            self.table[index] = head.get_next()
            return 
        else:
            prev = head
            node = node.get_next()
        
            while node and node.get_key() != key:
                prev = node
                node = node.get_next()
            
            #skip the key in the chain of node if found
            if node.get_key() == key:
                prev.set_next(node.get_next())
            

            

p = HashTable()
p.insert("papa", 1)
p.insert("kaka", 13)
p.insert("hoho", 11)
p.insert("hehe", 90)
p.insert("papa", 45)

print(p.find("papa"))
print(p.find("kaka"))
print(p.find("hoho"))
print(p.find("hehe"))
