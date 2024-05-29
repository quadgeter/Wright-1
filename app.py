from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        cust_name = request.form.get('name')
        cust_email = request.form.get('email')
        cust_phone = request.form.get('phone_number')
        message = request.form.get('comment')
        
        print(cust_name, cust_email, cust_phone, message)
        
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        text = f"""============\nCustomer Lead Generated From https://quadgeter.github.io/Wright-1/\n==============\nCustomer Name: {cust_name}\nCustomer Email: {cust_email}\nCustomer Phone: {cust_phone}\nService Message: {message}\n=========="""
        
        msg = MIMEMultipart()
        msg['Subject'] = "Customer Lead"
        msg['From'] = 'wright1automatedservice@gmail.com'
        msg['To'] = 'quadgeter@gmail.com'
        msg.attach(MIMEText(text))
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.ehlo() 
        s.starttls() 
        s.login('wright1automatedservice@gmail.com', 'wndw somm klla xide')
        
        s.sendmail(from_addr='wright1automatedservice@gmail.com', to_addrs='wright1contractors@gmail.com', msg=msg.as_string())
        s.quit()
        
        
    
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')
    

if __name__ == "__main__": 
    app.run(debug=True)
