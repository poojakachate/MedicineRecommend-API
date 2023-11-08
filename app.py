from flask import Flask, request, render_template, jsonify
import csv

# Initialize the Flask app
app = Flask(__name__)

# Read the CSV file and populate the dictionary with 'utf-8' encoding
symptoms_and_medicines = {}

with open('medicine.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symptom = row['Reason']
        medicines = [medicine for medicine in row.values() if medicine and medicine != symptom]
        symptoms_and_medicines[symptom] = medicines

@app.route('/')
def index():
    # Render the HTML template and pass the symptoms data
    return render_template('mediAPIjs.html', symptoms_and_medicines=symptoms_and_medicines)

@app.route('/api/recommendations', methods=['POST'])
def recommend():
    data = request.get_json()
    selected_symptoms = data.get('symptoms')

    # Replace this with your recommendation logic
    recommended_medicine = []

    for symptom in selected_symptoms:
        if symptom in symptoms_and_medicines:
            recommended_medicine.extend(symptoms_and_medicines[symptom])

    return jsonify({"recommended_medicine": recommended_medicine})

if __name__ == '__main__':
    app.run(debug=True)
