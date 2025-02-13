# Use flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        req = request.get_json()
        intent_name = req["queryResult"]["intent"]["displayName"]
        age = req['queryResult']['parameters'].get('age')
        age = int(age)
        gender = req['queryResult']['parameters'].get('gender')
        height = req['queryResult']['parameters'].get('height')
        weight = req['queryResult']['parameters'].get('weight')
        
        weight = weight['amount']

        if height and weight:
            height_m = height / 100  # Convert cm to meters
            bmi = round(weight / (height_m ** 2), 2)  # Calculate BMI and round to 2 decimal places

            # Categorize BMI
            if bmi < 18.5:
                category = "Underweight.So be careful you need to gain weight with healthy diet and consult your docter!"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight.Don't worry you are healthy!"
            elif 25 <= bmi < 29.9:
                category = "Overweight.You need to lose weight but it's not impossible you can do it!"
            else:
                category = "Obese.You need to lose weight immediately and also consult your docter!"

            response_text = f"You are a {age}-year-old {gender}, {height} cm tall, and weigh {weight} kg. Your BMI is {bmi}, which is considered {category}"
        else:
            response_text = "I need both height and weight to calculate your BMI."

        return jsonify({"fulfillmentText": response_text})
    return render_template('chatbot.html')


if __name__ == '__main__':
    app.run(port=7000, debug=True)