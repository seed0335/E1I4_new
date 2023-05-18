from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'김장원',
    'about_me':'목표하는 꿈을 위해 달려가고 있는 청년입니다.',
    'photo':'없음',
    'imoge':'💻',
    'Q1':'자바스크립트, 자바',
    'Q2':'새로운 것을 빨리 배웁니다.',
    'Q3':'MBTI',
    'Q4':'삼일동안 집을 나간적이 없다. ㅠㅠ',
}
db.profiles.insert_one(doc) 

# 김장원님 본인 데이터 저장해주세요. (위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)