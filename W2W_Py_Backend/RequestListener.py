from flask import Flask, request
from flask_restful import Resource, Api
from threading import Thread
import DetectEmotionsOnVideo as Deov

app = Flask(__name__)
api = Api(app)


class RunVideo(Resource):
    @staticmethod
    def get():
        url = request.args.get('url')
        thread = Thread(target=Deov.DetectEmotionsOnVideo.start_video, args=(url,))
        thread.start()
        return "did start video"


api.add_resource(RunVideo, '/runVideo')

if __name__ == '__main__':
    app.run(port='8080')
