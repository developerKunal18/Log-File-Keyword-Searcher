filename = input("Enter log file name: ")
keyword = input("Enter keyword to search: ")

count = 0

try:
    with open(filename, "r") as file:
        print("\nMatching lines:\n")

        for line in file:
            if keyword in line:
                print(line.strip())
                count += 1

    print(f"\nTotal matches: {count}")

except FileNotFoundError:
    print("File not found.")
