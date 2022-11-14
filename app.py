import pickle
import numpy as np
from sklearn.svm import SVC
from flask import *

app = Flask(__name__)

with open('SVM.pickle', 'rb') as f:
    model = pickle.load(f)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        X = []
        X_new = []
        X_new.append(request.form['plen'])
        X_new.append(request.form['pwid'])
        X_new.append(request.form['slen'])
        X_new.append(request.form['swid'])
        X.append(X_new)
        result = model.predict(X)
        return render_template('predict.html', result=result, X=X)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
