from flask import Flask, render_template,request,redirect
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
  
app = Flask(__name__)

API_KEY = 'ENTER-YOUR-API-KEY'
  
 
    
@app.route('/Currency', methods=['GET', 'POST'])
def bank():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            from_c = request.form['from_c']
            to_c = request.form['to_c']
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
                from_c, to_c, API_KEY)
            response = requests.get(url=url).json()
            rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
            rate = float(rate)
            result = rate * amount
            from_c_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
            from_c_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
            to_c_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
            to_c_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
            time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
            return render_template('Currency_Convertor_app.html', result=round(result, 2), amount=amount,
                                   from_c_code=from_c_code, from_c_name=from_c_name,
                                   to_c_code=to_c_code, to_c_name=to_c_name, time=time)
            return redirect('/')
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
    else:
        return render_template('Currency_Convertor_app.html')

    
@app.route('/')
def home():
    try:
        var=pd.read_excel('F:\IT-VEDANT-INSTITUTE\UIAI Technologies LLP\Python developer - Currency_Conversion_Test_Data\Currency_Conversion_Test_Data\Consolidated_Exchange_Rate_file.xlsx')
        var.head()
        print("Sum: ",var["Production"].sum())
        print("Mean: ",var["Production"].mean())
        print("Maximum: ",var["Production"].max())
        print("Minimum: ",var["Production"].min())
        plt.show()
        
        return render_template('Currency_Code_Conversion_Calculation.html')
    except Exception:
        print("The error is",Exception)
    
    

  
if __name__ == "__main__":
    app.run(debug=True)
