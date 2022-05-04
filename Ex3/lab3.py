from math import *

def get_sliced_str(letters, slices):
	result = []
	s = slices
	for i in slices:
		t, letters = letters[:i], letters[i:]
		result.append(t)
	return result

def all_ways_to_cut(letters, num_words):
	if len(letters) < num_words: return []
	count = len(letters)
	slices = []
	s = [count]
	flag = True

	while flag:

		while len(s) < num_words:
			s.append(s[-1] - 1)
			s[-2] = 1
		if len(s) == num_words:
			slices.append(get_sliced_str(letters, s))

		i = 0
		while len(s) > 1 and s[-1] == 1:
			s.pop()
			i += 1
		s[-1] += i
		if len(s) >= 2:
			s[-1] -= 1
			s[-2] += 1

		if len(s) == 1: flag = False

	return slices



def max_by(lst, key = lambda p: p):
	if lst == []: return None
	max_index = 0
	max_val = key(lst[0])
	for i in range(1,len(lst)):
		val = key(lst[i])
		if max_val < val:
			max_val = val
			max_index = i
	return lst[max_index]

print(*all_ways_to_cut("abcdefghijk", 4), sep = "\n")
