from flask import Flask, render_template, request, send_file
import pandas as pd
from werkzeug.utils import secure_filename
from geopy.geocoders import ArcGIS


nom=ArcGIS()

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success-table", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file = request.files.get(u'file')
        df = pd.read_csv(file)
        if "Address" in df.columns:
            df["Latitude"]=(df["Address"].apply(nom.geocode)).apply(lambda x : x.latitude if x != None else None)
            df["Longitude"]=(df["Address"].apply(nom.geocode)).apply(lambda x : x.longitude if x != None else None)
            df.to_csv(secure_filename("New_"+file.filename), index=False)
            return render_template("index.html", btn="download.html", tables=[df.to_html(index=False)])
        else:
            return render_template("index.html", text="Error: Please make sure you have an address column in your CSV file!")
        
@app.route("/download")
def download():
    return send_file("New_"+file.filename, attachment_filename="Your file.csv", as_attachment=True)    

if __name__=='__main__':
    app.debug=False
    app.run()    