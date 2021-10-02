def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    print("test_sum executed successfully")

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
    print("test_sum_tuple executed successfully")
	
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")

