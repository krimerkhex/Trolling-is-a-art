from pyrse import add_ingot, get_ingot, empty


def squeak(f):
    def wrapper(purse):
        print("SQUEAK")
        return f(purse)

    return wrapper


if __name__ == "__main__":
    wallet: {str, int} = {}
    add_ingot = squeak(add_ingot)
    get_ingot = squeak(get_ingot)
    empty = squeak(empty)
    print(add_ingot(get_ingot(add_ingot(empty(wallet)))))
