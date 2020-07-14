from flask import Flask,render_template,request,wrappers
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def calc():
	bmi = ''
	if request.method == 'POST' and 'weight' in request.form:
		weight = float(request.form.get('weight'))
		height = float(request.form.get('height'))
		bmi = calc_bmi(weight,height)

	response = wrappers.Response(render_template("index.html", bmi=bmi))
	response.headers['Cache-Control']= 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	response.headers['max-age']= '0'
	return response
	# return render_template("index.html", bmi=bmi)

def calc_bmi(weight,height):
	return round((weight/((height/100)**2)), 2)

app.run()
