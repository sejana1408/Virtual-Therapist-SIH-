import  psycopg2
connection = psycopg2.connect(host = "localhost",port = "5432",database = "localhost",user = "postgres",password = "root")

cursor = connection.cursor()
print("database is connected successfully")

disease = input()
if disease == "articulation disorder":
    cursor.execute("select therapy_words from therapy where p_id = 1001;")


a = cursor.fetchall()


lst = a
i=0
lst = [str(i) for i in lst]
result = ''.join(lst)
retrived_therapy = (result[2:-3])
print(retrived_therapy)


instruction = retrived_therapy


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
except Exception as e:
     print('Sorry, I could not convert the audio to text')

text = text.lower()
if text == instruction:
    print("your exercise is successfully completed")
else:
    print("retry this exercise")
