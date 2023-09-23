from flask import Flask, render_template, request
import webbrowser
from chatgpt import ChatGPT

app = Flask(__name__, template_folder='./templates')

# 初始文本框内容
textbox1_text = ""
textbox2_text = ""
chatgpt = ChatGPT()

@app.route('/', methods=['GET', 'POST'])
def index():
    global textbox1_text, textbox2_text
    global chatgpt

    if request.method == 'POST':
        textbox1_text = request.form['textbox1']
        # 设置文本框2的内容为文本框1的内容
        textbox2_text = chatgpt.send_request(textbox1_text)
        # textbox2_text = textbox1_text

    return render_template('index.html', textbox1_text=textbox1_text, textbox2_text=textbox2_text)

if __name__ == '__main__':
    # 自动打开浏览器
    webbrowser.open('http://127.0.0.1:8000/')
    app.run(debug=True, port=8000)
