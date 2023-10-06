def getCount(self, head_node):
    count = 0
    current_node = head_node
    
    while current_node is not None:
        count += 1
        current_node = current_node.next
    
    return count
            