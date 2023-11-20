from flask import Flask

app = Flask(__name__)



@app.route('/alkuluku/<int:luku>')
def onkoAlku(luku):
    onAlkuLuku = True

    if luku < 2:
        onAlkLuku = False


    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            onAlkuLuku = False
            break


    vastaus = {
        "Number" : luku,
        "isPrime": onAlkuLuku

    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)