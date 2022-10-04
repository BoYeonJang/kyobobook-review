from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from inference import *

# from .inference import inference_fn

# app = Flask(__name__)
# CORS(app)

# def get_web_service_app(inference_fn):
#   model = torch.load('../Data/모델/model.pt')

#   # Flask 객체 인스턴스 생성
#   # app = Flask(__name__)
#   # CORS(app)

#   # 접속 URL 설정
#   @app.route('/')
#   def index():
#     return f'{model}'
#     # return render_template('index.html')

#   @app.route('/api', methods=['POST'])
#   def api():
#     if request.method == 'POST':
#       query = request.json
#       output_data = inference_fn(query["prompt"])
#       response = jsonify(output_data)

#     return response

#   @app.route('/predict', methods=['POST'])
#   def predict():
#     if request.method == 'POST':
#       data = request.get_json()
#       print(data)

#       return jsonify({'resultType': 1, 'data': data})

model = torch.load('../Data/모델/model.pt')

  # Flask 객체 인스턴스 생성
app = Flask(__name__)
CORS(app)

# 접속 URL 설정
@app.route('/')
def index():
  return f'{model}'

@app.route('/api', methods=['POST'])
def api():
  if request.method == 'POST':
    query = request.json
    output_data = inference_fn(
      query["prompt"],
      query["min_length"],
      query["max_length"],
      query["top_p"],
      query["top_k"],
      query["repetition_penalty"],
      query["no_repeat_ngram_size"],
      query["temperature"])
    response = jsonify(output_data)

  return response

# @app.route('/api', methods=['GET'])
# def api():
  # query = request.json
  # output_data = inference_fn("이건테스트입니다.ㄴ아너아ㅣㅇ너리ㅏㅁㄴ;ㅓ")
  # response = jsonify(output_data)

  # return inference_fn("이건테스트입니다.ㄴ아너아ㅣㅇ너리ㅏㅁㄴ;ㅓ")

@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
    data = request.get_json()
    print(data)

    return jsonify({'resultType': 1, 'data': data})

if __name__ == "__main__":
  # 코드 수정 시 자동 반영
  app.run(host='0.0.0.0', debug=True)
