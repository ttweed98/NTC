from is_greater import is_greater 

# The next function is used to display my test results more human eye-ball friendly
def publish_result(test):
		def result1():
			value = test()
			if value[0] == value[1]:
				outcome = "PASS"
			else:
				outcome = "FAIL"
			print(f"{test.__name__}: {outcome}")
		return result1


@publish_result
def true_when_greater():
	answer = [is_greater(5, 4), True]
	return answer

@publish_result
def false_when_smaller():
	result = [is_greater(4, 5), False]
	return result

@publish_result
def false_when_equal():
	result = [is_greater(5, 5), False]
	return result

if __name__ == "__main__":
	true_when_greater()
	false_when_smaller()
	false_when_equal()


