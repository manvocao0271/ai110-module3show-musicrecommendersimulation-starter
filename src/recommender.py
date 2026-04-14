import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a single song and its audio attributes loaded from the CSV."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Stores a listener's taste preferences used to score and rank songs."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: float

class Recommender:
    """OOP wrapper around the recommendation logic that holds a song catalogue."""
    def __init__(self, songs: List[Song]):
        """Initialises the recommender with a list of Song objects."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k Song objects best matching the given UserProfile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable string explaining why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file and returns each row as a dict with numeric fields cast to int or float."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences and returns a (total_score, reasons) tuple."""
    score = 0.0
    reasons = []

    # Categorical: genre — strongest identity signal (+3.0)
    if user_prefs.get("genre") and song["genre"] == user_prefs["genre"]:
        score += 3.0
        reasons.append("genre match (+3.0)")

    # Categorical: mood — contextual fit (+2.0)
    if user_prefs.get("mood") and song["mood"] == user_prefs["mood"]:
        score += 2.0
        reasons.append("mood match (+2.0)")

    # Numeric: energy proximity — weighted ×1.5, max +1.5
    target_energy = user_prefs.get("target_energy", user_prefs.get("energy"))
    if target_energy is not None:
        energy_points = (1.0 - abs(song["energy"] - target_energy)) * 1.5
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    # Numeric: valence proximity — weighted ×1.0, max +1.0
    target_valence = user_prefs.get("target_valence", user_prefs.get("valence"))
    if target_valence is not None:
        valence_points = (1.0 - abs(song["valence"] - target_valence)) * 1.0
        score += valence_points
        reasons.append(f"valence similarity (+{valence_points:.2f})")

    # Boolean: acoustic preference (+1.0 if song is clearly acoustic)
    if user_prefs.get("likes_acoustic") and song["acousticness"] > 0.6:
        score += 1.0
        reasons.append("acoustic feel (+1.0)")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs, sorts them highest to lowest, and returns the top k as (song, score, explanation) tuples."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong matches"
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
