#Basic implementation of a max binary heap.

class MaxHeap:
	def __init__(self, items):
		self.arr = items
		self.buildMaxHeap()
	
	def buildMaxHeap(self):
		for i in xrange((len(self.arr)-1)//2, -1, -1):
			self.maxHeapifyDown(i)
	
	def maxHeapifyUp(self, i):
		parentIndex = self.parentIndex(i)
		while parentIndex is not None:
			if  self.arr[i] <= self.arr[parentIndex]:
				break
			temp = self.arr[parentIndex]
			self.arr[parentIndex] = self.arr[i]
			self.arr[i] = temp
			i = parentIndex
			parentIndex = self.parentIndex(i)
	
	def parentIndex(self, i):
		return (i+1) // 2 - 1 if i != 0 else None
	
	def leftChildIndex(self, i):
		leftChildIdx = i * 2 + 1
		return leftChildIdx if leftChildIdx < len(self.arr) else None
	
	def rightChildIndex(self, i):
		rightChildIdx = i * 2 + 2
		return rightChildIdx if rightChildIdx < len(self.arr) else None
	
	def maxHeapifyDown(self, i):
		max = i
		leftChildIdx = self.leftChildIndex(i)
		if leftChildIdx is None:
			return
		if self.arr[i] < self.arr[leftChildIdx]:
			max = leftChildIdx
		rightChildIdx = self.rightChildIndex(i)
		if rightChildIdx is not None and self.arr[max] < self.arr[rightChildIdx]:
			max = rightChildIdx
		if i != max:
			temp = self.arr[i]
			self.arr[i] = self.arr[max]
			self.arr[max] = temp
			self.maxHeapifyDown(max)

	def extractMax(self):
		if self.isEmpty():
			return None
		max = self.arr[0]
		last = self.arr.pop()
		if 0 < len(self.arr):
			self.arr[0] = last
			self.maxHeapifyDown(0)
		return max
	
	
	def isEmpty(self):
		return len(self.arr) == 0
