#Passing Stones
#Aaron Sartin, Sunwoo Yim

#passes in two matrices

import math

def addArray(array1, array2):
	output = []
	for n in range (0, len(array1)):
		output = output + [array1[n] + array2[n]]
	return output
#returns some a matrix that sums each of the matrices elements
	
#passes in adjacency matrix in a 2D array and stone locations in a 1D array
def passStones(adjacency, stones):
	addedStones = [0]*len(stones)
	newStones = []
	for n in range (0, len(stones)):
		#check if there are more stones at a location than adjacent edges
		if stones[n] >= sum(adjacency[n]):
			#if there are remove stones to pass out to adjacent vertices
			newStones = newStones + [stones[n] - sum(adjacency[n])]
			#determines stones to be passed out
			addedStones = addArray(addedStones, adjacency[n])
		else:
			newStones = newStones + [stones[n]]
	return addArray(newStones, addedStones)
#outputs new stone locations

def makePath(length):
	adjacency = []
	for n in range (0, length):
		if n == 0:
			adjacency = adjacency + [[0,1] + [0]*(length - 2)]
		elif n + 1 == length:
			adjacency = adjacency + [[0]*(length - 2) + [1,0]]
		else:
			adjacency = adjacency + [[0]*(n - 1) + [1,0,1] + [0]*(length - n - 2)]
	return adjacency
	
def makeCycle(length):
	adjacency = []
	for n in range (0, length):
		if n == 0:
			adjacency = adjacency + [[0,1] + [0]*(length - 3) + [1]]
		elif n + 1 == length:
			adjacency = adjacency + [[1] + [0]*(length - 3) + [1,0]]
		else:
			adjacency = adjacency + [[0]*(n - 1) + [1,0,1] + [0]*(length - n - 2)]
	return adjacency
	
def makeComplete(length):
	adjacency = []
	for n in range (0, length):
		adjacency = adjacency + [[1]*n + [0] + [1]*(length - n - 1)]
	return adjacency
	
def makeStones(length, startPosition, initialValue):
	stones = [[0]*startPosition + [initialValue] + [0]*(length - startPosition - 1)]
	return stones

def main():
	typeGraph = str(input("path, cycle, or complete?\n"))
	length = int(input("length?\n"))
	initialValue = int(input("initial stone value? automatic is 0?\n"))
	if typeGraph == "path":
		if initialValue == 0:
			#automatically adjusts initialValue
			initialValue = 2*(length - 1)
		for n in range (0, math.ceil(length/2)):
			adjacency = makePath(length)
			stones = makeStones(length, n, initialValue)
			#checks equilibrium
			while stones[-1] not in stones[:-1]:
				stones = stones + [passStones(adjacency, stones[-1])]
			print(str(n) + "   " + str(stones[:-1].index(stones[-1])) + "   " + str(len(stones) - stones[:-1].index(stones[-1]) - 1))
	if typeGraph == "cycle":
		if initialValue == 0:
			#automatically adjusts initialValue
			initialValue = 2*length
		adjacency = makeCycle(length)
		stones = makeStones(length, 0, initialValue)
		while stones[-1] not in stones[:-1]:
			stones = stones + [passStones(adjacency, stones[-1])]
		print(str(0) + "   " + str(stones[:-1].index(stones[-1])) + "   " + str(len(stones) - stones[:-1].index(stones[-1]) - 1))
	if typeGraph == "complete":
		if initialValue == 0:
			#automatically adjusts initialValue
			initialValue = length*(length - 1)
		adjacency = makeComplete(length)
		stones = makeStones(length, 0, initialValue)
		while stones[-1] not in stones[:-1]:
			stones = stones + [passStones(adjacency, stones[-1])]
		print(str(0) + "   " + str(stones[:-1].index(stones[-1])) + "   " + str(len(stones) - stones[:-1].index(stones[-1]) - 1))
	print("initial location - steps to equilibrium - equilibrium cycle length")
	
	
main()