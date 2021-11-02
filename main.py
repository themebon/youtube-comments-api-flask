from flask import Flask, jsonify
from ytb_comment_scraper import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/<string:videoId>")
def get_comments_json(videoId):

    try:
        youtube_url = f'https://www.youtube.com/watch?v={videoId}'
        limit = COMMENT_LIMIT
        count = 0
        comments_array = []
        for comment in download_comments(youtube_url):
            # print(comment)
            comments_array.append(comment)

            count += 1
            if limit and count >= limit:
                break

        if comments_array:
            return jsonify(comments_array)
        else:
            return {'error': 'No video id found'}

    except Exception as e:
        print('Error:', str(e))
        sys.exit(1)
