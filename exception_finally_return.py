def test():
    try:
        return 10
    finally:
        return 20
print(test())
