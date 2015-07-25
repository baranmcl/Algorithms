#InsertionSort
#Iterate through each item in the list, inserting each item into the ordered list

def insertionSort(somelist):
  for index in range(1, len(somelist)):
    currentvalue = somelist[index]
    position = index
    
    while position > 0 and somelist[position-1]>currentvalue:
      somlist[position] = somelist[position-1]
      position = position-1
      
    somelist[position] = currentvalue
