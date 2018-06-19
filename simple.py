from flask import Flask,render_template,request
app=Flask(__name__)
 
@app.route('/')
def expenses():
   return render_template('details.html')

@app.route('/saved/<float:savings>' ,methods=['POST' ,'GET'])
def saved(savings):
   if request.method=='POST':
      savings=request.form['salary']- (request.form['houserent']+request.form['food']+request.form['travelcharges'])
   return render_template('saved.html',saved = savings)

if __name__=='__main__':
   app.run(debug=True)
