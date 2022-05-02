from src.transSheet import sheet

cols = int(input("Enter the number of columns of data: "))
names = input("Enter the names of the columns: ").split()
rows = int(input("Enter the number of rows of data: "))

thisSheet = sheet(cols, rows, names)
for i in range(0, cols):
    print(thisSheet.table[i].name)
