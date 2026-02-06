import sqlite3
import random
from flask import Flask, render_template, request, g, jsonify

app = Flask(__name__)
DATABASE = "data/bingo.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    db = get_db()
    albums = db.execute(
        "SELECT id, title, year, artist_credit FROM albums ORDER BY year"
    ).fetchall()

    eras = {
        "Rainbow": [a for a in albums if a["artist_credit"] == "Rainbow"],
        "Black Sabbath": [a for a in albums if a["artist_credit"] == "Black Sabbath"],
        "Dio": [a for a in albums if a["artist_credit"] == "Dio"],
    }
    return render_template("index.html", eras=eras)


@app.route("/songs/<int:album_id>")
def songs(album_id):
    db = get_db()
    songs = db.execute(
        "SELECT id, title, track_number FROM songs WHERE album_id = ? ORDER BY track_number",
        (album_id,),
    ).fetchall()
    album = db.execute("SELECT title FROM albums WHERE id = ?", (album_id,)).fetchone()
    return render_template("_songs.html", songs=songs, album=album)


@app.route("/word-count", methods=["POST"])
def word_count():
    song_ids = request.form.getlist("song_ids[]", type=int)
    album_ids = request.form.getlist("album_ids[]", type=int)

    if not song_ids and not album_ids:
        return '<span id="word-count">0 words in pool</span>'

    db = get_db()
    placeholders_songs = ",".join("?" for _ in song_ids)
    placeholders_albums = ",".join("?" for _ in album_ids)

    query_parts = []
    params = []

    if song_ids:
        query_parts.append(
            f"SELECT DISTINCT word_id FROM song_words WHERE song_id IN ({placeholders_songs})"
        )
        params.extend(song_ids)

    if album_ids:
        query_parts.append(
            f"SELECT DISTINCT sw.word_id FROM song_words sw JOIN songs s ON sw.song_id = s.id WHERE s.album_id IN ({placeholders_albums})"
        )
        params.extend(album_ids)

    union_query = " UNION ".join(query_parts)
    count = db.execute(f"SELECT COUNT(*) FROM ({union_query})", params).fetchone()[0]

    css_class = "sufficient" if count >= 24 else "insufficient"
    return f'<span id="word-count" class="{css_class}">{count} words in pool</span>'


@app.route("/generate", methods=["POST"])
def generate():
    song_ids = request.form.getlist("song_ids[]", type=int)
    album_ids = request.form.getlist("album_ids[]", type=int)
    num_cards = request.form.get("num_cards", 1, type=int)
    num_cards = max(1, min(8, num_cards))

    if not song_ids and not album_ids:
        return '<div class="warning">Please select at least some songs or albums.</div>'

    db = get_db()

    query_parts = []
    params = []

    if song_ids:
        placeholders = ",".join("?" for _ in song_ids)
        query_parts.append(
            f"SELECT DISTINCT w.id, w.word FROM words w JOIN song_words sw ON w.id = sw.word_id WHERE sw.song_id IN ({placeholders})"
        )
        params.extend(song_ids)

    if album_ids:
        placeholders = ",".join("?" for _ in album_ids)
        query_parts.append(
            f"SELECT DISTINCT w.id, w.word FROM words w JOIN song_words sw ON w.id = sw.word_id JOIN songs s ON sw.song_id = s.id WHERE s.album_id IN ({placeholders})"
        )
        params.extend(album_ids)

    union_query = " UNION ".join(query_parts)
    words = db.execute(union_query, params).fetchall()
    word_list = [w["word"] for w in words]

    if len(word_list) < 24:
        return f'<div class="warning">Only {len(word_list)} words in pool — need at least 24. Select more songs!</div>'

    cards = []
    for i in range(num_cards):
        chosen = random.sample(word_list, 24)
        # Insert FREE space at center (index 12 in a 25-cell grid)
        chosen.insert(12, "FREE")
        grid = [chosen[r * 5 : (r + 1) * 5] for r in range(5)]
        cards.append(grid)

    return render_template("cards.html", cards=cards)


@app.route("/print", methods=["POST"])
def print_view():
    song_ids = request.form.getlist("song_ids[]", type=int)
    album_ids = request.form.getlist("album_ids[]", type=int)
    num_cards = request.form.get("num_cards", 1, type=int)
    num_cards = max(1, min(8, num_cards))

    db = get_db()

    query_parts = []
    params = []

    if song_ids:
        placeholders = ",".join("?" for _ in song_ids)
        query_parts.append(
            f"SELECT DISTINCT w.word FROM words w JOIN song_words sw ON w.id = sw.word_id WHERE sw.song_id IN ({placeholders})"
        )
        params.extend(song_ids)

    if album_ids:
        placeholders = ",".join("?" for _ in album_ids)
        query_parts.append(
            f"SELECT DISTINCT w.word FROM words w JOIN song_words sw ON w.id = sw.word_id JOIN songs s ON sw.song_id = s.id WHERE s.album_id IN ({placeholders})"
        )
        params.extend(album_ids)

    if not query_parts:
        return "No songs selected", 400

    union_query = " UNION ".join(query_parts)
    words = db.execute(union_query, params).fetchall()
    word_list = [w["word"] for w in words]

    if len(word_list) < 24:
        return "Not enough words", 400

    cards = []
    for i in range(num_cards):
        chosen = random.sample(word_list, 24)
        chosen.insert(12, "FREE")
        grid = [chosen[r * 5 : (r + 1) * 5] for r in range(5)]
        cards.append(grid)

    return render_template("print.html", cards=cards)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
