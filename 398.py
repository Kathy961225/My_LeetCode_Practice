def __init__(self, nums: List[int]):
    self.n=nums
    

def pick(self, target: int) -> int:
    c=self.n.count(target)
    p=random.randint(1,c)
    for i in range(len(self.n)):
        if self.n[i]==target:
            p-=1
            if p==0:
                return i
				'''