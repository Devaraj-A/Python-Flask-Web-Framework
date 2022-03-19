from flask import Flask, render_template, request, redirect
import csv

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

#save data in txt
def extract(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\nEmail:{email},\nSubject:{subject},\nMessage:{message}\n')

#save data in csv
def extract2(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email,subject,message])

#contact form data
@app.route('/submit_form', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        extract2(data)
        return redirect('contact.html')
    else:
        print('error')
