def add_ingot(purse) -> dict:
    new_dict = purse.copy()
    try:
        new_dict["gold_ingot"] += 1
    except KeyError:
        print("[ERROR] no gold_ingots in:", purse)
    return new_dict


def get_ingot(purse) -> dict:
    new_dict = purse.copy()
    try:
        if new_dict["gold_ingot"] != 0:
            new_dict["gold_ingot"] -= 1
    except KeyError:
        new_dict: {str, int} = {}
        print("[ERROR] no gold_ingots in:", purse)
    return new_dict


def empty(purse) -> dict:
    new_dict = purse.copy()
    if "gold_ingot" not in new_dict.keys():
        new_dict["gold_ingot"] = 0
    return new_dict


if __name__ == "__main__":
    wallet: {str, int} = {}
    print(add_ingot(get_ingot(add_ingot(empty(wallet)))))
