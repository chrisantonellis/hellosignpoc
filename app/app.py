import flask
import hellosign_sdk
import pprint
import json


# create app
app = flask.Flask(__name__)

# configure app
app.config.from_pyfile("/app/config.py")

# create hellosign api client
hsclient = hellosign_sdk.HSClient(api_key=app.config["HELLOSIGN_API_KEY"])


# helper functions -------------------------------------------------------------

def json_response(body):
    response = flask.Response(json.dumps(body))
    response.headers["Content-Type"] = "application/json"
    return response
    
def update_object(obj, data):
    for key, value in data.items():
        setattr(obj, key, value)


# routes -----------------------------------------------------------------------

# root

@app.route("/")
def hello_world():
    return "Hello, World!"
    
# webhooks (callbacks)

# TODO: ngrok stuff
@app.route("/applications/webhooks")
def hellosign_applications_webhooks():
    pass

# account
    
@app.route("/account", methods=["GET"])
def hellosign_account_read():
    account_info = hsclient.get_account_info()
    
    return json_response(account_info.json_data)
    
@app.route("/account", methods=["POST"])
def hellosign_account_update():
    request_data = json.loads(flask.request.data)
    account_info = hsclient.get_account_info()
    
    update_object(account_info, request_data)
    hsclient.update_account_info()
    
    return json_response(account_info.json_data)


# run app ----------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
