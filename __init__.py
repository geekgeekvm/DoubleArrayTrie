value={'#':1,'a':2,'b':3,'c':4,'d':5,'e':6,'f':7,'g':8,'h':9,'i':10,'j':11,'k':12,'l':13,'m':14,'n':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27}

  

class DATrie:
    def __init__(self):
        self.base=[0]*50
        self.check=[0]*50
        self.tail=[]
        self.base[0]=None
        self.check[0]=None
        self.tail.append(None) #tail[0]
        self.tail.append(None) #tail[1] -- for initial condition
        self.base[1]=1
        self.check[1]=0
        self.pos=1
        
        
    def search(self,word):
        n=1
        k=0
        for i in range(0,len(word)):
            if self.base[n] >0:
                if self.check[self.base[n]+value[word[i]]] == n:
                    n=self.base[n]+value[word[i]]
                    k+=1
                else:
                    return False
            else:
                break
        pos=-1*self.base[n]
        cmpword=""
        for i in self.tail[pos:]:
            if i != "#":
                cmpword+=i 
            elif i == "#":
                cmpword+=i 
                break
    
        if cmpword==word[k:]:
            return True
        else:
            return False
        
    
    
    
    def insert(self,word):
        #Case 1: Inserting a word when the trie is empty
        if self.tail[1] is None:
            c=1
            self.tail[1]=word[1]
            for i in word[2:]:
                self.tail.append(i)
                c+=1
                
            self.base[self.base[1]+value[word[0]]]=-1*self.pos   
            self.pos=c+1
            self.check[self.base[1]+value[word[0]]]=1            
            return
    
    
        #Case 2: insertion when the new word is inserted without collisions
        if self.check[self.base[1]+value[word[0]]] == 0:
            c=1
            for i in word[1:]:
                self.tail.append(i)
                c+=1
            
            self.base[self.base[1]+value[word[0]]]=-1*self.pos
            self.pos+=c-1       
            self.check[self.base[1]+value[word[0]]]=1
        
        
        
        elif self.check[self.base[1]+value[word[0]]] != 0:
            t=self.base[1]+value[word[0]]
            k=1
            while self.base[t]>0:
                if self.check[self.base[t]+value[word[k]]]==t:
                    t=self.base[t]+value[word[k]]
                    k+=1
                
                elif self.check[self.base[t]+value[word[k]]]==0:
                    c=1
                    for i in word[k+1:]:
                        self.tail.append(i)
                        c+=1
            
                    self.base[self.base[t]+value[word[k]]]=-1*self.pos
                    self.pos+=c-1       
                    self.check[self.base[t]+value[word[k]]]=t
                    break
                    
                elif self.check[self.base[t]+value[word[k]]]!=t and self.check[self.base[t]+value[word[k]]]>0:
                    
                    #Case 4: insertion when a new word is inserted with a collision
                    tempnode=self.base[t]+value[word[k]]
                 
                    m=self.max(t,self.check[self.base[t]+value[word[k]]])
                    l=[[] for y in range(m+1)]
                    for i in range(len(self.check)):
                        if self.check[i] == t:
                            alph=list(value.keys())[list(value.values()).index(i-self.base[t])]
                            l[t].append(alph)
                        elif self.check[i] == self.check[self.base[t]+value[word[k]]]:
                            alph=list(value.keys())[list(value.values()).index(i-self.base[self.check[self.base[t]+value[word[k]]]])]
                            l[self.check[self.base[t]+value[word[k]]]].append(alph)
    
                    if len(l[t])+1<len(l[self.check[self.base[t]+value[word[k]]]]): 
                        tempbase=self.base[t]
                        q=self.x_check(l[t])
                        self.base[t]=q
                        
                        for i in l[tempbase]:
                            tn1=tempbase+value[i]
                            tn2=q+value[i]
                            self.base[tn2]=self.base[tn1]
                            self.check[tn2]=self.check[tn1]
                            
                            if self.base[tn1]>0:
                                for x in range(1,100):
                                    if self.check[self.base[tn1]+x]==tn1:
                                        self.check[self.base[tn1]+x]=tn2
                                        break
                                self.base[tn1]=0
                                self.check[tn1]=0
                            else:
                                self.base[tn1]=0
                                self.check[tn1]=0
                        
                        
                                 
                        self.base[tempnode]=-1*self.pos
                        self.check[tempnode]=t
                        c=1
                        for i in word[k+1:]:
                            self.tail.append(i)
                            c+=1
                        self.pos+=c-1
                        
                    else:
                        tempbase=self.base[self.check[self.base[t]+value[word[k]]]]
                        q=self.x_check(l[self.check[self.base[t]+value[word[k]]]])
                        self.base[self.check[self.base[t]+value[word[k]]]]=q
                        
                        for i in l[tempbase]:
                            tn1=tempbase+value[i]
                            tn2=q+value[i]
                            self.base[tn2]=self.base[tn1]
                            self.check[tn2]=self.check[tn1]
                            
                            if self.base[tn1]>0:
                                for x in range(1,100):
                                    if self.check[self.base[tn1]+x]==tn1:
                                        self.check[self.base[tn1]+x]=tn2
                                        break
                                self.base[tn1]=0
                                self.check[tn1]=0
                            else:
                                self.base[tn1]=0
                                self.check[tn1]=0
                        
                        
                                 
                        self.base[tempnode]=-1*self.pos
                        self.check[tempnode]=t
                        c=1
                        for i in word[k+1:]:
                            self.tail.append(i)
                            c+=1
                        self.pos+=c-1
                    break   
                                        
                    
            #Case 3: insertion when a collision occurs but no repositioning required 
            
            position=-1*self.base[t]
            oldword=""
            c=position
            for i in self.tail[position:]:
                if i != "#":
                    oldword+=i 
                    self.tail[c]="?"
                    c+=1
                elif i == "#":
                    oldword+=i 
                    self.tail[c]="?"
                    break
            #checking if same word is being inserted
            if oldword == word[position:]:
                #reinsert
                c=position
                for i in word[position:]:
                    self.tail[c]=i
                    c+=1
                    return
            else:   #string comparison fails
                temp=position
                i=0
                #inserting common prefix into base & check
                q=0
                while word[i+1] == oldword[i]:
                    i+=1
                    q=self.x_check(word[i])
                    self.base[self.base[i]+value[word[0]]]=q
                    self.check[q+value[word[i]]]=self.base[1]+value[word[0]]
                    
                qnew=self.x_check([word[i+1],oldword[i]])
                self.base[q+value[word[i]]]=qnew
                self.base[qnew+value[oldword[i]]]=-1*temp
                self.check[qnew+value[oldword[i]]]=q+value[word[i]]
                
                #inserting remaining word into tail
                c=-1*self.base[qnew+value[oldword[i]]]
                for j in oldword[i+1:]:
                    self.tail[c]=j
                    c+=1
                
                self.base[qnew+value[word[i+1]]]=-1*self.pos
                self.check[qnew+value[word[i+1]]]=q+value[word[i]]
                
                c=self.pos
                for j in word[i+2:]:
                    self.tail.append(j)
                    c+=1
                
                self.pos=c

                
        
    #helper functions
    def x_check(self,list): #returns minimum integer q such that  q> 0 and CHECK [ q+c ] =0 for all c in list
        q=1
        for i in list:
            while self.check[q+value[i]] != 0:
                q+=1   
        return q        
    
    def max(self,a,b):
        if a>b:
            return a
        else:
            return b
    
    
    def delete(self,word):
        n=1
        k=0
        for i in range(0,len(word)):
            if self.base[n] >0:
                if self.check[self.base[n]+value[word[i]]] == n:
                    n=self.base[n]+value[word[i]]
                    k+=1
                else:
                    print("Word not in dictionary!")
                    return
            else:
                break
        pos=-1*self.base[n]
        cmpword=""
        for i in self.tail[pos:]:
            if i != "#":
                cmpword+=i 
            elif i == "#":
                cmpword+=i 
                break
        if cmpword==word[k:]:
            print("Deleted!")
            self.base[n]=0
            self.check[n]=0
            for i in range(pos,256):
                if self.tail[i] != "#":
                    self.tail[i]='?' 
                elif self.tail[i] == "#":
                    self.tail[i]='?'
                    break
        else:
            print("Word not in dictionary!")
            return     
            
        
        
        
    
