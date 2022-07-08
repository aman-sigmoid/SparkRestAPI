from query import *
from flask import *
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'

# Query_1
@app.route("/api_1")
def api_1():
    data = query_1()
    return jsonify(data)

# Query_2
@app.route("/api_2")
def api_2():
    data = query_2()
    return jsonify(data)

# Query_3
@app.route("/api_3")
def api_3():
    data = query_3()
    return jsonify(data)

# Query_4
@app.route("/api_4")
def api_4():
    data = query_4()
    return jsonify(data)

# Query_5
@app.route("/api_5")
def api_5():
    data = query_5()
    return jsonify(data)

# Query_6
@app.route("/api_6")
def api_6():
    data = query_6()
    return jsonify(data)

# Query_7
@app.route("/api_7")
def api_7():
    data = query_7()
    return jsonify(data)

# Query_8
@app.route("/api_8")
def api_8():
    data = query_8()
    return jsonify(data)

# Query_9
@app.route("/api_9")
def api_9():
    data = query_9()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)