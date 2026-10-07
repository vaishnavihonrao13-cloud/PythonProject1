try:
    int("abc")
except ValueError as e :
    raise RuntimeError("unable to process input") from e
