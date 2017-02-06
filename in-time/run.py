from server import APP, environ

if __name__ == '__main__':
    APP.run(debug=environ['FLASK_DEBUG'])
