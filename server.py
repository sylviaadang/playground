from flask import Flask, render_template
app = Flask(__name__)


# def welcome():
#     return render_template('index3.html', repeat=3, color='blue')


# def more(num):
#     repeat = num
#     return render_template('index3.html', repeat=repeat, color='blue')
@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def color(num=3, color='blue'):
    repeat = num
    color = color
    return render_template('index3.html', repeat=repeat, color=color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True, host = 'localhost', port = 5000)    # Run the app in debug mode.
