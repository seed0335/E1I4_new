from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import certifi
ca = certifi.where()
#제발
bb = aa
cc = ddd

# mongoDB는 김장원 - 본인 mongoDB로 변경하기
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.txlb0px.mongodb.net/?retryWrites=true&w=majority',tlsCAFile =ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/myprofile/new", methods=["GET"])
def post_profile():

    return render_template('sub.html')

@app.route('/sub')
def sub():
    return render_template('sub.html')

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


# 방명록 저장하는 곳
@app.route('/guestbook', methods=['POST'])
def guestbook_post():
   name_receive = request.form['name_give']
   comment_receive = request.form['comment_give']
   doc = {
       'name'  :name_receive,
       'comment' : comment_receive
   }
   db.guestbook_comments.insert_one(doc)
   return jsonify({'msg': '방명록이 등록되었습니다!'})

# 방명록 mongDB에서 index.html로 데이터 전송
@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.guestbook_comments.find({},{'_id':False}))
    #db.user.find 에서 users 바꿔야한다 일단 강의대로 fan으로 저장함
    #fan -> guestbool_comments 로 변경
    return jsonify({'result': all_comments})

# mac 사용자는 포트5001로 변경하세요.
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
