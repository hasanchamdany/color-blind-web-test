from flask import Flask, jsonify, render_template, request, json
from clips import Environment
import os


dataPath = os.path.abspath(os.path.join(os.getcwd(), 'data'))
diseasePath = os.path.join(dataPath, 'dataGenerate.clp')
env = Environment()
env.load(diseasePath)

def addnumber(number, answer):
    print(number, answer)
    text = f'(assert (number_{number} {answer}))'
    print(text)
    env.eval(text)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    data = request.get_data(as_text=True)
    result = []
    try:
        data = json.loads(data)
        print(data)
        answers = data['answers']
        for i in range(0, len(answers)):
            addnumber(i+1, answers[i])
        env.run()
        for fact in env.facts():
            fact = str(fact)
            print(fact)
            if "people_is" in fact:
                x = fact[1:-1].split(" ")[1]
                result.append(x)
        return jsonify({
            'result' : result
        })
    except:
        return jsonify({
            'status': 'error'
        })
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
