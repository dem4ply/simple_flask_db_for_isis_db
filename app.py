from flask import Flask
from flask import request, render_template
from werkzeug.utils import secure_filename
import csv
import os
from iris import insert_from_file

app = Flask(__name__)
app.config[ 'UPLOAD_FOLDER' ] = 'files'


@app.route( '/', methods=[ 'GET','POST' ] )
def upload_file( filename=None, column=None, data=None ):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)

        if file:
            file_name = secure_filename( file.filename )
            file_path = os.path.join(
                app.config[ 'UPLOAD_FOLDER' ], file_name )
            file.save( file_path )
            insert_from_file( file_path, ignore_pks=True )

    return render_template( 'index.html' )
