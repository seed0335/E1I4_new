from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.w1iiuru.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'이현경',
    'about_me':'https://chun-k.tistory.com/',
    'photo':'<img src="https://ca.slack-edge.com/T043597JK8V-U0532LT9LLE-58e265f5a665-512" class="img" alt="...">',
    'imoge':'💍',
    'Q1':'html, css, javascript, java, python',
    'Q2':'근육이 잘 붙는 몸을 소유함',
    'Q3':'모든게 쏠려있는 극 ISTP',
    'Q4':'아침 헬스 좋아해요!'
 }
db.profiles.insert_one(doc) 

# 이현경님 본인 데이터 저장해주세요. (위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)