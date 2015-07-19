def mergeSort(listofnumbers):
  if len(listofnumbers)>1:
    mid = len(listofnumbers)//2
    lefthalf = listofnumbers[:mid]
    righthalf = listofnumbers[mid:]
    
    mergeSort(lefthalf)
    mergeSort(righthalf)
    
    i=0
    j=0
    k=0
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
      
    
