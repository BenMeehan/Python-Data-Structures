class HashTable:
    def __init__(self,size=20):
        self.table=[[] for i in range(size)]
        
    def _hash(self,val):
        total=0
        for i in range(0,min(len(val),20)):
            total+=ord(val[i])
        
        total=(total*7)%min(len(val),20)
        return total

    def Set(self,keyval):
        key=self._hash(keyval[0])
        self.table[key].append(keyval)
        
    def Get(self,val):
        key=self._hash(val)
        if self.table[key]==[]:
            return None
        else:
            found=0
            for i in self.table[key]:
                if i[0]==val:
                    found=1
                    return i[1]
            if found==0:
                return None
            
    def Keys(self):
        key_arr=[]
        for i in self.table:
            for j in i:
                key_arr.append(j[0])
        print(key_arr)
    
    def Values(self):
        val_arr=[]
        for i in self.table:
            for j in i:
                val_arr.append(j[1])
        print(val_arr)

h=HashTable()