def main():
    tree=DATrie()
    
    ch=1
    while ch == 1:
        print("Enter:\n0.To test trie using standard inputs \n1.To insert into trie \n2.To delete from trie \n3.To search for a word in trie \n4.To exit")
        inp=int(input())
        if inp == 0:
                tree.insert("bachelor#")
                print("Inserted!")
                print(tree.base)
                print(tree.check)
                print(tree.tail)
                tree.insert("jar#")
                print("Inserted!")
                print(tree.base)
                print(tree.check)
                print(tree.tail)
                tree.insert("badge#")
                print("Inserted!")
                print(tree.base)
                print(tree.check)
                print(tree.tail)
                tree.insert("baby#")
                print("Inserted!")
                print(tree.base)
                print(tree.check)
                print(tree.tail)
                print(tree.search("bachelor#"))
                print(tree.search("jar#"))
                print(tree.search("baby#"))
                print(tree.search("badge#"))
                print(tree.search("party#"))
                tree.delete("bachelor#")
                print(tree.base)
                print(tree.check)
                print(tree.tail)                
                tree.delete("party")
                print(tree.base)
                print(tree.check)
                print(tree.tail)
                 
            
        elif inp == 1:
            w=input("Enter a word to insert.")
            tree.insert(w+"#")
            print("Inserted!")
            print(tree.base)
            print(tree.check)
            print(tree.tail)            
            
        elif inp == 2:
            w=input("Enter a word to delete.")
            tree.delete(w+"#")
            print(tree.base)
            print(tree.check)
            print(tree.tail)
            
        elif inp == 3:
            w=input("Enter a word to search for.")
            print(tree.search(w+"#"))

        elif inp == 4:
            ch=4
        
        else:
            print("Invalid input")

    

if __name__=='__main__':
    main()
    
