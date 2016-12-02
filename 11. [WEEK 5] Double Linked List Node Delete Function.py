class Node(object):
    '''This class is for the nodes'''
    def __init__(self, value):
        '''Initialising class Node attributes, value, next and previous.'''
        self.value=value                   #Value will be passed to the function.
        self.next=None                     #Next and previous are set to none to begin with.
        self.prev=None

class List(object):                   
    '''This class is for the list'''                          
    def __init__(self):
        '''Initialising list head, tail and list of nodes'''
        self.head=None                     #Head and tail are set to none to begin with.
        self.tail=None
        self.listofNodes = []

    def insert(self,n,x):
    '''This function is for node insertion. It reconnects the pointers of the surrounding nodes to
    the newly inserted node'''
        if n!=None:                        #if n isn't null...
            x.next=n.next                  #node x next = node n next.
            n.next=x                       #node n next = x
            x.prev=n                       #node x previous = n
          
        if x.next!=None:               
            x.next.prev=x              

        if n == None and self.head != None: #if n is the same as none and the head isn't pointing to anything
            self.head.prev = x              #list head previous = x
            x.next = self.head              #node x becomes head
            self.head = x                   #head = x
            x.prev = None                   #node x previous = none because it's the head

            
        if self.head==None:                #if list head is null
            self.head=self.tail=x          #list head = list tail = x
            x.prev=x.next=None             #node x previous = node x nexts = null
          
        elif self.tail==n:                 #and if list tail == node n...
            self.tail=x                    #list tail = node x

    def display(self):
        '''Ths function is for displaying the nodes. '''
        values=[]                          #values is an empty array
        n=self.head                        #node n = list head
        while n!=None:                     #For as long as node n isn't null...
            values.append(str(n.value))    #append values to n 
            n=n.next                       #node n = n next (N points to itself)
        print ("List:"," "," " .join(values))    #output new list and join values?

    def delete(self, deleteNode):
    '''This function will delete any given node. It disconnects the next and previous node pointers from
    the node to be deleted.It then reconnects them after the given node is deleted'''
        foundNode = False                  
        beginSearch = self.head            #begin search at the list head

        while foundNode == False:                             #As long as the node has not been found...
      
            if beginSearch.value == deleteNode:               #If self.head.value is same as the node to be deleted...
          
                if beginSearch.prev != None:                  #If self.head prev is not the head.
              
                    beginSearch.prev.next = beginSearch.next      #The previous node points to the node ahead of the node to be deleted
          
                else:                                             #Otherwise, the next node after the deleted one becomes the head 
                    l.head = beginSearch.next

                if beginSearch.next != None:           #If the head node next points doesn't point to anything... (if it is not the tail)
                    beginSearch.next.prev = beginSearch.prev              #The next node points to the previous node before the node to be deleted.

                else:
                    l.tail = beginSearch.prev                     #The last node becomes the node after the deleted node.

                del(beginSearch) 
                foundNode = True

            elif beginSearch.next == None:                        #if reached end of list and current node isn't to be deleted....
                return False
            else:                                                 #Otherwise, continue searching by moving onto next node.
                beginSearch = beginSearch.next
        return True 

if __name__ == '__main__':
    l=List()                            #calls list function and withn the parameters it creates a node object and then passes that to the
    
    l.insert(None, Node(4))             #prev = none to make it the head of the list
    l.insert(l.head, Node(5))           #l.head refers to the first node
    l.insert(None,Node(6))
    l.insert(l.head,Node(8))
    l.insert(l.head, Node(10))
    l.insert(None, Node(1))         
    l.display()                         #Call display function

    flag = False
    while flag == False:
        try:
            number = int(input("Please enter the number of the node you wish to delete: "))
            flag = True
        except ValueError:
            print("Please enter an integer ONLY: ")
            
    print(l.delete(number))
    l.display()
