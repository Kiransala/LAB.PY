import os

user = False

while not user:
    choice = int(input("\n\n1.To read the content of file and write it in another file.\n2.To append data to existing file and then display the entire file.\n3.To count the number of lines, words and characters in a file.\n4.To display file available in current directory\n5.Exit.\nEnter Your Choice: "))

    if choice == 1:
        f = open("demofile.txt", "w")
        ch = 0
        while (ch != 1):
            msg = input("Enter a line: ")
            f.write(msg + "\n")
            ch = int(input("1 for exit: "))
        f.close()
        f = open("demofile.txt", "r")
        f1 = open("writefile.txt", "w")
        msg = f.read()
        f1.write(msg)
        f.close()
        f1.close()

    elif choice == 2:
        f1 = open("writefile.txt", "a")
        inp = input("Enter the line to be appended: ")
        f1.write(inp)
        f1.close()

        f1 = open("writefile.txt", "r")
        msg = f1.read()
        print(msg)
        f1.close()

    elif choice == 3:
        lc, wc, cc = 0, 0, 0
        f1 = open("writefile.txt", "r")
        for l in f1:
            lc += 1
            wc += len(l.split())
            cc += len(l)

        print(lc, "::", wc, "::", cc)
        f1.close()
    
    elif choice == 4:
        for path, dirn, filen in os.walk("."):
            print(filen)

    elif choice == 5:
        user = True

    else:
        print("Invalid Choice")
