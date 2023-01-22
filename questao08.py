from flask import Flask, request

app = Flask(__name__)

count = {"counter": 0}


@app.post('/contador')
def new_value():
    value = request.get_json('numero')
    count["counter"] = value['numero']
    return "", 201


@app.get('/contador')
def get_value():
    return {'numero': count["counter"]}, 200


@app.put('/contador/incrementa')
def incrementa():
    count["counter"] += 1
    return '', 202


@app.delete('/contador')
def delete():
    count['counter'] = 0
    return '', 202


if __name__ == '__main__':
    app.run(debug=True)
