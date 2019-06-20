class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.a=n_rows-1
        self.b=n_cols-1
        
        self.w=[]
        #print(1)
    def flip(self) -> List[int]:
        g=1
          
        while g:
            
            t1=random.randint(0, self.a)
            t2=random.randint(0, self.b)
            if [t1,t2] in self.w:
                continue
            else:
                self.w.append([t1,t2])
                g=0
        return [t1,t2]
             
        

    def reset(self) -> None:
        self.w=[]
        #print(3)