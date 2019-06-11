def findRadius(houses, heaters):    
	houses.sort()
    heaters.sort()
    N, i, maxRadius = len(heaters), 0, 0

	for house in houses:
		while i+1 < N and heaters[i+1] < house:
            i += 1
        maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))    

    return maxRadius