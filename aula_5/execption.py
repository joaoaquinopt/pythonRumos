def divide(a, b):
    try:
        if b == 0:
            raise AiresDivisionError()
        result = a / b
    except AiresDivisionError as e:
        print(e)
    else:
        print("Result ", result)
    finally:
        print("Division finalized")
