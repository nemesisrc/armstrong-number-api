from flask import Flask
from flask import render_template, jsonify, request


app= Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/armstrongnumber/<int:number>')
def check_armstrong(number):
    # Convert the number to a string to calculate the number of digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum equals the original number and return final result accordingly
    if armstrong_sum == number:
        return render_template('armstrong-number-positive.html')
    else:
        return render_template('armstrong-number-negative.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)