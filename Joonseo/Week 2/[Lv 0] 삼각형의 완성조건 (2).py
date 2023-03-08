def solution(sides):
	answer = 0
	for x in range(1, sides[0] + sides[1]):
		tri = [sides[0],sides[1],x]
		maxs = max(tri)
		mins = sum(tri)-maxs
		if maxs < mins:
			answer+=1
	return answer