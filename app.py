from flask import Flask, render_template, request, flash
from truecallerpy import search_phonenumber

app = Flask(__name__, static_folder = "static")
app.secret_key = "deep"

@app.route("/")
def index():
    indian = "Only Indian numbers supported !"
    return render_template("index.html", alert=indian)

def search_number(user_number):
    id = "a1i0i--cZbrxwVEFlUzHgOoZao-BD0og4Z5eajg7BSZA2VQycbi-i5jIC6cR0wZz"
    try:
        response = (search_phonenumber(user_number,"IN", id))
        try:
            data = response["data"][0]
            phone_name = data["name"]
            print("Name - ",data["name"])
            data2 = data["phones"][0]
            phone_carrier = data2['carrier']
            print("Carrier - ",data2['carrier'])
        except:
            phone_name = "Not on Truecaller"
            phone_carrier = "Not on Truecaller"

        final = [phone_name,phone_carrier]
        return final
    except:
        phone_name = "Value provided is not a number"
        phone_carrier = "Value provided is not a number"
        final = [phone_name,phone_carrier]
        return final

@app.route('/search', methods=["POST","GET"])
def search():
    user_number = str(request.form['name_input'])
    contact_info = search_number(user_number)

    phone_name = contact_info[0]
    phone_carrier = contact_info[1]

    return render_template("index.html", name=phone_name, carrier=phone_carrier)

app.run(host="0.0.0.0",port=0)
