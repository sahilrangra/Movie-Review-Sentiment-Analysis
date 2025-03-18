import pandas as pd
import random

# Expanded dataset with 100 reviews
data = [
    # Positive Reviews (Sentiment: 0.7 - 1.0)
    ("Absolutely fantastic! One of the best movies I've seen.", 1.0),
    ("The performances were breathtaking, and the story was deeply moving.", 0.95),
    ("A cinematic masterpiece! Every frame was stunning.", 0.98),
    ("I was hooked from start to finish. A must-watch!", 0.93),
    ("A beautiful blend of storytelling and stunning visuals.", 0.9),
    ("Brilliantly written and acted, highly recommend it.", 0.88),
    ("The soundtrack alone makes this film unforgettable.", 0.86),
    ("A masterpiece in every sense, flawless execution.", 0.92),
    ("So much fun! Great action and humor throughout.", 0.89),
    ("An emotional rollercoaster, left me speechless.", 0.94),
    ("One of the most thought-provoking films of the decade.", 0.91),
    ("Incredible performances and a script full of depth.", 0.87),
    ("The best movie in its genre, hands down.", 0.85),
    ("Everything about this film was perfect!", 0.97),
    ("A must-watch for anyone who loves cinema.", 0.96),
    ("The cinematography alone makes it worth watching.", 0.84),
    ("This movie stayed with me long after the credits rolled.", 0.93),
    ("Engaging from start to finish, never a dull moment.", 0.88),
    ("An unforgettable experience, easily one of my favorites.", 0.9),
    ("Such an inspiring and uplifting story.", 0.89),

    # Neutral Reviews (Sentiment: 0.4 - 0.7)
    ("Decent movie, but nothing groundbreaking.", 0.6),
    ("Enjoyable, but I probably wouldn’t watch it again.", 0.55),
    ("Had some great moments, but overall just okay.", 0.5),
    ("Good acting, but the story lacked depth.", 0.58),
    ("Not bad, but I've seen better movies of this kind.", 0.52),
    ("A mix of good and bad, just an average watch.", 0.45),
    ("Some scenes were great, but overall a bit slow.", 0.49),
    ("The ending was nice, but the middle dragged a lot.", 0.47),
    ("Pretty standard movie, nothing too special.", 0.55),
    ("It was entertaining enough, but forgettable.", 0.57),
    ("A bit too long for my liking, but otherwise okay.", 0.51),
    ("I liked it, but it didn’t blow me away.", 0.6),
    ("Had potential, but missed the mark.", 0.53),
    ("Some great performances, but the plot was weak.", 0.56),
    ("A decent weekend watch, but nothing more.", 0.5),
    ("Not great, not terrible. Just fine.", 0.5),
    ("The visuals were amazing, but the story lacked impact.", 0.59),
    ("It had some good moments, but overall it felt rushed.", 0.48),
    ("An okay movie, but I wouldn’t go out of my way to watch it.", 0.52),
    ("Not as good as I expected, but not bad either.", 0.54),

    # Negative Reviews (Sentiment: 0.0 - 0.4)
    ("A complete waste of time, boring and predictable.", 0.2),
    ("Terrible acting and a weak storyline.", 0.1),
    ("One of the worst movies I've ever seen.", 0.05),
    ("The plot made absolutely no sense.", 0.15),
    ("Couldn’t even finish it, that bad.", 0.1),
    ("The dialogue was laughably bad.", 0.3),
    ("Nothing interesting happened throughout the film.", 0.25),
    ("The pacing was horrible, I almost fell asleep.", 0.22),
    ("I regret wasting my money on this.", 0.1),
    ("Terrible CGI, completely ruined the experience.", 0.12),
    ("Overhyped and disappointing.", 0.3),
    ("No character development at all.", 0.18),
    ("Cliché and uninspired from start to finish.", 0.2),
    ("The jokes didn’t land, and the action was dull.", 0.35),
    ("Too long and full of unnecessary scenes.", 0.3),
    ("The script felt like it was written in a day.", 0.22),
    ("Predictable, unoriginal, and just plain bad.", 0.1),
    ("A mess from start to finish.", 0.15),
    ("Tried too hard to be deep, but failed miserably.", 0.3),
    ("Bad direction, bad acting, bad everything.", 0.05)
]

# Convert to DataFrame and save
df = pd.DataFrame(data, columns=["review", "sentiment"])
df.to_csv("movie_reviews_100.csv", index=False)

print("✅ Dataset saved as movie_reviews_100.csv")