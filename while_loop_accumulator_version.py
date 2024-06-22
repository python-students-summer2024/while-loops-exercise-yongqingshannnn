def get_starting_number():
    while True:
        string = input("How many bottles of beer on the wall? ")
        if string.isdigit():
            num = int(string)
            if num > 0:
                return num
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Invalid input. Please enter an integer.")


def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 0:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(
                f"Take one down, pass it around, {bottles - 1} bottle{'s' if bottles - 1 != 1 else ''} of beer on the wall.\n")
        bottles -= 1
