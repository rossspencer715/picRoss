from flask import Flask, request, render_template
import random

app = Flask(__name__)
GRIDLENGTH = 5
GRIDWIDTH = 5
NRAND = 10
grid = [[0 for i in range(5)] for _ in range(GRIDLENGTH)]
gridGuess = [[0 for i in range(5)] for _ in range(GRIDWIDTH)]
# area = (GRIDLENGTH*GRIDWIDTH)


def initGrid():
    global grid
    global gridGuess
    for i in range(NRAND):
        randRow = random.randrange(GRIDLENGTH)
        randCol = random.randrange(GRIDWIDTH)
        grid[randRow][randCol] = 1
        gridGuess[randRow][randCol] = -1 if randRow < GRIDLENGTH//2 else 1


@app.route('/', methods=['GET','POST'])
def root():
    global gridGuess
    if request.method == 'POST':
        try:
            boxName = request.form.get("box_name")
            boxNum = int(boxName[3:])
            row = boxNum // 10
            col = boxNum % 10
            if grid[row][col] == 1:
                gridGuess[row][col] = 1
            else:
                gridGuess[row][col] = -1
            return render_template('main.html', grid=gridGuess)
        except Exception as e:
            print(e)
    return render_template('main.html', grid=gridGuess)
      
         
if __name__ == '__main__':
    initGrid()
    app.run(debug = True, host='0.0.0.0', port=80)