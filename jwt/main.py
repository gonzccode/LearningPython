from flask import Flask, request, make_response, session, jsonify
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

##import uuid
##uuid.uuid4().hex
app.config['SECRET_KEY'] = 'af87a28216bd4e49a1bd241d4134ea69'


@app.route('/login', methods=['POST'])
def login():
    #print(request.data)
    #print(request.json.get('username'))
    #1 validar que esto estén en la base de datos
    if request.json.get('username') == 'gonzalo' and request.json.get('password') == '123456':
        #2 si se valida entonces la session es TRUE
        session['logged_in'] = True

        #3 se crea el token y tengo que pasar 2 valores el primer objeto y el secreteKey
        token = jwt.encode({
            'user': request.json.get('username'),
            'expiration': str(datetime.utcnow() + timedelta(seconds=120)),

        }, app.config['SECRET_KEY'])

        #jsonify convierte a json
        return jsonify({'token': token})
        #este token creado se debe enviar en cada solicitud para validar si está funcionando o no
        #esto se hace con decorator en cada endpoint

        """def check_token():
            pass
        
        @app.route('/private')
        @check_token
        def show_menus():
            return 'show dishes'
        """
    else:
        return make_response('Unable to verify', 403, {'Status': 'Invalid credentials'})


if __name__ == '__main__':
    app.run(debug=True)
#or comand flask --app main run --debug

