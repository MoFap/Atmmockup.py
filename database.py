

def create(account_number, user_details):

    completion_state = False

    try:
        f = open("data/user_record/" + str(account_number) + ".txt", "x")

    except FileExistsError:
        print("User already exists")
        return completion_state

    else:
        f.write(str(user_details));
        completion_state = True

    finally:
        f.close()

    return completion_state



create(1664902096, ["morenike", "fapojuwo", "baffie@yahoo.com", "baffie1990", 500])