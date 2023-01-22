from flask import Flask, request


app = Flask(__name__)

@app.route('/soma', methods=['POST']) 
def soma():
    num= request.get_json()
    x = num['x']
    y = num['y']
    resultado= x + y
    return {"Resultado": resultado}, 200


if __name__ == '__main__':
    app.run(debug=True)
