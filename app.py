# from flask import Flask, render_template, request
# import requests   # ✅ ADD THIS LINE

# app = Flask(__name__)

# # 🏠 HOME PAGE
# @app.route('/')
# def home():
#     return render_template("index.html")

# # 📞 CONTACT PAGE
# @app.route('/contact')
# def contact():
#     return render_template("contact.html")

# # 📅 APPOINTMENT PAGE
# @app.route('/appointment')
# def appointment():
#     return render_template("appointment.html")

# # 📩 CONTACT FORM SUBMIT
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']

#     url = "https://api.web3forms.com/submit"

#     data = {
#         "access_key":"58594d35-47a2-4b83-96f4-4189cbade72d",
#         "name": name,
#         "email": email,
#         "message": message,
#         "subject": "New Contact Form Submission"
#     }

#     response = requests.post(url, data=data)
#     result = response.json()

#     if result.get("success"):
#         return "✅ Thanks for your submission!"
#     else:
#         return f"❌ Error: {result.get('message', 'Something went wrong')}"

# # ▶️ RUN APP (ALWAYS LAST)
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "super_secret_key_for_session" # Required for flash messages

# 🏠 HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")

# 📞 CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template("contact.html")

# 📅 APPOINTMENT PAGE
@app.route('/appointment')
def appointment():
    return render_template("appointment.html")

# 📩 CONTACT FORM SUBMIT
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    url = "https://api.web3forms.com/submit"

    # The payload for Web3Forms
    data = {
        "access_key": "58594d35-47a2-4b83-96f4-4189cbade72d",
        "name": name,
        "email": email,
        "message": message,
        "subject": "New Contact Form Submission"
    }

    try:
        response = requests.post(url, data=data)
        result = response.json()

        if result.get("success"):
            # Redirect back to home with a success message
            return "<h1>✅ Success!</h1><p>Thanks for your submission. <a href='/'>Go Back</a></p>"
        else:
            return f"<h1>❌ Error</h1><p>{result.get('message')}</p>"
            
    except Exception as e:
        return f"<h1>❌ Connection Error</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True)
