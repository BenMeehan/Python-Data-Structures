def merge(li1,li2,arr):
    i=0
    j=0
    k=0
    while i<len(li1) and j<len(li2):
        if(li1[i]<li2[j]):
            arr[k]=li1[i]
            k=k+1
            i=i+1 
        else:
            arr[k]=li2[j]
            k=k+1
            j=j+1
    while i<len(li1):
        arr[k]=li1[i]
        k=k+1
        i=i+1
    while j<len(li2):
        arr[k]=li2[j]
        k=k+1
        j=j+1
        
def merge_sort(arr):
    if len(arr)==1 or len(arr)==0:
        return
    mid=len(arr)//2
    li1=arr[0:mid]
    li2=arr[mid:]
    
    merge_sort(li1)
    merge_sort(li2)
    
    merge(li1,li2,arr)
    return arr
print(merge_sort([4,2,1,6,7,0,9]))