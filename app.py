from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(features):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict([features])
    return pred[0]

@app.route('/', methods=['GET', 'POST'])
def index():
    pred_value = None
    form_data = {}  

    if request.method == 'POST':
        form_data = request.form.to_dict() 

        brand = form_data['brand']
        transmission = form_data['transmission']
        fuel_type = form_data['fuel_type']
        color = form_data['color']
        engine_cc = form_data['engine_cc']
        mileage_kmpl = form_data['mileage_kmpl']
        make_year = form_data['make_year']
        owner_count = form_data['owner_count']
        service_history = form_data['service_history']
        insurance_valid = form_data['insurance_valid']

        feature_list = [
            int(make_year),
            float(mileage_kmpl),
            int(engine_cc),
            int(owner_count)
        ]

        def traverse_list(lst, value):
            for item in lst:
                feature_list.append(1 if item == value else 0)

        brand_list = ['BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Nissan', 'Tesla', 'Toyota', 'Volkswagen']
        transmission_list = ['Automatic', 'Manual']
        fuel_type_list = ['Diesel', 'Electric', 'Petrol']
        color_list = ['Black', 'Blue', 'Gray', 'Red', 'Silver', 'White']
        service_history_list = ['Full', 'Partial']
        insurance_valid_list = ['No', 'Yes']

        traverse_list(fuel_type_list, fuel_type)
        traverse_list(brand_list, brand)
        traverse_list(transmission_list, transmission)
        traverse_list(color_list, color)
        traverse_list(service_history_list, service_history)
        traverse_list(insurance_valid_list, insurance_valid)

        predicted_price = prediction(feature_list)
        pred_value = "${:,.2f}".format(predicted_price)

    return render_template("index.html", pred_value=pred_value, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
