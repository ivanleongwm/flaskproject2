import datetime
from flask import Flask, render_template, request
import json


app = Flask(__name__)
#client = MongoClient(r"mongodb+srv://ivanleongwm:Ivan1904@microblog-application.utvq0.mongodb.net/test")
#app.db = client.microblog
entries = []

@app.route("/", methods=["GET","POST"])
def home():
    #print([e for e in app.db.entries.find({})])
    if request.method == "POST":
        entry_content0 = request.form.get("content0")
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content0,entry_content,formatted_date))

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[2],"%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]

    color = ['Red','Black','Blue','Orange']

    dictionary = {
        'Vincent':[["SPPSG Recon","Nexus Script to automate posting of JE"],["Lumos Query Error","Fixing of syntax errors in lumos"]],
        'Tiffany':[["Invoice generator","Using python and vba to generate invoices"],["File Lag","Aggregated rows"]]
    }

    javascript_data = [1,"foo"]

    return render_template("home.html", entries=entries_with_date, colours=color, dictionary=dictionary, data=json.dumps(javascript_data), dictionary2=dictionary)

