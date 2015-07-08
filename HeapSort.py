#HeapSort
#HeapSort is split into two parts - Heaping (heapify) and Sorting (taking the root of the heap and maintaining heap definition)
#In this code I'm going to attempt to HeapSort the array "BooYeah"
#credit for this code goes to StackOverflow user i159

BooYeah = [976,648,819,430,216,734,513,51,775,878,591,837,749,477,30,14,899,228,755,451,788,868,543,908,209,688,665,246,216,658,518]

def heapsort(sequence):                                                      
    sequence_length = len(sequence)                                          

    def swap_if_greater(parent_index, child_index):                          
        if sequence[parent_index] < sequence[child_index]:                   
            sequence[parent_index], sequence[child_index] = sequence[child_index], sequence[parent_index]            

    def sift(parent_index, unsorted_length):                                 
        index_of_greater = lambda a, b: a if sequence[a] > sequence[b] else b
        while parent_index*2+2 < unsorted_length:                            
            left_child_index = parent_index*2+1                              
            right_child_index = parent_index*2+2                             

            greater_child_index = index_of_greater(left_child_index,         
                    right_child_index)                                       

            swap_if_greater(parent_index, greater_child_index)               

            parent_index = greater_child_index                               

    def heapify():                                                           
        for i in range((sequence_length/2)-1, -1, -1):                       
            sift(i, sequence_length)                                         

    def sort():                                                              
        count = sequence_length                                              
        while count > 0:                                                     
            count -= 1                                                       
        swap_if_greater(count, 0)  
        sift(0, count)                                                   

    heapify()                                                                
    sort()

HeapSort(BooYeah)
print(BooYeah)
