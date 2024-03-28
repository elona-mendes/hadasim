import math

def main():
    option = int(
        input("Press 1 for rectangle;Press for 2 triangle; To exit please press 3.\nYour "
              "choice: "))

    while option != 3:

        height = int(input("Please enter the height of the tower: "))
        if height < 2:
            print("The height must be at least 2, try again.")
            continue
        length = int(input("Please enter the length of the tower: "))
        # rectangle option
        if option == 1:
            if abs(height - length) > 5:
                print(f"The area of the given rectangle is {height * length}.")
            else:
                print(f"The perimeter of the given rectangle is {(height * 2) + (length * 2)}")
        elif option == 2:
            triangle_opt = int(input("Press 1 to calculate the perimeter of the triangle.\nPress 2 to print the "
                                     "triangle\nYour choice: "))
            if triangle_opt == 1:
                edge = math.sqrt((length / 2 * length / 2) + (height * height))
                print(f"The perimeter of the given triangle is {edge * 2 + height}")
            elif triangle_opt == 2:
                if (length % 2 == 0) or (length > (2 * height)):
                    print("Sorry, the triangle cannot be printed.")
                else:
                    # number of ""levels" without first and last levels.
                    level_num = int((length + 1) / 2) - 2
                    if level_num > 0:
                        # number of "*" in each level.
                        each_level = (height - 2) // level_num
                        # number of plus "*" in "top inside" level.
                        last_level = (height - 2) % level_num
                    count = 3
                    print("*".center(length))
                    for i in range(level_num):
                        for k in range(each_level):
                            print(("*" * count).center(length))
                        if count == 3:
                            for j in range(last_level):
                                print(("*" * count).center(length))
                        count += 2
                    print(("*" * count).center(length))
        option = int(
            input("Press 1 for rectangle;Press for 2 triangle; To exit please press 3.\nYour "
                  "choice: "))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
