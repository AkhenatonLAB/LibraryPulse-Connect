import os
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = Flask(__name__)

# Firebase bağlantısını kur
cred = credentials.Certificate('serviceAccountKey.json')  # Firebase Admin SDK JSON dosyası
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL')  # .env dosyasındaki Firebase URL'sini kullan
})

@app.route('/get_people_count', methods=['GET'])
def get_people_count():
    ref = db.reference('number_of_people')  # Firebase'deki verinin yolu
    people_count = ref.get()  # Veriyi çekiyoruz
    return jsonify({"number_of_people": people_count}), 200

if __name__ == '__main__':
    app.run(debug=True)
