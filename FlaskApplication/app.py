from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./')

# Conversion functions
def kg_to_grams(kg):
    # 1 kg = 1000 grams
    return kg * 100

def grams_to_kg(grams):
    # 1 gram = 0.001 kg
    return grams * 0.001

def kg_to_pounds(kg):
    # 1 kg = 2.20462 pounds
    return kg * 2.20462

def pounds_to_kg(pounds):
    # 1 pound = 0.453592 kg
    return pounds * 0.453592

def grams_to_pounds(grams):
    # chain the functions together: grams -> kg -> pounds
    kg = grams_to_kg(grams)
    return kg_to_pounds(kg)

def pounds_to_grams(pounds):
    # chain the functions together: pounds -> kg -> grams
    kg = pounds_to_kg(pounds)
    return kg_to_grams(kg)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']

            if from_unit == to_unit:
                result = value
            elif from_unit == 'kg' and to_unit == 'grams':
                result = kg_to_grams(value)
            elif from_unit == 'grams' and to_unit == 'kg':
                result = grams_to_kg(value)
            elif from_unit == 'kg' and to_unit == 'pounds':
                result = kg_to_pounds(value)
            elif from_unit == 'pounds' and to_unit == 'kg':
                result = pounds_to_kg(value)
            elif from_unit == 'grams' and to_unit == 'pounds':
                result = grams_to_pounds(value)
            elif from_unit == 'pounds' and to_unit == 'grams':
                result = pounds_to_grams(value)
            else:
                result = "Invalid conversion"

            # results as strings
            if result is not "Invalid conversion":
                result = f"{value} {from_unit} is equal to {result} {to_unit}"
            
        except ValueError:
            result = "Invalid input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(port=8080, debug=False)