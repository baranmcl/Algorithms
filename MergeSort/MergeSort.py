def mergeSort(listofnumbers):
  if len(listofnumbers)>1:
    mid = len(listofnumbers)//2
    lefthalf = listofnumbers[:mid]
    righthalf = listofnumbers[mid:]
    
    mergeSort(lefthalf) #recursively moves towards the beginning of a list until it hits a base case
    mergeSort(righthalf)
    
    i=0 #left index counter
    j=0 #right index counter
    k=0 #main list index counter
    #this part actually does the merging
    while i<len(lefthalf) and j <len(righthalf):
      if lefthalf[i]<righthalf[j]:
        listofnumbers[k]=lefthalf[i]
        i+=1
      else:
        listofnumbers[k]=righthalf[j]
        j+=1
      k+=1
    
    while i<len(lefthalf):
      listofnumbers[k]=lefthalf[i]
      i+=1
      k+=1
    
    while j<len(righthalf):
      listofnumbers[k]=righthalf[j]
      j+=1
      k+=1
      
    
