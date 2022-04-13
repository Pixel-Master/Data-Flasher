import random
import os


def main():
    def written_text(B_written):
        print("Written:", B_written, "Bytes,", B_written / 1000, "KB,", B_written / 1000000, "MB or ",
              B_written / 1000000000, "GB.")

    print("This is a simpel script which just writes useless data.\nBy Pixel Master!\n-----------------\nHow many Bytes do you want to write?")
    goal = input()
    goal = int(goal)
    B_written = 0
    print("You are going to write", goal, "Bytes,", goal / 1000, "KB,", goal / 1000000, "MB or ", goal / 1000000000,
          "GB. To this Directory:", os.getcwd() + "/Spam.txt")
    print("\nType \"YES\" to confirm or any other Key to cancel!")
    confirm = input()
    if confirm == "YES":
        spam_file = open("Spam.txt", "w")
        written_text(B_written)
        while B_written < goal:
            # writeformat = 'Bytes: {1}, KB: {1}'.format(B_written, B_written / 1000)
            show = random.randint(1, 100000)
            if show == 3:
                written_text(B_written)
            spam_file.write("0")
            B_written += 1
            # print(writeformat)
        print("\n-----------------Done!-----------------")
        written_text(B_written)
        print("To this Directory:", os.getcwd() + "/Spam.txt")
    else:
        print("-----------------You canceled!-----------------")
        print("Do you want to run the script again? (y/N)")
        again = input()
        if again == "y":
            main()
        else:
            print("-----------------CANCELED!-----------------")


if __name__ == "__main__":
    main()
