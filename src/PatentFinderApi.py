# coding=utf-8
"""
Author : AAYUSH KUMAR
Created on : 05/02/2018 4:17 PM
"""
import json
import os
import sys
import logging
import re
from pathlib import Path
from PatentFinder import PatentFinder
parent_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
sys.path.append(parent_dir)
from flask import Flask, request, make_response, jsonify,Response
from util.ConfigReader import ConfigReader
from util.LogUtil import LogUtil
app = Flask(__name__)
config = ConfigReader()
host = config.getConfig("API", "host")
port = config.getConfig("API", "port")
global custom_dict 
patent_repo = config.getConfig("API", "patent_repo")
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logUtil = LogUtil()

@app.errorhandler(404)
def not_found(error):
    """
    Handles page not found error
    :param error:
    :return:
    """
    logUtil.debug("Page Not Found error occurred..")
    return make_response(jsonify({'error': 'Page not found'}), 404)


@app.route('/', methods=['POST'])
def index_route():
    return jsonify({
        'author': 'Aayush Kumar',
        'author_url': '***',
        'base_url': '***',
        'project_name': 'PATENT API',
        'project_url': '***',
        'project_issues': '***',
        'endpoints': {
            'Search the status of a given Patent':'/api/v1/patent/status'
        },
        'payload':{"id":"Pass your reference id"}
})

@app.route("/api/v1/patent/status", methods=['POST'])
def checkStatus():
    """
    API to train data, create model file and push the metadata to MongoDB
    :return:
    """
    try:
        logUtil.debug("Entering the status finder API...")
        request_data = request.get_json()
        
        if not request_data.get('id'):
            logUtil.debug("Invalid JSON format...")
            return json.dumps({"outputtext": "invalid json format."})

        # in future may be needed 
        # elif not request_data.get('email'):
        #     return json.dumps({"outputtext": "invalid json format."})
            
        
        else:
            logUtil.debug("JSON format validation successful...")
            patent_finder = PatentFinder(patent_repo)
            status = patent_finder.get_status(request_data['id'])
            patent_status = json.dumps(status)
            return Response(patent_status, status=200, mimetype='application/json')

    except KeyError as e:
        print e
        logUtil.error(e)
        return json.dumps({"outputtext": "Expected key {}".format(e)}), 400
    except ValueError as e:
        print e
        logUtil.error(e)
        return json.dumps({"outputtext": "ValueError"}), 400
    except Exception as e:
        print e
        logUtil.error(e)
        return json.dumps({"outputtext": "{}".format(e)}), 500

if __name__ == "__main__":
    logUtil.debug('Patent status Bot started...')
    app.debug = True
    print "Patent status application started on:",host,port
    app.run(host=host, port=int(port), use_reloader=False, threaded=True)
    

