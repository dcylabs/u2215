#!/usr/local/bin/python3
import io
import os
import zipfile
from flask import Flask, request, send_file, make_response

app = Flask(__name__)
directory = "/workdir/data"

@app.route('/handle')
def handle_request():
    domain = request.args.get('athack_domain')
    path = request.args.get('athack_path')
    filename = request.args.get('athack_filename')

    # Validate required parameters
    if not domain or not path or not filename:
        return 'Missing parameters', 400
 
    # Generate the zip file in memory
    zip_data = io.BytesIO()
    with zipfile.ZipFile(zip_data, 'w') as zip_file:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):  # Process only files, not directories
                # Read the content of the file
                with open(filepath, 'r') as file:
                    content = file.read()
                
                # Replace the word "__TOCHANGE__" with "REPLACED"
                updated_content = content
                updated_content = updated_content.replace('__ATHACK_DOMAIN__', domain)
                updated_content = updated_content.replace('__ATHACK_PATH__', path)
                updated_content = updated_content.replace('__ATHACK_FILENAME__', filename)

                zip_file.writestr(filename, updated_content)

    # Set the zip data position to the beginning
    zip_data.seek(0)

    # Create a response with the zip file data
    response = make_response(zip_data.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'application/zip'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
