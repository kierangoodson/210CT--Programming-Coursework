class BinTreeNode(object):

    def __init__(self, value):
        '''A function that, when the class is called, the value is
         passed to it and saved as instance. Left and right set to none for now'''
        self.value=value
        self.left=None
        self.right=None

def tree_insert(tree, item):
    '''This function is for the tree insertion, taking  '''
    if tree==None:                          
        tree=BinTreeNode(item)              
        
    else:
        if(item < tree.value):                  #If item is less than tree value...
            if(tree.left==None):                #If there's nothing in the left branch.
                tree.left=BinTreeNode(item)     #tree.left is equal to the item 
            else:
                tree_insert(tree.left,item)     #Insert item to left of tree
        else:                                   #Otherwise...
            if(tree.right==None):               #If there's nothing in the right branch
                tree.right=BinTreeNode(item)    #tree.right is equal to the item
            else:                               
                tree_insert(tree.right,item)    #Insert item to right of tree
    return tree


def postorder(tree):

    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    else:
        print(tree.value)


def in_order(tree):
    '''This function prints the tree in order'''
    top = tree                                      #Parameter tree becomes variable 'top'
    List = []                                       #List = empty list 
    treeDisplayed = False                             
    while treeDisplayed == False:
        if top != None:                             #If the tree isn't empty...
            List.append(top)                        #Append the tree to the list 
            top = top.left                          #Moves down the left hand branch of tree

        else:                                       #Otherwise...
            if len(List) > 0:                       #As long as the length of the list is > 0 
                top = List.pop()                    #Take list off the top
                print(top.value)                    #print tree value
                top = top.right                     #Moves down the right branch of the tree

            else:
                treeprinted = True

if __name__ == '__main__':

  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
