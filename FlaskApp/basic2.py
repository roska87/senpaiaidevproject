# import dependencies
import os
from flask import Flask, render_template, jsonify, send_file
from flask_restplus import Api, Resource
import model
from nocache import nocache
import utils

# bootstrap the app
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
api = Api(app=app,
          title='AI Project API',
          description='ML/DL models prediction API',
          version='1.0')

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

gan_space = api.namespace('gan', description='GAN horse image prediction')
cgan_space = api.namespace('cgan', description='cGAN image prediction')


@nocache
@gan_space.route("/predict")
class GanClass(Resource):

    # return an image from the GAN model prediction
    # @app.route('/predict')
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @nocache
    def get(self):
        gen_img = model.gan_predict()
        print("Predicted image:", gen_img.shape)
        file = utils.gen_img_to_file(gen_img)
        return send_file(
            file,
            as_attachment=True,
            attachment_filename='prediction_horse_image.png',
            mimetype='image/png')

    """
    def post(self):
        return {
            "status": "Posted new data"
        }
    """


@nocache
@cgan_space.route("/predict/<label>", endpoint='predict')
class CGanClass(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Internal Server Error'},
             params={'label': 'Specify the prediction label'})
    @nocache
    def get(self, label):
        print("Label received:", label)
        gen_img = model.cgan_predict(label)
        print("Predicted image:", gen_img.shape, "with label:", label)
        file = utils.gen_img_to_file(gen_img)
        return send_file(
            file,
            as_attachment=True,
            attachment_filename='prediction_image.png',
            mimetype='image/png')


# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
