#Function to merge two halves of list.		
def merge(first, second):
    
    #base cases when either of two halves is null.
    if first is None: 
        return second  
    if second is None: 
        return first 

    #comparing data in both halves and storing the smaller in result and
    #recursively calling the merge function for next node in result.
    if first.data < second.data: 
        first.next = merge(first.next, second) 
        first.next.prev = first 
        first.prev = None
        #returning the resultant list.
        return first 
    else: 
        second.next = merge(first, second.next) 
        second.next.prev = second 
        second.prev = None
        #returning the resultant list.
        return second 

#Function to sort the given doubly linked list using Merge Sort. 
def sortDoubly(head): 
    if head is None:  
        return head 
    if head.next is None: 
        return head 
    
    #splitting the list into two halves. 
    second = split(head) 
      
    #calling the sortDoubly function recursively for both parts separately. 
    head = sortDoubly(head) 
    second = sortDoubly(second) 

    #calling the function to merge both halves.
    return merge(head, second) 

#Function to split the list into two halves.
def split(head):
    
    #using two pointers to find the midpoint of list.
    fast = slow =  head 
    
    #first pointer, slow moves 1 node and second pointer, fast moves
    #2 nodes in one iteration.
    while(True): 
        if fast.next is None: 
            break
        if fast.next.next is None: 
            break
        fast = fast.next.next 
        slow = slow.next
    
    #slow is before the midpoint in the list, so we split the 
    #list in two halves from that point.      
    temp = slow.next
    slow.next = None
    return temp 
    