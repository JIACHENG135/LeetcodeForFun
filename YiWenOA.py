def stringFormattedWeeklyPrices(dailyPrice):
	toString = lambda x:"%.2f" % x

	if len(dailyPrice)<7:
		return []
	else:
		state = 0
		ans = []
		for i in range(7):
			state += dailyPrice[i]
		ans.append(toString(state/7))
		for i in range(7,len(dailyPrice)):
			state -= dailyPrice[i-7]
			state += dailyPrice[i]
			ans.append(toString(state/7))
		return ans
a = stringFormattedWeeklyPrices([1,1,1,1,1,1,1,7,7,7,7,7,7,7])
print(a)