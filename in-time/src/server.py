from application.flask_config import *
from api import *

if __name__ == '__main__':
    app.run(debug=os.environ['FLASK_DEBUG'])
