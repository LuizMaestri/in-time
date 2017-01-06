from application.flask_config import *


@app.route('/')
def index():
    return "index page"

if __name__ == '__main__':
    app.run(debug=os.environ['FLASK_DEBUG'])
