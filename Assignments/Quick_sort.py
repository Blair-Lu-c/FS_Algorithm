import time
import random
import matplotlib.pyplot as plt

class QuickSort:
    """
    This is an ascending quicksort class.
    """ 
    def find_pivot(self, arr, left, right):
        """
        This function chooses the middile number from first, middle, last index of elements as pivot.
        """
        mid = (right+1 - left)//2
        if arr[left] <= arr[mid] <= arr[right] or arr[left] >= arr[mid] >= arr[right]:
            return mid
        elif arr[mid] <= arr[left] <= arr[right] or arr[mid] >= arr[left] >= arr[right]:
            return left
        elif arr[mid] <= arr[right] <= arr[left] or arr[mid] >= arr[right] >= arr[left]:
            return right

    def partition(self, arr, left, right):
        """
        This function compare other numbers of array with pivot number.
        If current element smaller than pivot on the left.
        If current element larger than pivot on the right.
        """
        i = left
        pivot_index = self.find_pivot(arr, left, right)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]   # swap the last element with pivot number 

        j = right - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        
        return i  
    
    def quicksort(self, arr, left, right):
        """
        Recursively call the partition function for left and right sides of array
        """
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return arr
        if left < right:
            pi = self.partition(arr, left, right)
            self.quicksort(arr, left, pi - 1)
            self.quicksort(arr, pi + 1, right)
    
    # Get and plot running time in different lists and different lengths of list.
    lengths_of_list = [5, 100, 500, 1000]
    sorted_list=[]
    inversly_sorted_list=[]
    random_list=[]

    def quicksort_running_time(arr, scenoario):
        if scenoario == "random":
            random.shuffle(arr)
        elif scenoario == "sorted":
            pass
        elif scenoario == "inversly":
            arr = arr[::-1]    
        
        time_begin = time.time()
        Q = QuickSort()
        Q.quicksort(arr, 0 ,len(arr)-1)
        time_end = time.time()
        total_time = time_end - time_begin
        return total_time

    for lengths in lengths_of_list:
        arr = list(range(1,lengths))
        time_elapsed = quicksort_running_time(arr = arr, scenoario="random")
        random_list.append(time_elapsed)
        
    print(f"random list running time: {random_list}")

    for lengths in lengths_of_list:
        arr = list(range(1,lengths))
        time_elapsed = quicksort_running_time(arr = arr, scenoario="sorted")
        sorted_list.append(time_elapsed)
        
    print(f"sorted list running time: {sorted_list}")

    for lengths in lengths_of_list:
        arr = list(range(1,lengths))
        time_elapsed = quicksort_running_time(arr = arr, scenoario="inversly")
        inversly_sorted_list.append(time_elapsed)
        
    print(f"inversly sorted list running time: {inversly_sorted_list}")

    plt.plot(lengths_of_list,random_list, label="Random",marker='o')
    plt.plot(lengths_of_list, sorted_list, label="Sorted",marker='o')
    plt.plot(lengths_of_list, inversly_sorted_list, label="Inversly",marker='o')
    plt.ylabel("running time")
    plt.xlabel("lengths of list")
    plt.title('Time Complexity')
    plt.legend()
                    
# Driven code         
if __name__ == '__main__':
    user_input = input("Enter elements of a list separated by space to sort: ")
    list_to_sort = user_input.split()
    for i in range(len(list_to_sort)):
        list_to_sort[i] = int(list_to_sort[i])
    print(f'List to sort: {list_to_sort}')
    Q = QuickSort()
    time_start = time.time()
    Q.quicksort(list_to_sort, 0,  len(list_to_sort)-1)
    time_end = time.time()
    running_time = time_end - time_start
    print(f'Sorted list in ascending order: {list_to_sort}\nRunning time: {running_time}')
    
    