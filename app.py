from helpers import User
def main():
    pedro = User(1, "pedro", "perdo123", "123", "analist")
    pedro.id = 2
    print(pedro)


if __name__ == "__main__":
    main()