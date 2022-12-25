from flask import Flask, request, render_template
import random

app = Flask(__name__)
GRIDLENGTH = 5
GRIDWIDTH = 5
NRAND = 10
# area = (GRIDLENGTH*GRIDWIDTH)
colHint = ["1-3","2","3","4","5"]

def initGrid():
    global grid
    global gridGuess
    grid = [["0" for i in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]
    gridGuess = [["0" for i in range(GRIDWIDTH)] for _ in range(GRIDLENGTH)]

    for i in range(NRAND):
        # intentionally letting some points potentially
        # overwrite the same box to add variability
        randRow = random.randint(0, GRIDLENGTH-1)
        randCol = random.randint(0, GRIDWIDTH-1)
        grid[randRow][randCol] = "1"
        gridGuess[randRow][randCol] = "2"
    print("grid is:\n")
    for row in grid:
        print(row)
    print("gridGuess is:\n")
    for row in gridGuess:
        print(row)



@app.route('/', methods=['GET','POST'])
def root():
    global gridGuess
    if request.method == 'GET':
        initGrid()
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
            return render_template('main.html', grid=gridGuess, colHint=colHint)
        except Exception as e:
            print(e)
    return render_template('main.html', grid=gridGuess, colHint=colHint)
      
         
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)