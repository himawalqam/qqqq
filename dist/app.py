from flask import Flask, render_template_string, request

app = Flask(__name__)

# 恋爱模拟的短语
pleading_phrases = [
    "考虑我一下嘛~", "求求你了(。•́︿•̀。)", "给我一个机会好不好？",
    "我真的很喜欢你呀！", "不要这么快拒绝嘛~"
]

@app.route("/", methods=["GET", "POST"])
def love_confession():
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == "yes":
            return render_template_string('''
                <h1>最爱你啦！(๑•̀ㅂ•́)و✧</h1>
                <img src="https://placekitten.com/300/200" style="border-radius: 10px;">
                <p><a href="/">返回</a></p>
            ''')
        else:
            import random
            phrase = random.choice(pleading_phrases)
            return render_template_string('''
                <h1>可以成为我的恋人吗？</h1>
                <img src="https://placekitten.com/250/200" style="border-radius: 10px;">
                <p style="color: blue; font-size: 18px;">{{ phrase }}</p>
                <form method="POST">
                    <button type="submit" name="choice" value="yes" style="background: pink; color: white;">可以</button>
                    <button type="submit" name="choice" value="no" style="background: lightgray;">不要</button>
                </form>
            ''', phrase=phrase)
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>恋爱模拟</title>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 50px; }
                button { padding: 10px 20px; font-size: 16px; margin: 10px; border: none; cursor: pointer; }
            </style>
        </head>
        <body>
            <h1>可以成为我的恋人吗？</h1>
            <img src="https://placekitten.com/300/200" style="border-radius: 10px;">
            <form method="POST">
                <button type="submit" name="choice" value="yes" style="background: pink; color: white;">可以</button>
                <button type="submit" name="choice" value="no" style="background: lightgray;">不要</button>
            </form>
        </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)