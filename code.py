
def k_nearest(distances,source_index,k):

	distances.sort()
	k_nearest = []

	for i in range(len(distances)):

		if(i<k):
			k_nearest.append(i)
		else: 
			break

	for i in range(k-1,len(distances)-1):

		if(distances[i] == distances[i+1]):
			k_nearest.append(i+1)
		else:
			break

	return k_nearest[1:]

print(k_nearest([0,2,3,3,3,4],0,3))
			




