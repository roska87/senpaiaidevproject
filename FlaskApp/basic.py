# import dependencies
import os
import io
from flask import Flask, render_template, jsonify, send_file
import model
from keras.preprocessing import image

"""
# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))


# our base route which just returns a string
@app.route('/')
def get():
    gen_img = model.predict()
    print(gen_img.shape)
    img = image.array_to_img(gen_img[0])
    file = io.BytesIO()
    img.save(file, 'png')
    file.seek(0)
    return send_file(
        file,
        as_attachment=True,
        attachment_filename='file.png',
        mimetype='image/png')


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
"""
