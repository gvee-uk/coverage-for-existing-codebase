from ghouls import Ghost, Zombie

if __name__ == "__main__":
    casper = Ghost(name="Casper")
    print(casper.introduce())
    print(casper.scare())
    print("")
    cranberry = Zombie(name="Cranberry", level_of_decay=2)
    print(cranberry.introduce())
    print(cranberry.scare())
