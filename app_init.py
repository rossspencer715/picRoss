from flask import *

app = Flask(__name__)

@app.route('/') #decorator
def root():
    grid = [[f"{i}" for i in range(5)] for _ in range(5)]
    return render_template('main.html', grid=grid)
 
@app.route('/check', methods = ["POST"])
def calculate():     
       data = request.form
       
       return render_template('main.html', grid=grid) 
       
         
if __name__ == '__main__':
       app.run(debug = True)