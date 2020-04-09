def fileExt():
    fileName = input("Enter the filename: ")
    splitName = fileName.split(".")
    extension = splitName[1]
    print("Your file extension is '" + str(extension) + "'")
