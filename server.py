"""
CF/XSA Python buildpack app example
Author: Andrew Lunde
"""
from flask import Flask
from flask import request
from flask import Response

from flask import send_from_directory
#   
import os
import json
import datetime
from cfenv import AppEnv

from hdbcli import dbapi

import platform

app = Flask(__name__)
env = AppEnv()

# Get port from environment variable or choose 9099 as local default
# If you are testing locally (i.e. not with xs or cf deployments,
# Be sure to pull all the python modules locally 
#   with pip using XS_PYTHON unzipped to /tmp
# mkdir -p local
# pip install -t local -r requirements.txt -f /tmp
port = int(os.getenv("PORT", 9099))
hana = env.get_service(label='hana')

# This module's Flask webserver will respond to these three routes (URL paths)
# If there is no path then just return Hello World and this module's instance number
# Requests passed through the app-router will never hit this route.
@app.route('/')
def hello_world():
    output = '<strong>Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0)) + '</strong> Try these links.</br>\n'
    output += '<a href="/env">/env</a><br />\n'

    return output
    
# Satisfy browser requests for favicon.ico so that don't return 404
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/env')
def dump_env():
    output = '\nKey Environment variables... \n'
    output += 'PORT: ' + str(os.getenv("PORT", 0)) + '\n'
    output += 'PYTHONHOME: ' + str(os.getenv("PYTHONHOME", 0)) + '\n'
    output += 'PYTHONPATH: ' + str(os.getenv("PYTHONPATH", 0)) + '\n'

    app_json = str(os.getenv("VCAP_APPLICATION", 0))
    japp = json.loads(app_json)
    output += 'VCAP_APPLICATION: ' + json.dumps(japp, sort_keys=True, indent=4) + '\n'

    svcs_json = str(os.getenv("VCAP_SERVICES", 0))
    svcs = json.loads(svcs_json)
    output += 'VCAP_SERVICES: ' + json.dumps(svcs, sort_keys=True, indent=4) + '\n'

    if hana:
       if hana.credentials:
          output += 'host: ' + hana.credentials['host'] + '\n'
          output += 'port: ' + hana.credentials['port'] + '\n'
          output += 'user: ' + hana.credentials['user'] + '\n'
          output += 'pass: ' + hana.credentials['password'] + '\n'

    output += '\n'
    # return output # Defaults to mimetype='application/html'
    return Response(output, mimetype='text/plain' , status=200,)

if __name__ == '__main__':
    print(platform.python_version())
    # Run the app, listening on all IPs with our chosen port number
    # Use this for production 
    #app.run(host='0.0.0.0', port=port)
    # Use this for debugging 
    app.run(debug=True, host='0.0.0.0', port=port)

