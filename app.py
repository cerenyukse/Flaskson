
import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'

@app.route('/predict',methods=['GET'])
def predict():
    from sklearn.externals import joblib
    model = joblib.load('mandariin.ml')
    

   

    predicted_health_score = model.predict([[int(request.args['gunluk_su']),
                                             int(request.args['gunluk_kutu_sekerli_icecek']),
                                             int(request.args['icecege_atilan_seker_adedi']),
                                             int(request.args['duzenli_beslenme']),
                                             int(request.args['saglikli_beslenme']),
                                             int(request.args['gunluk_fincan_kahve']),
                                             int(request.args['gunluk_cay_bardak']),
                                             int(request.args['gunluk_sigara_adet']),
                                             int(request.args['haftalik_alkol_bardak']),
                                             int(request.args['gunluk_dis_fircalama']),
                                             int(request.args['haftalik_dis_ipi']),
                           ]])
    return str(round(predicted_health_score[0],2))


if __name__ == "__main__":
    app.run(debug=True)


#http://127.0.0.1:5000/predict