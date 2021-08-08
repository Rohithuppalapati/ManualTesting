def code(num):
    try:
        if num:
            return int(num) + 10
        else:
            return 'please give number'
    except ValueError as err:
        return err
