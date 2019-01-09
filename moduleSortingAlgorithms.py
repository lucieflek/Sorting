def insertionSort(liste):
	for index in range(1,len(liste)):
		currentvalue = liste[index]
		position = index
		while position>0 and liste[position-1]>currentvalue:
			liste[position]=liste[position-1]
			position = position-1
			liste[position]=currentvalue


def bubbleSort(liste):
	for passnum in range(len(liste)-1,0,-1):
		for i in range(passnum):
			if liste[i]>liste[i+1]:
				temp = liste[i]
				liste[i] = liste[i+1]
				liste[i+1] = temp


def mergeLists(left_sublist,right_sublist):
	i,j = 0,0
	result = []
	#iterate through both left and right sublist
	while i<len(left_sublist) and j<len(right_sublist):
		#if left value is lower than right then append it to the result
		if left_sublist[i] <= right_sublist[j]:
			result.append(left_sublist[i])
			i += 1
		else:
			#if right value is lower than left then append it to the result
			result.append(right_sublist[j])
			j += 1
	#concatenate the rest of the left and right sublists
	result += left_sublist[i:]
	result += right_sublist[j:]
	#return the result
	return result

def mergeSort(liste):
	#if list contains only 1 element return it
	if len(liste) <= 1:
		return liste
	else:
		#split the lists into two sublists and recursively split sublists
		midpoint = int(len(liste)/2)
		left_sublist = mergeSort(liste[:midpoint])
		right_sublist = mergeSort(liste[midpoint:])
		#return the merged list using the merge_list function above
		return mergeLists(left_sublist,right_sublist)


def quickSort(liste):
	quickSortHelper(liste,0,len(liste)-1)

def quickSortHelper(liste,first,last):
	if first<last:
		 splitpoint = partition(liste,first,last)
		 quickSortHelper(liste,first,splitpoint-1)
		 quickSortHelper(liste,splitpoint+1,last)

def partition(liste,first,last):
	pivotvalue = liste[first]
	leftmark = first+1
	rightmark = last
	done = False
	while not done:
		 while leftmark <= rightmark and liste[leftmark] <= pivotvalue:
			  leftmark = leftmark + 1

		 while liste[rightmark] >= pivotvalue and rightmark >= leftmark:
			  rightmark = rightmark -1
		 if rightmark < leftmark:
			  done = True
		 else:
			  temp = liste[leftmark]
			  liste[leftmark] = liste[rightmark]
			  liste[rightmark] = temp
	temp = liste[first]
	liste[first] = liste[rightmark]
	liste[rightmark] = temp

	return rightmark
