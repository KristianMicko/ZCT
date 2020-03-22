from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import mysql.connector as MYSQL
app = Flask(__name__)
CORS(app)



@app.route('/', methods=['POST'])
def autorize():
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("SELECT Meno, Heslo from prihlasenie")
	result = cursor.fetchall()
	autorizovanie = request.get_json()
	dict_autorizovanie = dict(autorizovanie)
	for i in result:
		if i[0] == dict_autorizovanie['login'] and i[1] == dict_autorizovanie['password']:
			cursor.close()
			myDb.close()
			return jsonify("Success"),200
		else:
			cursor.close()
			myDb.close()
			return jsonify("Not allowed"),401

@app.route('/data', methods=['GET'])			
def show():
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("SELECT *from data")
	result = cursor.fetchall()
	cursor.close()
	myDb.close()
	vysledok = []
	for i in result:
		vysledok.append('{'+'"id":{},"zamestnanci":"{}","pozicia":"{}","zaciatok":"{}","posledny":"{}","email":"{}","vek":{},"adresa":"{}","karta":"{}"'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])+'}')
	vys = []
	for k in range(len(vysledok)):
		vys.append(eval(vysledok[k]))
	return jsonify(vys),200

@app.route('/data/<id>', methods=['GET'])
def show_sel(id):
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("SELECT *from data where id="+id)
	result = cursor.fetchall()
	cursor.close()
	myDb.close()
	vysledok = []
	for i in result:
		vysledok.append('{'+'"id":{},"zamestnanci":"{}","pozicia":"{}","zaciatok":"{}","posledny":"{}","email":"{}","vek":{},"adresa":"{}","karta":"{}"'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])+'}')
	vys = []
	for k in range(len(vysledok)):
		vys.append(eval(vysledok[k]))
	return jsonify(vys),200
	
@app.route('/data/<id>', methods=['PUT'])
def update(id):
	data = request.get_json()
	data_dict = dict(data)
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("UPDATE data set ID={}, zamestnanci='{}', pozicia='{}', zaciatok='{}', posledny='{}', email='{}', vek={}, adresa='{}', karta='{}' where ID={}".format(data_dict['ID'],data_dict['zamestnanci'],data_dict['pozicia'],data_dict['zaciatok'],data_dict['posledny'],data_dict['email'],data_dict['vek'],data_dict['adresa'],data_dict['karta'],id))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Updated"),200

@app.route('/data/<id>', methods=['DELETE'])	
def delete(id):
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("DELETE FROM data where id={}".format(id))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Deleted"),204

	
@app.route('/data', methods=['POST'])
def create():
	data = request.get_json()
	data_dict = dict(data)
	myDb = MYSQL.connect(host="192.168.99.100", user="root", passwd="", database="zct")
	cursor = myDb.cursor()
	cursor.execute("INSERT INTO data(zamestnanci, pozicia, zaciatok, posledny, email, vek, adresa, karta) values('{}','{}','{}','{}','{}',{},'{}','{}')".format(data_dict['zamestnanci'],data_dict['pozicia'],data_dict['zaciatok'],data_dict['posledny'],data_dict['email'],data_dict['vek'],data_dict['adresa'],data_dict['karta']))
	myDb.commit()
	cursor.close()
	myDb.close()
	return jsonify("Created"),201