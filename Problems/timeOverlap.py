# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


# sort based on start time
# loop through sorted ints
	# if curr start is <= prev end, count += 1
	# start = max(prev end, curr start)
	# end = curr end


def find_rooms(intervals):
	sorted_intervals = sorted(intervals, key= lambda x:x[0])
	print sorted_intervals
	start = sorted_intervals[0][0]
	end = sorted_intervals[0][1]
	count = 0
	for interval in sorted_intervals[1:]:
		print interval[0], end
		if interval[0] <= end:
			count += 1
		start = max(end, interval[0])
		end = interval[1]
	return count




intervals = [(30, 75), (0, 50), (60, 150), (0,20)]

print find_rooms(intervals)