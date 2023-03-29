from Operation import Operation

def main():
    option = Operation()
    print("Enter the following operation:")
    print("1. Create\n2. Update")
    choice = int(input("Choose"))
    if choice == 1:
        option.create()
        print(option.control)
    elif choice == 2:
        option.update()
        print(option.control)
    elif choice == 3:
        option.loaddb()
        print(option.control)

if __name__ == "__main__":
    main()
