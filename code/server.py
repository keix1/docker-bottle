from bottle import route, run

@route('/hello/<user>')
def hello(user="taro"):
    return "Hello {user}".format(user=user)

@route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
    return "{month}/{day} {path}".format(month=month, day=day, path=path)

@route('/')
def hello():
    return "Heaalloiiiiii Wor!aaaaa!\n"

@route('/test')
def test():
    return "test"

run(host='0.0.0.0', port=8080, debug=True)
