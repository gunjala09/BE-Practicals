#WAP to implement Huffman encoding using a greed stategy
class node:
    def __init__(self,freq,symbol,left=None,right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=''

def branching(node,val=''):
    new_num=val+str(node.huff)
    if(node.left):
        branching(node.left,new_num)
    if(node.right):
        branching(node.right,new_num)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {new_num}")
    
chars=['a','b','c','d','e','f']
freq=[5,25,7,15,4,12]
nodes=[]
#convesion of chars and freq into tree nodes
for x in range (len(chars)):
    nodes.append(node(freq[x],chars[x]))

while len(nodes)>1:
    nodes=sorted(nodes, key=lambda x: x.freq)

    left=nodes[0]
    right=nodes[1]

    left.huff=0
    right.huff=1

    new_node=node(left.freq+right.freq, left.symbol+right.symbol,left ,right)
    nodes.remove(left)    
    nodes.remove(right)
    nodes.append(new_node)

print("huffman enconding:")
branching(nodes[0])    
