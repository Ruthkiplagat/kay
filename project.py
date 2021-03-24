def drawField(field):
    for row in range(5):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow],end ="")
                    else:
                         print(field[practicalColumn][practicalRow])
                else:
                    print("|", end = "")
        else:
            print("------")
Player = 1
currentField = [[" "," "," "],[ " "," "," "],[" "," "," "]]
drawField(currentField)
while(True):
    print("Players turn:",Player)
    moveRow = int(input("Please enter the Row\n"))
    moveColumn = int(input("please enter the column\n"))
    if Player == 1:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "x"
            Player = 2
    else:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "o"
            Player = 1
    drawField(currentField)





