ls1 = [1,2,3,4,5,5,4,1]
ls2 = [2,2,2,4,5,6,7,8]

def find_common_elements(ls1:list,ls2:list):
    return list(set(ls1) & set(ls2))

print(find_common_elements(ls1,ls2))