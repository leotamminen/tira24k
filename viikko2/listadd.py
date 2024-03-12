# Funktio luo uuden listan (ei tule sivuvaikutuksia)
# jokainen alkio lisätään x:ään
def create(t, x):
    return [luku + x for luku in t]
 
if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]