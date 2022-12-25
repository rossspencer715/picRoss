from flask import Flask, request, render_template
import random

app = Flask(__name__)
GRIDLENGTH = 5
GRIDWIDTH = 5
NRAND = 10
gridGuess = [[None for _ in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]
grid = [[None for _ in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]
colHints = []
rowHints = []

def initGrid():
    global grid, gridGuess

    grid = [["0" for i in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]
    gridGuess = [["0" for i in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]

    for i in range(NRAND):
        # intentionally letting some points potentially
        # overwrite the same box to add variability
        randRow = random.randint(0, GRIDLENGTH-1)
        randCol = random.randint(0, GRIDWIDTH-1)
        grid[randRow][randCol] = "1"
        # gridGuess[randRow][randCol] = "2"
    print("grid is:\n")
    for row in grid:
        print(row)
    print("gridGuess is:\n")
    for row in gridGuess:
        print(row)


def refreshHints():
    global grid, colHints, rowHints
    colHints = [""]
    for j in range(GRIDLENGTH):
        colStr = ""
        count = 0
        for i in range(GRIDWIDTH):
            if grid[i][j] != "0":
                count += 1
            elif count > 0:
                colStr += str(count)
                count = 0
        if count > 0:
                colStr += str(count)
        count = 0
        colHints.append(colStr)
    rowHints = []
    for i in range(GRIDWIDTH):
        rowStr = ""
        count = 0
        for j in range(GRIDLENGTH):
            if grid[i][j] != "0":
                count += 1
            elif count > 0:
                rowStr += str(count)
                count = 0
        if count > 0:
                rowStr += str(count)
        count = 0
        rowHints.append(rowStr)


@app.route('/', methods=['GET','POST'])
def root():
    global gridGuess
    if request.method == 'GET':
        initGrid()
        refreshHints()
    else:
        try:
            boxName = request.form.get("box_name")
            print(boxName)
            boxNum = int(boxName[3:])
            print(boxNum)
            rowIdx = boxNum // 10
            colIdx = boxNum % 10
            print(rowIdx, colIdx)
            print("grid is:\n")
            for row in grid:
                print(row)
            print("gridGuess is:\n")
            for row in gridGuess:
                print(row)
            if grid[rowIdx][colIdx] == "1":
                gridGuess[rowIdx][colIdx] = "1"
            else:
                gridGuess[rowIdx][colIdx] = "2"
            return render_template('main.html', grid=gridGuess, colHints=colHints, rowHints=rowHints)
        except Exception as e:
            print(e)
    return render_template('main.html', grid=gridGuess, colHints=colHints, rowHints=rowHints)
      
         
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)