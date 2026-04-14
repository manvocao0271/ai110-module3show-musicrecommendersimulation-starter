# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration 

This recommender is a basic simulation that suggests songs from a small dataset (of about 20) based on a user's preferences for genre, mood, energy level, and a couple of other attributes. It assumes the user already knows what they like and scores each song based on the matches and similarities.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Each song is scored by comparing it against the attributes of the user's profile. A match of genre adds 3 points, a mood match adds 2, and a numeric features like energy and valence add up to 2.5 more points based on how close these numerical values are. Likewise, an acoustic metric is calculated too. Once every song has a score, the system sorts them from the highest to lowest and returns the top 5.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset 

The dataset consists of 20 songs spanning 17 different genres, with a variety of attributes of the headers mentioned. No songs were removed from the starter set, just added with the help of Claude Code. However, it is observerd during testing that the dataset is skewed towards lower-energy songs, leaving a few options of listeners that want higher-energy level songs.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works best when the user's preferences are internally consistent. This is when all of the attributes of a user's profile all point to the same type of song. Additionally, the numerical scoring logic of the valence and energy level is a good backbone of the recommender in case the genre or mood does not match. The system can still find songs that feel similar based on these attributes.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The dataset only conly consists of about 2/20 songs that have an energy level between 0.5-0.7. Thus, this will produce lopsided results even when the scoring logic is fair. A user who wants a moderately energetic song will be recommended by something that has a lower energy level just because of how skewed the dataset is. Additionally, the genre weight is quite heavy compared to every else. Once a genre is matched, the system is most likely to proceed with a higher score for that song.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The user profiles we tested were: High-Energy Sad, Chill Lo-Fi, Deep Intense Rock, Angry Acoustic, and Ghost Genre. For the recommended songs, I mostly looked for the reasons why the results were recommended, which all made sense according to the type of user profile. It is quite subjective per user and the type of songs they like because I was surprised to see a mix of upbeat and sad songs for the High-Energy Sad profile. This goes the same for the other profiles too, perhaps this recommender would fair better with a larger variety dataset of songs.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

The most impactful future work is to add a much larger dataset of songs. Additionally, it would be best to not use genre and mood because there are so many types and subcategories. Instead, a single metric that groups all of these together like "melancholic" or "sad" or "classical" would be most appropriate. This should vastly improve the recommender to handle larger catalog of songs.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this system made it clear to me that the saying "garbage in garbage out" is definitely true when it comes to user IO. The recommender can only be as good as the dataset, despite no machine learning. Straitforward arithmetic calculations is still a strong and simple way for content-based filtering to work. This did not change how I think about music recommendation apps because this is mostly the algorithm and core logic of how recommendations system should work.

---