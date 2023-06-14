#!/usr/local/bin/python3
from urllib.parse import urlparse, urlencode
from flask import Flask, request, Response
import requests
import base64
import os

#---------- OS ENV VAR READ ----------#
athack_default_target = os.getenv('ATHACK_DEFAULT')
if athack_default_target is None:
    athack_default_target = 'http://localhost:8000'

athack_handle_target = os.getenv('ATHACK_HANDLE')
if athack_handle_target is None:
    athack_handle_target = 'http://localhost:9000/athack_handle'

#---------- FLASK FORWARD SERVER ----------#
app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def forward_request(path):
    try:
        req_headers = dict(request.headers)
        req_headers.pop("Host", None)

        # Get the target URL for forwarding
        target_url = athack_default_target + '/' + path

        # Get the Basic Authorization header from the request
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_type, encoded_credentials = auth_header.split(' ')
            if auth_type.lower() == 'basic':
                credentials = base64.b64decode(encoded_credentials).decode('utf-8')
                username, password = credentials.split(':')
                if "\u2215" in username:
                    parsed = urlparse("http://" + "/".join(username.split("\u2215")) + "@" + request.host + request.path)
                    domain = parsed.netloc
                    path = parsed.path.strip("/")
                    _, filename = os.path.split(path)
                    filename = filename.split(":")[0]
                    params = {"athack_domain": domain, "athack_path": path, "athack_filename": filename}
                    target_url = athack_handle_target + "?" + urlencode(params)

        print(f"Forward to: {target_url}")
        # Forward the request to the target URL
        if request.method == 'GET':
            response = requests.get(target_url,headers=req_headers, stream=True, allow_redirects=False)

            response.headers.pop('Content-Encoding', None)
            response.headers.pop('Transfer-Encoding', None)

            # Manually forward the response without chunked encoding
            headers = list(response.headers.items())

            content = b''.join(response.iter_content(chunk_size=1024))

            # Pass the response back to the client
            return Response(content, headers=headers)

        elif request.method == 'POST':
            response = requests.post(target_url, headers=req_headers, data=request.data, allow_redirects=False)

            # Pass the response received from the target server back to the client
            return response.content, response.status_code, response.headers.items()

    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    print(f" - DEFAULT: {athack_default_target} / HANDLE: {athack_handle_target}")
    app.run(host='0.0.0.0', port=80)
