from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        note = request.form["note"]
        notes.append(note)
        return redirect("/")

    return render_template("add_note.html")

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_note(index):
    if request.method == "POST":
        notes[index] = request.form["note"]
        return redirect("/")

    return render_template(
        "edit_note.html",
        note=notes[index],
        index=index
    )

@app.route("/delete/<int:index>")
def delete_note(index):
    if 0 <= index < len(notes):
        notes.pop(index)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)