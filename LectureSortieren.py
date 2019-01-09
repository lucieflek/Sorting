from moduleSortingHelpers import *
from moduleSortingAlgorithms import *

def selectionSort(liste):
	# Traverse through all array elements 
	for i in range(len(liste)): 
		# Find the minimum element in remaining unsorted array 
		min_idx = i 
		for j in range(i+1, len(liste)): 
			if liste[min_idx] > liste[j]: 
				min_idx = j 
		# Swap the found minimum element with the first element		 
		liste[i], liste[min_idx] = liste[min_idx], liste[i]


initializeRandomNumberList()

# liste = makeRandomNumberList(2000)
# print(liste[:20])
#startTime = time.time()
#selectionSort(liste)
#endeTime = time.time()
#print(liste[:20])
#print('{:5.3f}s'.format(endeTime-startTime))
performanceStudy(mergeSort, PLOT_WITHFIT, PARTIALLY_SORTED)
#performanceStudy(10000, quickSort, "QuickSort")
