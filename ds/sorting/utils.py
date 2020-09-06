def printFormattedData(file,data):
    try:
        for i in data:
            file.write(str(i)+",")
            file.write("\n")
    except Exception as e:
        print(e)