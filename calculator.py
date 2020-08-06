from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('calculator.html')

def addition(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = addition(var_1, var_2)
    elif(operation == 'Subtraction'):
        result = subtract(var_1, var_2)
    elif(operation == 'Multiplication'):
        result = multiplication(var_1, var_2)
    elif(operation == 'Division'):
        result = division(var_1, var_2)
    else:
        result = 'INVALID CHOICE'
    # entry = result
    return render_template('result.html', entry=result)

if __name__ == '__main__':
    app.run(debug=True)
