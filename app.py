from flask import Flask, json, render_template

app = Flask(__name__)

with open('candidates.json', encoding='utf-8') as json_file:
    candidates = json.load(json_file)


@app.route("/")
def page_index():
    title = 'Candidates'
    return render_template('index.html', title=title, arr=candidates)


@app.route("/candidates/<int:can>")
def page_candidates(can: int):
    candidate = next((item for item in candidates if item['id'] == can), None)
    return render_template('candidates.html', candidate=candidate, img=candidate['picture'])


@app.route("/skills/<skill>")
def page_skills(skill):
    title = 'Exact skills'
    result_arr = [x for x in candidates if skill.lower() in x['skills']]
    return render_template('skills.html', title=title, arr=result_arr)


if __name__ == "__main__":
    app.run(debug=True)
