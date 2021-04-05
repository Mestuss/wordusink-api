from flask import Flask, jsonify
from crawling import get_image_with_bs,get_image_with_selenium
from threading import Thread

app = Flask(__name__)

@app.route("/api/<term>/<start>", methods=['GET'])
def get_images(term, start):
  # from_googles =  get_image_with_selenium(term,int(start))
  from_googles =  get_image_with_bs(term,int(start))
  
  return jsonify(from_googles)

@app.route("/")
def index():
  return "<h1>Do you wanna get Google Image? 🤔<h1>"
  
if __name__ == "__main__":
  app.run(port=3000, host="0.0.0.0")
  # host="172.30.59.85"
