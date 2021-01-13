from forms import TodoForm
from models import todos
from flask import request, render_template, redirect, url_for
from app import app


@app.route('/todos/', methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            data = (
                None, form.data["nazwa"],
                form.data["deadline"], form.data["priorytet"]
            )
            todos.create(data)
        return redirect(url_for("todos_list"))

    return render_template(
        "todos.html", form=form, todos=todos.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id, nazwa=form.data["nazwa"],
                         deadline=form.data["deadline"],
                         priorytet=form.data["priorytet"],
                         )
            return redirect(url_for("todos_list"))

    return render_template("todo.html", form=form, todo_id=todo_id)


@app.route("/todos/<int:todo_id>/delete", methods=["GET"])
def todo_delete(todo_id):
    form = TodoForm()
    error = ''
    if request.method == "GET":
        todos.delete(todo_id)
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form,
                           todos=todos.all(), error=error)

