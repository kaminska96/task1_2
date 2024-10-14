from flask import Flask, request, render_template
import zeep

app = Flask(__name__)

wsdl_name = "https://apps.learnwebservices.com/services/hello?WSDL"
client_name = zeep.Client(wsdl=wsdl_name)

wsdl_text = "https://www.dataaccess.com/webservicesserver/TextCasing.wso?WSDL"
client_text = zeep.Client(wsdl=wsdl_text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name'].strip()
    case_option = request.form.get('case_option', 'no_change')

    message = client_name.service.SayHello(name)

    if case_option == 'lower_case':
        message = client_text.service.AllLowercaseWithToken(message, "")
        
    elif case_option == 'upper_case':
        message = client_text.service.AllUppercaseWithToken(message, "")
        
    elif case_option == 'invert_case':
        message = client_text.service.InvertStringCase(message)

    return render_template('index.html', name=name, message=message, case_option=case_option)

if __name__ == '__main__':
    app.run(debug=True)