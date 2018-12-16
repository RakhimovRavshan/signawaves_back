from flask import Flask
from flask import request
from service import DocumentService
from flask import jsonify
from flask_cors import CORS
import sys

SUCCESS_STATUS = "success"

FAILED_STATUS = "failed"

app = Flask(__name__)
cors = CORS(app, resources={r"/api*": {"origins": "*"}})

ROOT_CONTEXT = "/api/1.0.0"


@app.route(ROOT_CONTEXT + "/documents/inbox")
def get_documents():
    try:
        documents = DocumentService.get_documents(request.args.get('seed'))
        return make_response(SUCCESS_STATUS, documents)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


@app.route(ROOT_CONTEXT + "/documents/outbox")
def get_documents_outbox():
    try:
        documents = DocumentService.get_documents_outbox(request.args.get('seed'))
        return make_response(SUCCESS_STATUS, documents)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


@app.route(ROOT_CONTEXT + "/document")
def get_document():
    try:
        document = DocumentService.get_document(request.args.get('id'))
        return make_response(SUCCESS_STATUS, document)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


@app.route(ROOT_CONTEXT + "/document/sign")
def sign_document():
    try:
        DocumentService.sign_document(request.args.get('id', 'seed'))

        return make_response(SUCCESS_STATUS)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


@app.route(ROOT_CONTEXT + "/main")
def get_counters():
    try:
        counters = DocumentService.get_counters(request.args.get('seed'))
        return make_response(SUCCESS_STATUS, counters)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


@app.route(ROOT_CONTEXT + "/files/send", methods=['POST'])
def send_file():
    try:
        seed = request.args.get('seed')
        data = request.get_json()
        print(data)
        tx_id = DocumentService.send_file(data, seed)
        return make_response(SUCCESS_STATUS, tx_id)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


def make_response(status, body):
    return jsonify({"header": {"status": status}, "body": body})


@app.route(ROOT_CONTEXT + "/files/download")
def download_file():
    try:
        tx_id = DocumentService.download_file(request.get_json())
        return make_response(SUCCESS_STATUS, tx_id)
    except:
        return make_response(FAILED_STATUS, sys.exc_info()[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
