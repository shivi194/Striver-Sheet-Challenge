class Queue :

    #Define data members and __init__()




    '''----------------- Public Functions of Queue -----------------'''
    def __init__(self):
        self.l = []
   
    def isEmpty(self) :
        return len(self.l)==0
        #Implement the isEmpty() function



    def enqueue(self, data) :
        #Implement the enqueue(element) function
        self.l.append(data)



    def dequeue(self) :
        if len(self.l) == 0:
            return -1
        else:
            ele = self.l.pop(0)
            return ele
        #Implement the dequeue() function



    def front(self) :
        if len(self.l) == 0:
            return -1
        else:
            ele = self.l[0]
            return ele
        
        #Implement the front() function
