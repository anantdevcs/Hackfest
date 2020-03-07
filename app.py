from flask import Flask, escape, request, render_template
from flask import  request,render_template,redirect,url_for,jsonify
import os
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/static/images"

@app.route('/')
def hello():
    
    return render_template('index.html')

@app.route('/upload-image',methods=['GET','POST'])

def upload():
	if request.method == "POST":
		if request.files:

		            image = request.files["file"]

		            image.save(image.filename)

		            print("Image saved")

		            return redirect(request.url)
	else:
		return render_template('index.html')	            
app.run(debug=True)