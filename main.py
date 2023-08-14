from flask import Flask, jsonify, request
import csv
allmovies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    #print(len(reader))
    data = list(reader)    
    allmovies = data[1:]

likemovies = []
notlikemovies = []
notwatchedmovies = []

app = Flask(__name__)

@app.route('/getmovie')
def getmovie():
    return jsonify({
        'data': allmovies[0],
        'status': 'success'
    })

@app.route('/likemovie', methods = ['POST'])
def likemovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    likemovies.append(movie)
    return jsonify({
        'status': 'success'
    }), 201

@app.route('/notlikemovie', methods = ['POST'])
def notlikemovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notlikemovies.append(movie)
    return jsonify({
        'status': 'success'
    }), 201

@app.route('/notwatchedmovie', methods = ['POST'])
def notwatchedmovie():
    movie = allmovies[0]
    allmovies = allmovies[1:]
    notwatchedmovies.append(movie)
    return jsonify({
        'status': 'success'
    }), 201

if __name__ == '__main__':
    app.run()