try:
    print("enter marks out of 100:")
    num = 175

    assert num >= 0 and num <= 100, "Only non-negative numbers and values in the range 0-100 are allowed"

    print("marks obtained:", num)

except AssertionError as msg:
    print(msg)