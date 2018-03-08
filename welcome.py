import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def Welcome():
        return 'welcome here'


@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app !'
      
@app.route('/art')
def api_article():
    return 'You are reading '
    
port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=int(port))
~                                                                                             
~                                                                                             
~                                                                                             
~                                                                                             
"welcome.py" 19L, 381C                                                      7,0-1         All

