from is_greater import is_greater


def publish_result(test):

			value = test()
			if value[0] == value[1]:
				result = "PASS"
			else:
				result = "FAIL"
			print(f"{test.__name__}: {result}")


def true_when_greater():
	result = [is_greater(5, 4), True]
	return result

def false_when_smaller():
	result = [is_greater(4, 5), False]
	return result

def false_when_equal():
	result = [is_greater(5, 5), False]
	return result



if __name__ == "__main__":
	publish_result(true_when_greater)
	publish_result(false_when_smaller)
	publish_result(false_when_equal)
	
