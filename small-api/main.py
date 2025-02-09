from flask import Flask, request, jsonify
import random
import tools.sql_queries as sql


app = Flask(__name__)

@app.route('/')
def hello_world ():
    return 'Hello world!'

@app.route('/random_number')
def random_int ():
    return str(random.randint(0,10))

@app.route('/everything-employees')
def example():
    return jsonify(sql.get_everything())

@app.route('/table/<one_table>')
def any_table(one_table):
    return jsonify(sql.table_ten(one_table))

@app.route('/insert-into-employees', methods=["POST"])
def insert_by_passing_params ():

    id_ = request.args["emp_no"] # params.id_ = {}
    date = request.args["birth_date"]
    name = request.args["first_name"] 
    fname = request.args["last_name"] 
    gender = request.args["gender"] 
    date_2 = request.args["hire_date"] 

    sql.insert_params (id_, date, name, fname, gender, date_2)
    return "ok"

@app.route("/insert/<emp_no>/<birth_date>/<first_name>/<last_name>/<gender>/<hire_date>", methods = ["POST"])
def insert_one (the_table, emp_no, birth_date, first_name, last_name, gender, hire_date):
    sql.insert_one(the_table, emp_no, birth_date, first_name, last_name, gender, hire_date)
    return "Inserted!"

@app.route('/get-gerards')
def some_gerards():
    return jsonify(sql.gerards())


if __name__ == '__main__':
    app.run(port = 9000, debug = True)