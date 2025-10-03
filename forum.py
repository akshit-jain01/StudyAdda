from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (resets when server restarts)
rooms = []
comments = {}

# Templates (inline for single-file simplicity)
room_list_html = """
<h1>Forum Rooms</h1>
<a href="{{ url_for('create_room') }}">➕ Create Room</a>
<ul>
  {% for i, room in enumerate(rooms) %}
    <li><a href="{{ url_for('room_detail', room_id=i) }}">{{ room }}</a></li>
  {% else %}
    <li>No rooms yet.</li>
  {% endfor %}
</ul>
"""

create_room_html = """
<h2>Create a New Room</h2>
<form method="post">
  <input type="text" name="name" placeholder="Room name" required><br>
  <button type="submit">Create</button>
</form>
<a href="{{ url_for('room_list') }}">⬅ Back to rooms</a>
"""

room_detail_html = """
<h2>{{ room }}</h2>
<h3>Comments:</h3>
<ul>
  {% for comment in comments %}
    <li>{{ comment }}</li>
  {% else %}
    <li>No comments yet.</li>
  {% endfor %}
</ul>
<form method="post">
  <textarea name="body" required></textarea><br>
  <button type="submit">Add Comment</button>
</form>
<a href="{{ url_for('room_list') }}">⬅ Back to rooms</a>
"""

@app.route("/")
def room_list():
    return render_template_string(room_list_html, rooms=rooms)

@app.route("/create/", methods=["GET", "POST"])
def create_room():
    if request.method == "POST":
        name = request.form["name"]
        rooms.append(name)
        comments[len(rooms) - 1] = []
        return redirect(url_for("room_list"))
    return render_template_string(create_room_html)

@app.route("/room/<int:room_id>/", methods=["GET", "POST"])
def room_detail(room_id):
    if room_id >= len(rooms):
        return "Room not found", 404
    if request.method == "POST":
        comments[room_id].append(request.form["body"])
        return redirect(url_for("room_detail", room_id=room_id))
    return render_template_string(room_detail_html, room=rooms[room_id], comments=comments[room_id])

if __name__ == "__main__":
    app.run(debug=True)
