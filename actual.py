
def magic(is_magician,is_expert):

    try:

        if is_magician and is_expert:
            return 'you are genius'
        elif is_magician and not is_expert:
            return 'atleast you are magician'
        elif not is_magician and is_expert:
            return 'atleast you are an expert'
        else:
            return 'you need magic'

    except ValueError as err:
        return err



magic(False,True)
