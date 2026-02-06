"""Seed the Dio Bingo database with albums, songs, words, and mappings."""

import sqlite3
import os

DB_PATH = "data/bingo.db"
SCHEMA_PATH = "schema.sql"


def init_db():
    # Remove existing DB to start fresh
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create tables
    with open(SCHEMA_PATH) as f:
        cur.executescript(f.read())

    # === ALBUMS ===
    albums = [
        # Rainbow
        ("Ritchie Blackmore's Rainbow", 1975, "Rainbow"),
        ("Rising", 1976, "Rainbow"),
        ("Long Live Rock 'n' Roll", 1978, "Rainbow"),
        # Black Sabbath
        ("Heaven and Hell", 1980, "Black Sabbath"),
        ("Mob Rules", 1981, "Black Sabbath"),
        ("Dehumanizer", 1992, "Black Sabbath"),
        # Dio
        ("Holy Diver", 1983, "Dio"),
        ("The Last in Line", 1984, "Dio"),
        ("Sacred Heart", 1985, "Dio"),
        ("Dream Evil", 1987, "Dio"),
        ("Lock Up the Wolves", 1990, "Dio"),
        ("Strange Highways", 1993, "Dio"),
        ("Angry Machines", 1996, "Dio"),
        ("Magica", 2000, "Dio"),
        ("Killing the Dragon", 2002, "Dio"),
        ("Master of the Moon", 2004, "Dio"),
    ]
    cur.executemany(
        "INSERT INTO albums (title, year, artist_credit) VALUES (?, ?, ?)", albums
    )

    # === SONGS ===
    # (album_index (1-based), title, track_number)
    songs_data = [
        # 1 - Ritchie Blackmore's Rainbow
        (1, "Man on the Silver Mountain", 1),
        (1, "Self Portrait", 2),
        (1, "Black Sheep of the Family", 3),
        (1, "Catch the Rainbow", 4),
        (1, "Snake Charmer", 5),
        (1, "The Temple of the King", 6),
        (1, "If You Don't Like Rock 'n' Roll", 7),
        (1, "Sixteenth Century Greensleeves", 8),
        (1, "Still I'm Sad", 9),
        # 2 - Rising
        (2, "Tarot Woman", 1),
        (2, "Run with the Wolf", 2),
        (2, "Starstruck", 3),
        (2, "Do You Close Your Eyes", 4),
        (2, "Stargazer", 5),
        (2, "A Light in the Black", 6),
        # 3 - Long Live Rock 'n' Roll
        (3, "Long Live Rock 'n' Roll", 1),
        (3, "Lady of the Lake", 2),
        (3, "L.A. Connection", 3),
        (3, "Gates of Babylon", 4),
        (3, "Kill the King", 5),
        (3, "The Shed (Subtle)", 6),
        (3, "Sensitive to Light", 7),
        (3, "Rainbow Eyes", 8),
        # 4 - Heaven and Hell
        (4, "Neon Knights", 1),
        (4, "Children of the Sea", 2),
        (4, "Lady Evil", 3),
        (4, "Heaven and Hell", 4),
        (4, "Wishing Well", 5),
        (4, "Die Young", 6),
        (4, "Walk Away", 7),
        (4, "Lonely Is the Word", 8),
        # 5 - Mob Rules
        (5, "Turn Up the Night", 1),
        (5, "Voodoo", 2),
        (5, "The Sign of the Southern Cross", 3),
        (5, "E5150", 4),
        (5, "The Mob Rules", 5),
        (5, "Country Girl", 6),
        (5, "Slipping Away", 7),
        (5, "Falling Off the Edge of the World", 8),
        (5, "Over and Over", 9),
        # 6 - Dehumanizer
        (6, "Computer God", 1),
        (6, "After All (The Dead)", 2),
        (6, "TV Crimes", 3),
        (6, "Letters from Earth", 4),
        (6, "Master of Insanity", 5),
        (6, "Time Machine", 6),
        (6, "Sins of the Father", 7),
        (6, "Too Late", 8),
        (6, "I", 9),
        (6, "Buried Alive", 10),
        # 7 - Holy Diver
        (7, "Stand Up and Shout", 1),
        (7, "Holy Diver", 2),
        (7, "Gypsy", 3),
        (7, "Caught in the Middle", 4),
        (7, "Don't Talk to Strangers", 5),
        (7, "Straight Through the Heart", 6),
        (7, "Invisible", 7),
        (7, "Rainbow in the Dark", 8),
        (7, "Shame on the Night", 9),
        # 8 - The Last in Line
        (8, "We Rock", 1),
        (8, "The Last in Line", 2),
        (8, "Breathless", 3),
        (8, "I Speed at Night", 4),
        (8, "One Night in the City", 5),
        (8, "Evil Eyes", 6),
        (8, "Mystery", 7),
        (8, "Eat Your Heart Out", 8),
        (8, "Egypt (The Chains Are On)", 9),
        # 9 - Sacred Heart
        (9, "King of Rock and Roll", 1),
        (9, "Sacred Heart", 2),
        (9, "Another Lie", 3),
        (9, "Rock 'n' Roll Children", 4),
        (9, "Hungry for Heaven", 5),
        (9, "Like the Beat of a Heart", 6),
        (9, "Just Another Day", 7),
        (9, "Fallen Angels", 8),
        (9, "Shoot Shoot", 9),
        # 10 - Dream Evil
        (10, "Night People", 1),
        (10, "Dream Evil", 2),
        (10, "Sunset Superman", 3),
        (10, "All the Fools Sailed Away", 4),
        (10, "Naked in the Rain", 5),
        (10, "Overlove", 6),
        (10, "I Could Have Been a Dreamer", 7),
        (10, "Faces in the Window", 8),
        (10, "When a Woman Cries", 9),
        # 11 - Lock Up the Wolves
        (11, "Wild One", 1),
        (11, "Born on the Sun", 2),
        (11, "Hey Angel", 3),
        (11, "Between Two Hearts", 4),
        (11, "Night Music", 5),
        (11, "Lock Up the Wolves", 6),
        (11, "Evil on Queen Street", 7),
        (11, "Walk on Water", 8),
        (11, "Twisted", 9),
        (11, "My Eyes", 10),
        # 12 - Strange Highways
        (12, "Jesus Mary & the Holy Ghost", 1),
        (12, "Firehead", 2),
        (12, "Strange Highways", 3),
        (12, "Hollywood Black", 4),
        (12, "Evilution", 5),
        (12, "One Foot in the Grave", 6),
        (12, "Give Her the Gun", 7),
        (12, "Blood from a Stone", 8),
        (12, "Here's to You", 9),
        (12, "Pain", 10),
        # 13 - Angry Machines
        (13, "Institutional Man", 1),
        (13, "Don't Tell the Kids", 2),
        (13, "Black", 3),
        (13, "Hunter of the Heart", 4),
        (13, "Stay Out of My Mind", 5),
        (13, "Big Sister", 6),
        (13, "Double Monday", 7),
        (13, "Golden Rules", 8),
        (13, "Dying in America", 9),
        (13, "This Is Your Life", 10),
        # 14 - Magica
        (14, "Fever Dreams", 1),
        (14, "Turn to Stone", 2),
        (14, "Feed My Head", 3),
        (14, "Eriel", 4),
        (14, "Challis", 5),
        (14, "As Long as It's Not About Love", 6),
        (14, "Losing My Insanity", 7),
        (14, "Otherworld", 8),
        (14, "Lord of the Last Day", 9),
        (14, "Magica Theme", 10),
        # 15 - Killing the Dragon
        (15, "Killing the Dragon", 1),
        (15, "Along Comes a Spider", 2),
        (15, "Scream", 3),
        (15, "Better in the Dark", 4),
        (15, "Rock & Roll", 5),
        (15, "Push", 6),
        (15, "Guilty", 7),
        (15, "Throw Away Children", 8),
        (15, "Before the Fall", 9),
        (15, "Cold Feet", 10),
        # 16 - Master of the Moon
        (16, "One More for the Road", 1),
        (16, "Master of the Moon", 2),
        (16, "The End of the World", 3),
        (16, "Shivers", 4),
        (16, "The Man Who Would Be King", 5),
        (16, "The Eyes", 6),
        (16, "Living the Lie", 7),
        (16, "I Am", 8),
        (16, "Death by Love", 9),
        (16, "Down in the World", 10),
    ]

    cur.executemany(
        "INSERT INTO songs (album_id, title, track_number) VALUES (?, ?, ?)",
        songs_data,
    )

    # === WORDS ===
    # Fantasy/dramatic vocabulary characteristic of Dio lyrics
    word_list = [
        "rainbow", "dragon", "wizard", "crystal", "thunder",
        "fire", "silver", "mountain", "shadow", "demon",
        "angel", "heaven", "hell", "evil", "holy",
        "sacred", "knight", "king", "queen", "crown",
        "sword", "magic", "dark", "light", "star",
        "moon", "sun", "storm", "flame", "spirit",
        "dream", "soul", "blood", "stone", "chains",
        "night", "eyes", "heart", "stranger", "wolf",
        "gypsy", "diver", "warrior", "temple", "babylon",
        "cross", "voodoo", "neon", "fallen", "mystery",
        "hunger", "shame", "invisible", "shout", "breathless",
        "twilight", "ocean", "sea", "world", "grave",
        "pain", "fever", "scream", "spider", "guilty",
        "wicked", "lightning", "castle", "dungeon", "serpent",
        "sacrifice", "prophecy", "sorcery", "enchanted", "midnight",
        "destiny", "eternity", "inferno", "phantom", "raven",
        "chalice", "spell", "witch", "beast", "doom",
        "glory", "iron", "steel", "power", "skull",
        "crypt", "abyss", "omen", "ritual", "vision",
        "rebel", "exile", "fury", "vengeance", "valor",
        "tower", "tiger", "death", "guilt",
    ]

    cur.executemany("INSERT INTO words (word) VALUES (?)", [(w,) for w in word_list])

    # Build word->id lookup
    word_ids = {}
    for row in cur.execute("SELECT id, word FROM words"):
        word_ids[row[1]] = row[0]

    # Build song title->id lookup
    song_ids = {}
    for row in cur.execute("SELECT id, title FROM songs"):
        song_ids[row[1]] = row[0]

    # === SONG-WORD MAPPINGS ===
    # Map words to the songs whose lyrics contain or strongly reference them
    song_word_map = {
        "Man on the Silver Mountain": [
            "silver", "mountain", "rainbow", "light", "magic", "star", "spirit",
        ],
        "Self Portrait": ["eyes", "soul", "heart", "shadow", "dark"],
        "Black Sheep of the Family": ["dark", "night", "heart", "rebel"],
        "Catch the Rainbow": [
            "rainbow", "sun", "moon", "star", "dream", "soul", "heaven",
        ],
        "Snake Charmer": ["serpent", "spell", "fire", "dark", "night", "enchanted"],
        "The Temple of the King": [
            "temple", "king", "fire", "night", "light", "dark", "soul", "spirit",
        ],
        "If You Don't Like Rock 'n' Roll": ["fire", "soul", "night"],
        "Sixteenth Century Greensleeves": [
            "queen", "castle", "sword", "knight", "crown", "blood",
        ],
        "Still I'm Sad": ["heart", "soul", "dark", "night", "pain"],
        "Tarot Woman": [
            "crystal", "magic", "star", "vision", "spell", "mystery", "wizard",
        ],
        "Run with the Wolf": [
            "wolf", "night", "fire", "moon", "dark", "blood", "beast",
        ],
        "Starstruck": ["star", "fire", "light", "eyes", "heart"],
        "Do You Close Your Eyes": ["eyes", "night", "dream", "dark"],
        "Stargazer": [
            "star", "wizard", "tower", "fire", "rainbow", "chains", "stone",
            "soul", "sun", "magic", "prophecy", "sacrifice",
        ],
        "A Light in the Black": [
            "light", "dark", "night", "fire", "star", "soul", "silver",
            "shadow", "eternity",
        ],
        "Long Live Rock 'n' Roll": ["night", "fire", "thunder", "power"],
        "Lady of the Lake": [
            "moon", "night", "enchanted", "spell", "magic", "silver", "spirit",
        ],
        "L.A. Connection": ["night", "fire", "eyes"],
        "Gates of Babylon": [
            "babylon", "dragon", "fire", "night", "dark", "doom", "evil",
            "prophecy", "hell", "vision",
        ],
        "Kill the King": [
            "king", "crown", "sword", "power", "thunder", "fury", "blood",
        ],
        "The Shed (Subtle)": ["dark", "shadow", "night", "eyes"],
        "Sensitive to Light": ["light", "night", "shadow", "dark", "eyes"],
        "Rainbow Eyes": [
            "rainbow", "eyes", "moon", "night", "star", "dream", "silver",
        ],
        "Neon Knights": [
            "neon", "knight", "dark", "light", "night", "fire", "thunder",
            "power", "glory",
        ],
        "Children of the Sea": [
            "sea", "ocean", "sun", "moon", "dark", "night", "world",
            "storm", "doom",
        ],
        "Lady Evil": [
            "evil", "shadow", "night", "dark", "crystal", "witch", "spell",
            "vision",
        ],
        "Heaven and Hell": [
            "heaven", "hell", "evil", "soul", "dark", "light", "fire",
            "world", "spirit", "doom", "eternity",
        ],
        "Wishing Well": ["dream", "eyes", "heart", "soul", "star"],
        "Die Young": [
            "dark", "night", "shadow", "evil", "world", "heart", "soul",
            "thunder",
        ],
        "Walk Away": ["night", "heart", "fire", "soul"],
        "Lonely Is the Word": ["dark", "night", "world", "soul", "pain", "doom"],
        "Turn Up the Night": ["night", "fire", "dark", "lightning"],
        "Voodoo": [
            "voodoo", "spell", "dark", "night", "fire", "ritual", "magic",
        ],
        "The Sign of the Southern Cross": [
            "cross", "fire", "dark", "night", "world", "storm", "star",
            "omen", "vision",
        ],
        "E5150": ["dark", "shadow", "doom"],
        "The Mob Rules": [
            "fire", "night", "dark", "hell", "thunder", "power",
        ],
        "Country Girl": ["sun", "heart", "dream"],
        "Slipping Away": ["night", "shadow", "dark", "soul", "heart"],
        "Falling Off the Edge of the World": [
            "world", "dark", "fire", "night", "abyss", "doom", "eternity",
        ],
        "Over and Over": ["fire", "night", "dark", "soul", "world"],
        "Computer God": [
            "iron", "steel", "dark", "night", "shadow", "evil", "power",
            "skull", "vision",
        ],
        "After All (The Dead)": [
            "dark", "night", "grave", "soul", "blood", "shadow", "doom",
        ],
        "TV Crimes": ["evil", "fire", "night", "dark", "wicked"],
        "Letters from Earth": [
            "fire", "world", "dark", "night", "blood", "hell", "pain",
        ],
        "Master of Insanity": [
            "dark", "night", "soul", "evil", "shadow", "pain", "doom",
        ],
        "Time Machine": [
            "dark", "night", "world", "fire", "steel", "power", "eternity",
        ],
        "Sins of the Father": [
            "blood", "soul", "dark", "night", "hell", "fire", "pain", "guilt",
        ],
        "Too Late": ["dark", "night", "soul", "heart", "pain"],
        "I": ["soul", "fire", "dark", "power", "iron"],
        "Buried Alive": ["grave", "dark", "night", "blood", "soul", "crypt"],
        "Stand Up and Shout": [
            "shout", "fire", "night", "dark", "power", "thunder", "rebel",
        ],
        "Holy Diver": [
            "holy", "diver", "dark", "night", "star", "midnight", "tiger",
            "fire", "thunder", "shadow", "dragon", "rainbow",
        ],
        "Gypsy": ["gypsy", "night", "fire", "dark", "magic", "spell", "soul"],
        "Caught in the Middle": ["fire", "night", "dark", "heart"],
        "Don't Talk to Strangers": [
            "stranger", "night", "dark", "evil", "shadow", "dream", "fire",
            "eyes", "wicked",
        ],
        "Straight Through the Heart": [
            "heart", "fire", "night", "dark", "blood", "sword",
        ],
        "Invisible": [
            "invisible", "dark", "night", "shadow", "eyes", "phantom",
        ],
        "Rainbow in the Dark": [
            "rainbow", "dark", "night", "fire", "star", "shadow", "light",
            "soul", "heart",
        ],
        "Shame on the Night": [
            "shame", "night", "dark", "fire", "eyes", "heart", "shadow",
        ],
        "We Rock": ["fire", "night", "thunder", "power", "lightning"],
        "The Last in Line": [
            "fire", "night", "dark", "holy", "thunder", "power", "world",
            "soul", "destiny",
        ],
        "Breathless": [
            "breathless", "fire", "night", "heart", "dark",
        ],
        "I Speed at Night": ["night", "fire", "dark", "lightning"],
        "One Night in the City": ["night", "fire", "dark", "eyes", "shadow"],
        "Evil Eyes": [
            "evil", "eyes", "dark", "night", "fire", "shadow", "wicked",
        ],
        "Mystery": [
            "mystery", "dark", "night", "fire", "shadow", "magic", "enchanted",
        ],
        "Eat Your Heart Out": ["heart", "fire", "night", "blood"],
        "Egypt (The Chains Are On)": [
            "chains", "fire", "sun", "dark", "night", "stone", "king",
            "sacrifice", "prophecy", "temple", "doom",
        ],
        "King of Rock and Roll": [
            "king", "crown", "fire", "night", "power", "glory",
        ],
        "Sacred Heart": [
            "sacred", "heart", "fire", "night", "dark", "soul", "heaven",
            "holy", "spirit",
        ],
        "Another Lie": ["dark", "night", "eyes", "heart", "soul"],
        "Rock 'n' Roll Children": [
            "dark", "night", "fire", "dream", "magic", "soul",
        ],
        "Hungry for Heaven": [
            "heaven", "hunger", "fire", "night", "dark", "soul", "world",
            "dream",
        ],
        "Like the Beat of a Heart": ["heart", "fire", "night", "thunder"],
        "Just Another Day": ["night", "dark", "sun", "heart"],
        "Fallen Angels": [
            "fallen", "angel", "dark", "night", "fire", "heaven", "hell",
            "soul", "doom",
        ],
        "Shoot Shoot": ["fire", "night", "power"],
        "Night People": [
            "night", "dark", "shadow", "fire", "moon", "midnight", "phantom",
        ],
        "Dream Evil": [
            "dream", "evil", "dark", "night", "fire", "shadow", "midnight",
            "scream", "wicked",
        ],
        "Sunset Superman": [
            "sun", "fire", "night", "dark", "power", "glory", "destiny",
        ],
        "All the Fools Sailed Away": [
            "night", "dark", "world", "sea", "ocean", "dream", "moon",
            "star", "storm",
        ],
        "Naked in the Rain": [
            "fire", "night", "dark", "storm", "thunder", "lightning",
        ],
        "Overlove": ["fire", "heart", "night", "dark"],
        "I Could Have Been a Dreamer": [
            "dream", "night", "dark", "star", "fire",
        ],
        "Faces in the Window": [
            "eyes", "night", "dark", "shadow", "phantom",
        ],
        "When a Woman Cries": ["heart", "night", "dark", "soul", "pain"],
        "Wild One": [
            "fire", "night", "dark", "wolf", "blood", "rebel", "fury",
        ],
        "Born on the Sun": [
            "sun", "fire", "night", "star", "flame", "inferno",
        ],
        "Hey Angel": [
            "angel", "heaven", "night", "dark", "soul", "fire", "spirit",
        ],
        "Between Two Hearts": ["heart", "fire", "soul", "night", "dark"],
        "Night Music": [
            "night", "dark", "moon", "shadow", "midnight", "enchanted",
        ],
        "Lock Up the Wolves": [
            "wolf", "night", "dark", "moon", "fire", "blood", "beast",
            "fury",
        ],
        "Evil on Queen Street": [
            "evil", "queen", "night", "dark", "shadow", "wicked",
        ],
        "Walk on Water": [
            "fire", "night", "dark", "power", "spirit", "soul",
        ],
        "Twisted": ["dark", "night", "fire", "evil", "shadow", "pain"],
        "My Eyes": ["eyes", "dark", "night", "soul", "shadow", "vision"],
        "Jesus Mary & the Holy Ghost": [
            "holy", "soul", "fire", "dark", "night", "blood", "spirit",
        ],
        "Firehead": [
            "fire", "flame", "night", "dark", "inferno", "blood",
        ],
        "Strange Highways": [
            "dark", "night", "shadow", "fire", "world", "doom",
        ],
        "Hollywood Black": ["dark", "night", "shadow", "fire", "blood"],
        "Evilution": [
            "evil", "dark", "night", "fire", "shadow", "wicked", "doom",
        ],
        "One Foot in the Grave": [
            "grave", "dark", "night", "blood", "soul", "doom", "death",
        ],
        "Give Her the Gun": ["fire", "night", "dark", "blood"],
        "Blood from a Stone": [
            "blood", "stone", "dark", "night", "fire", "soul",
        ],
        "Here's to You": ["fire", "night", "heart", "soul"],
        "Pain": ["pain", "dark", "night", "soul", "fire", "blood"],
        "Institutional Man": [
            "dark", "night", "iron", "steel", "power", "chains",
        ],
        "Don't Tell the Kids": ["dark", "night", "fire", "world", "eyes"],
        "Black": ["dark", "night", "shadow", "fire", "soul", "abyss"],
        "Hunter of the Heart": [
            "heart", "dark", "night", "fire", "blood", "beast",
        ],
        "Stay Out of My Mind": ["dark", "night", "shadow", "eyes", "soul"],
        "Big Sister": ["dark", "night", "eyes", "evil", "shadow"],
        "Double Monday": ["dark", "night", "fire", "world"],
        "Golden Rules": [
            "dark", "night", "fire", "power", "glory", "crown",
        ],
        "Dying in America": ["dark", "night", "fire", "blood", "world", "doom"],
        "This Is Your Life": ["fire", "night", "soul", "heart", "world"],
        "Fever Dreams": [
            "fever", "dream", "dark", "night", "fire", "shadow", "vision",
            "phantom",
        ],
        "Turn to Stone": [
            "stone", "dark", "night", "fire", "shadow", "spell", "sorcery",
        ],
        "Feed My Head": ["fire", "night", "dark", "eyes", "soul"],
        "Eriel": [
            "star", "night", "dark", "magic", "enchanted", "spell", "spirit",
        ],
        "Challis": [
            "chalice", "dark", "night", "fire", "magic", "ritual", "sorcery",
        ],
        "As Long as It's Not About Love": [
            "heart", "night", "dark", "fire", "soul",
        ],
        "Losing My Insanity": [
            "dark", "night", "fire", "shadow", "soul", "pain",
        ],
        "Otherworld": [
            "world", "dark", "night", "star", "magic", "sorcery", "eternity",
        ],
        "Lord of the Last Day": [
            "dark", "night", "fire", "doom", "power", "destiny", "omen",
        ],
        "Magica Theme": [
            "magic", "dark", "night", "sorcery", "enchanted", "spell",
        ],
        "Killing the Dragon": [
            "dragon", "fire", "night", "dark", "sword", "blood", "beast",
            "power", "fury", "valor",
        ],
        "Along Comes a Spider": [
            "spider", "dark", "night", "shadow", "fire", "wicked",
        ],
        "Scream": [
            "scream", "fire", "night", "dark", "blood", "pain", "fury",
        ],
        "Better in the Dark": [
            "dark", "night", "shadow", "fire", "soul", "midnight",
        ],
        "Rock & Roll": ["fire", "night", "thunder", "power"],
        "Push": ["fire", "night", "dark", "power", "fury"],
        "Guilty": [
            "guilty", "dark", "night", "fire", "blood", "soul",
        ],
        "Throw Away Children": [
            "dark", "night", "fire", "world", "blood", "pain",
        ],
        "Before the Fall": [
            "fallen", "dark", "night", "fire", "doom", "soul", "destiny",
        ],
        "Cold Feet": ["night", "dark", "fire", "shadow", "heart"],
        "One More for the Road": ["night", "dark", "fire", "soul", "heart"],
        "Master of the Moon": [
            "moon", "dark", "night", "shadow", "magic", "star", "midnight",
            "sorcery",
        ],
        "The End of the World": [
            "world", "dark", "night", "fire", "doom", "abyss", "eternity",
        ],
        "Shivers": ["dark", "night", "shadow", "fire", "phantom", "crypt"],
        "The Man Who Would Be King": [
            "king", "crown", "dark", "night", "power", "glory", "destiny",
        ],
        "The Eyes": [
            "eyes", "dark", "night", "shadow", "vision", "fire",
        ],
        "Living the Lie": ["dark", "night", "fire", "soul", "heart"],
        "I Am": [
            "fire", "night", "dark", "power", "soul", "destiny", "glory",
        ],
        "Death by Love": [
            "dark", "night", "heart", "blood", "fire", "doom",
        ],
        "Down in the World": [
            "world", "dark", "night", "fire", "pain", "doom",
        ],
    }

    # Insert song-word mappings
    mappings = []
    missing_songs = []
    missing_words = []

    for song_title, words in song_word_map.items():
        if song_title not in song_ids:
            missing_songs.append(song_title)
            continue
        sid = song_ids[song_title]
        for word in words:
            if word not in word_ids:
                missing_words.append(word)
                continue
            mappings.append((sid, word_ids[word]))

    if missing_songs:
        print(f"Warning: Songs not found in DB: {missing_songs}")
    if missing_words:
        unique_missing = sorted(set(missing_words))
        print(f"Warning: Words not found in DB: {unique_missing}")

    cur.executemany(
        "INSERT OR IGNORE INTO song_words (song_id, word_id) VALUES (?, ?)", mappings
    )

    conn.commit()

    # Print stats
    album_count = cur.execute("SELECT COUNT(*) FROM albums").fetchone()[0]
    song_count = cur.execute("SELECT COUNT(*) FROM songs").fetchone()[0]
    word_count = cur.execute("SELECT COUNT(*) FROM words").fetchone()[0]
    mapping_count = cur.execute("SELECT COUNT(*) FROM song_words").fetchone()[0]

    print(f"Database seeded successfully!")
    print(f"  Albums: {album_count}")
    print(f"  Songs: {song_count}")
    print(f"  Words: {word_count}")
    print(f"  Song-word mappings: {mapping_count}")

    conn.close()


if __name__ == "__main__":
    init_db()
