"""
Adversarial / edge-case evaluation script for the Music Recommender.

Runs 5 stress-test profiles designed to expose unexpected scoring behaviour,
then prints the top-5 results for each.
"""

from recommender import load_songs, recommend_songs

PROFILES = [
    {
        "label": "1. High-Energy Sad",
        "description": (
            "energy=0.9 conflicts with mood='sad'. Only 1 sad song exists "
            "(Empty Hallways, energy=0.45). Does the +2.0 mood bonus beat "
            "high-energy songs that score better on proximity?"
        ),
        "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9},
    },
    {
        "label": "2. Chill Lo-fi (baseline)",
        "description": (
            "Fully aligned profile — genre, mood, and energy all point toward "
            "the same songs. Used as a control to compare against the adversarial cases."
        ),
        "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35, "valence": 0.58},
    },
    {
        "label": "3. Deep Intense Rock",
        "description": (
            "Only 1 rock song exists in the catalog (Storm Runner). "
            "Reveals what fills ranks 2-5 when the niche is exhausted."
        ),
        "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95},
    },
    {
        "label": "4. Angry Acoustic Contradiction",
        "description": (
            "mood='angry' + likes_acoustic=True. The only angry song (Iron Descent, metal) "
            "has acousticness=0.03 — it CANNOT earn the +1.0 acoustic bonus. "
            "Acoustic songs are all peaceful/chill and never match the mood."
        ),
        "prefs": {
            "genre": "folk",
            "mood": "angry",
            "energy": 0.85,
            "likes_acoustic": True,
        },
    },
    {
        "label": "5. Ghost Genre (latin)",
        "description": (
            "genre='latin' matches zero songs. The +3.0 genre bonus never fires, "
            "so ranking falls back entirely on mood, energy, and valence proximity."
        ),
        "prefs": {"genre": "latin", "mood": "happy", "energy": 0.80, "valence": 0.90},
    },
]


def run_eval() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Catalog loaded: {len(songs)} songs\n")

    for profile in PROFILES:
        label = profile["label"]
        description = profile["description"]
        prefs = profile["prefs"]

        print("=" * 60)
        print(f"  {label}")
        print("=" * 60)
        print(f"  Prefs : {prefs}")
        print(f"  Why   : {description}")
        print()

        results = recommend_songs(prefs, songs, k=5)

        for rank, (song, score, explanation) in enumerate(results, start=1):
            print(f"  #{rank}  {song['title']}  —  {song['artist']}")
            print(
                f"       genre={song['genre']:<14} mood={song['mood']:<12} "
                f"energy={float(song['energy']):.2f}"
            )
            print(f"       score={score:.2f}   {explanation}")

        print()

    print("=" * 60)
    print("  Evaluation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_eval()
