def show(x):
    try:
        if x==0:
            raise ValueError
    finally:
        print("show block exceuted")
show(1)
show(0)