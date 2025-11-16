import sqlite3

conn = sqlite3.connect('recommendations.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion TEXT NOT NULL,
    recommendation TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
)
''')

cursor.execute('DELETE FROM recommendations')
cursor.execute('DELETE FROM categories')

categories = [
    ('movie',),
    ('place',),
    ('song',),
    ('food',),
    ('activity',)
]
cursor.executemany('INSERT INTO categories (name) VALUES (?)', categories)

recommendations = {
    'happy': {
        'movies': [
            "The Greatest Showman", "Coco", "La La Land", "Sing", "Paddington 2", 
            "Mamma Mia!", "Zootopia", "Tangled", "Ratatouille", "Up",
            "Finding Nemo", "The Intouchables", "Paddington", "The Secret Life of Pets", 
            "The Lego Movie", "The Princess Bride", "Ferris Bueller's Day Off", 
            "Crazy Rich Asians", "10 Things I Hate About You", "The 40-Year-Old Virgin",
            "Bridesmaids", "The Intern", "Chef", "Little Miss Sunshine", "The Proposal",
            "The Other Woman", "Easy A", "Mean Girls", "Pitch Perfect", "The Heat",
            "The Nice Guys", "Crazy, Stupid, Love", "The Spy Who Dumped Me", "Jumanji: Welcome to the Jungle",
            "The Secret Life of Walter Mitty", "About Time", "The King's Speech", "The Imitation Game",
            "The Theory of Everything", "The Hundred-Foot Journey", "The Intern", "The Greatest Showman",
            "The Secret Life of Pets 2", "The Croods", "Paddington 3", "The Incredibles", "Shrek",
            "The Lego Movie 2", "Moana", "Kung Fu Panda", "Despicable Me", "Cloudy with a Chance of Meatballs",
            "Hotel Transylvania", "Trolls", "The Peanuts Movie", "The Emoji Movie", "Finding Dory"
        ],
        'places': [
            "Disneyland", "Beach resort", "Sunflower field", "Amalfi Coast", "Santorini",
            "Hawaii", "Paris", "Tokyo Disneyland", "Bali", "Venice", "Maldives", 
            "New York City", "Barcelona", "Sydney", "Rio de Janeiro", "Prague",
            "Key West", "Maui", "Costa Rica", "Lake Tahoe", "Grand Teton National Park",
            "Yellowstone National Park", "Zion National Park", "Big Sur", "Napa Valley",
            "The Bahamas", "Cancun", "Dubai", "Santorini", "Florence", "Lisbon", "Amsterdam",
            "The Great Wall of China", "Machu Picchu", "Niagara Falls", "Santorini", "The Eiffel Tower",
            "The Colosseum", "The Louvre", "The Taj Mahal", "The Grand Canyon", "The Great Barrier Reef",
            "Mount Fuji", "The Northern Lights", "The Amazon Rainforest", "The Sahara Desert", "The Galapagos Islands"
        ],
        'songs': [
            "Happy by Pharrell Williams", "Sugar by Maroon 5", "Dynamite by BTS", 
            "Shake It Off by Taylor Swift", "Good Vibrations by The Beach Boys", 
            "Walking on Sunshine by Katrina and the Waves", "Best Day of My Life by American Authors",
            "Can't Stop the Feeling! by Justin Timberlake", "Uptown Funk by Mark Ronson ft. Bruno Mars",
            "Shut Up and Dance by Walk the Moon", "I Gotta Feeling by The Black Eyed Peas",
            "Happy Together by The Turtles", "Walking on Sunshine by Katrina and the Waves",
            "Good Life by OneRepublic", "On Top of the World by Imagine Dragons",
            "Best Day of My Life by American Authors", "Good Time by Owl City and Carly Rae Jepsen",
            "Firework by Katy Perry", "Roar by Katy Perry", "Shake It Off by Taylor Swift",
            "Good Time by Owl City", "Best Day of My Life by American Authors", "Shut Up and Dance by Walk the Moon",
            "Good Vibrations by The Beach Boys", "Walking on Sunshine by Katrina and the Waves",
            "Happy by Pharrell Williams", "Can't Stop the Feeling! by Justin Timberlake",
            "Best Day of My Life by American Authors", "Good Time by Owl City",
            "Shake It Off by Taylor Swift", "Uptown Funk by Mark Ronson ft. Bruno Mars"
        ],
        'foods': [
            "Fruit salad", "Cheesecake", "Smoothie bowl", "Eclairs", "Chocolate fondue",
            "Pancakes", "Ice cream sundae", "Chocolate cake", "Cupcakes", "Macarons",
            "Tacos", "Sushi", "Pasta Primavera", "Grilled cheese sandwich", "Fruit tart",
            "Chocolate-dipped strawberries", "Mango sticky rice", "Pavlova", "Banana split",
            "Waffles", "Pineapple fried rice", "Burgers", "Nachos", "Spring rolls",
            "Fried rice", "Pasta salad", "Stuffed peppers", "Quiche", "Fruit smoothies",
            "Chocolate mousse", "Pavlova", "Banana split", "Gelato", "Fruit tart",
            "Sushi rolls", "Gourmet burgers", "Tropical fruit salad", "Chocolate-covered pretzels"
        ],
        'activities': [
            "Hot air balloon", "Music festival", "Picnic", "Salsa dancing", "Amusement park",
            "Dance party", "Beach volleyball", "Karaoke night", "Potluck dinner", "Outdoor movie night",
            "Crafting", "Baking", "Playing board games", "Going for a hike", "Visiting a zoo",
            "Attending a concert", "Going to a comedy show", "Taking a cooking class", "Exploring a new city",
            "Going to a trampoline park", "Participating in a flash mob", "Going on a road trip",
            "Hosting a game night", "Joining a dance class", "Taking a painting class", "Going to a fair",
            "Visiting an amusement park", "Going to a festival", "Taking a scenic drive", "Going to a concert",
            "Trying a new sport", "Joining a community event", "Participating in a charity run"
        ]
    },
    'sad': {
        'movies': [
            "The Pursuit of Happyness", "Forrest Gump", "Inside Out", "The Notebook", 
            "Good Will Hunting", "A Star is Born", "The Fault in Our Stars", "Schindler's List", 
            "The Green Mile", "Eternal Sunshine of the Spotless Mind", "The Boy in the Striped Pajamas", 
            "Her", "The Road", "Requiem for a Dream", "The Lovely Bones", 
            "The Kite Runner", "A Walk to Remember", "Blue Valentine", 
            "The Time Traveler's Wife", "The Last Song", "The Perks of Being a Wallflower",
            "Me Before You", "The Book Thief", "The Help", "The Fault in Our Stars",
            "The Pursuit of Happyness", "The Lovely Bones", "The Road", "A Ghost Story",
            "Atonement", "The Fault in Our Stars", "The Lovely Bones", "The Road",
            "The Notebook", "The Pursuit of Happyness", "The Fault in Our Stars", "A Ghost Story"
        ],
        'places': [
            "Botanical garden", "Quiet lake", "Mountain cabin", "Monastery", "Secluded beach",
            "Cemetery", "Quiet library", "Art gallery", "Old bookstore", "Nature reserve",
            "Lighthouse", "Abandoned places", "Historical sites", "Countryside", "Small town",
            "Old church", "Deserted island", "Rainy park", "Foggy forest", "Peaceful meadow",
            "A quiet coffee shop", "A serene beach", "A tranquil forest", "A cozy cabin",
            "A quiet park", "A secluded beach", "A peaceful garden", "A quiet library",
            "A tranquil lake", "A serene mountain", "A quiet retreat", "A peaceful meadow"
        ],
        'songs': [
            "Fix You by Coldplay", "Someone Like You by Adele", "Let Her Go by Passenger",
            "Tears Dry on Their Own by Amy Winehouse", "Hallelujah by Jeff Buckley",
            "The Night We Met by Lord Huron", "Skinny Love by Bon Iver", "Back to December by Taylor Swift",
            "Breathe Me by Sia", "Chasing Cars by Snow Patrol", "The A Team by Ed Sheeran",
            "Someone You Loved by Lewis Capaldi", "I Will Always Love You by Whitney Houston",
            "Say Something by A Great Big World", "All I Want by Kodaline", "Let Her Go by Passenger",
            "Someone Like You by Adele", "Fix You by Coldplay", "Back to December by Taylor Swift",
            "The Night We Met by Lord Huron", "Skinny Love by Bon Iver", "Breathe Me by Sia",
            "Tears Dry on Their Own by Amy Winehouse", "Hallelujah by Jeff Buckley"
        ],
        'foods': [
            "Chicken noodle soup", "Chamomile tea", "Mac and cheese", "Apple pie", 
            "Warm bread pudding", "Chocolate chip cookies", "Warm apple cider", 
            "Grilled cheese and tomato soup", "Pasta with marinara sauce", "Rice pudding",
            "Mashed potatoes", "Pumpkin pie", "Brownies", "Peach cobbler", "Cinnamon rolls",
            "Comfort food platter", "Hot chocolate", "Baked potatoes", "Cheesy garlic bread",
            "Chocolate cake", "Pasta with cream sauce", "Baked ziti", "Stuffed peppers",
            "Chicken pot pie", "Shepherd's pie", "Beef stew", "Vegetable soup", "Chocolate fondue"
        ],
        'activities': [
            "Yoga", "Nature walk", "Reading", "Listening to music", "Jigsaw puzzles",
            "Writing in a journal", "Watching the rain", "Stargazing", "Meditation", 
            "Taking a long bath", "Gardening", "Volunteering", "Watching documentaries",
            "Creating art", "Knitting or crocheting", "Cooking comfort food", "Going for a drive",
            "Spending time with pets", "Listening to audiobooks", "Watching old movies",
            "Taking a leisurely walk", "Practicing mindfulness", "Doing yoga", "Journaling",
            "Watching a sad movie", "Listening to calming music", "Engaging in a creative hobby",
            "Going for a nature walk", "Spending time in a quiet place", "Reflecting on memories"
        ]
    },
    'angry': {
        'movies': [
            "Gladiator", "John Wick", "Fight Club", "The Equalizer", "Mad Max: Fury Road",
            "The Punisher", "Deadpool", "The Dark Knight", "Kill Bill", "Oldboy",
            "Law Abiding Citizen", "The Revenant", "American History X", "Training Day",
            "Django Unchained", "The Hateful Eight", "The Mechanic", "Lawless", "Warrior",
            "The Expendables", "Taken", "John Wick: Chapter 2", "The Equalizer 2",
            "Fight Club", "The Dark Knight Rises", "Gladiator", "The Punisher",
            "The Equalizer", "Law Abiding Citizen", "American History X", "John Wick"
        ],
        'places': [
            "Open field", "Mountain trail", "Gym", "Martial arts dojo", "Boxing ring",
            "Racetrack", "Paintball arena", "Shooting range", "Skate park", "Rock climbing gym",
            "Football field", "Basketball court", "Ice rink", "Soccer field", "Wrestling mat",
            "Axe throwing venue", "High ropes course", "Obstacle course", "Trampoline park",
            "A boxing gym", "A martial arts studio", "A sports arena", "A skate park",
            "A gym", "A boxing ring", "A racetrack", "A paintball arena"
        ],
        'songs': [
            "Lose Yourself by Eminem", "In the End by Linkin Park", "Stronger by Kanye West",
            "Break Stuff by Limp Bizkit", "Killing in the Name by Rage Against the Machine",
            "Bodies by Drowning Pool", "Walk by Pantera", "Duality by Slipknot",
            "Angry Again by Megadeth", "Freak on a Leash by Korn", "Killing in the Name by Rage Against the Machine",
            "Burn It Down by Linkin Park", "Fight Song by Rachel Platten", "I Will Not Bow by Breaking Benjamin",
            "Break Stuff by Limp Bizkit", "Killing in the Name by Rage Against the Machine",
            "Stronger by Kanye West", "Lose Yourself by Eminem", "In the End by Linkin Park"
        ],
        'foods': [
            "Spicy wings", "Indian curry", "Fiery Szechuan hot pot", "Buffalo wings", 
            "Espresso", "Chili", "Hot sauce", "Nachos with jalapeños", "Pepperoni pizza",
            "Szechuan noodles", "Spicy ramen", "Cajun shrimp", "Buffalo chicken dip",
            "Spicy tacos", "Jalapeño poppers", "Chili cheese fries", "Hot wings platter",
            "Spicy nachos", "Buffalo cauliflower", "Spicy chicken sandwich", "Hot pepper sauce",
            "Fiery hot wings", "Spicy beef stir-fry", "Szechuan chicken", "Spicy shrimp tacos",
            "Ghost pepper salsa", "Spicy sausage pizza", "Spicy chili con carne", "Hot pepper jelly"
        ],
        'activities': [
            "Boxing", "Kickboxing", "High-intensity workout", "Axe throwing", "Climbing",
            "Screaming into a pillow", "Heavy lifting at the gym", "Going for a run", 
            "Playing competitive sports", "Engaging in a debate", "Playing video games",
            "Participating in a team sport", "Going for a drive", "Practicing martial arts", 
            "Joining a local sports league", "Taking a self-defense class", "Participating in a charity run",
            "Going for a hike", "Playing a competitive game", "Engaging in a physical activity",
            "Joining a sports league", "Participating in a martial arts class", "Going to a boxing match"
        ]
    },
    'surprised': {
        'movies': [
            "Inception", "The Matrix", "The Sixth Sense", "Shutter Island", "Arrival",
            "Get Out", "Gone Girl", "Shutter Island", "The Prestige", "Fight Club",
            "The Others", "The Usual Suspects", "Memento", "The Cabin in the Woods",
            "The Game", "The Village", "The Witch", "The Invisible Man", "The Prestige",
            "The Secret in Their Eyes", "Oldboy", "The Orphanage", "The Others",
            "The Prestige", "The Sixth Sense", "Gone Girl", "Shutter Island",
            "The Prestige", "The Cabin in the Woods", "The Game", "The Village"
        ],
        'places': [
            "Grand Canyon", "Northern Lights", "Cave system", "Hot air balloon",
            "Escape room", "Haunted house", "Mystery mansion", "Abandoned amusement park",
            "Secret garden", "Hidden beach", "Underground tunnels", "Historical ruins",
            "A unique art installation", "A pop-up restaurant", "A themed café", "An escape room",
            "A secret garden", "A hidden waterfall", "A mysterious cave", "A ghost town",
            "A hidden treasure", "A secret location", "An undiscovered island", "A mysterious forest"
        ],
        'songs': [
            "Bohemian Rhapsody by Queen", "Radioactive by Imagine Dragons",
            "Uptown Funk by Mark Ronson ft. Bruno Mars", "Somebody That I Used to Know by Gotye",
            "Take On Me by a-ha", "Sweet Child O' Mine by Guns N' Roses", "Crazy by Gnarls Barkley",
            "Shape of You by Ed Sheeran", "Rolling in the Deep by Adele", "Chasing Cars by Snow Patrol",
            "Somebody That I Used to Know by Gotye", "Shallow by Lady Gaga and Bradley Cooper",
            "Radioactive by Imagine Dragons", "Somebody That I Used to Know by Gotye",
            "Bohemian Rhapsody by Queen", "Uptown Funk by Mark Ronson ft. Bruno Mars"
        ],
        'foods': [
            "Molecular gastronomy", "Exotic fruit platter", "Rainbow cake",
            "Sushi", "Surprise cake", "Charcuterie board", "Fusion cuisine",
            "Deconstructed dishes", "Savory ice cream", "Gourmet popcorn",
            "Bento box", "Sushi burrito", "Gourmet donuts", "Artisan chocolates",
            "Surprise dessert", "Mystery dish", "Exotic cuisine", "Gourmet meal",
            "Unexpected flavor combinations", "Surprise tasting menu", "Mystery box meal"
        ],
        'activities': [
            "Skydiving", "Bungee jumping", "Escape room", "Spontaneous road trip",
            "Flash mob", "Mystery dinner", "Surprise party planning", "Treasure hunt",
            "Participating in a scavenger hunt", "Going to a pop-up event",
            "Visiting a surprise destination", "Trying a new hobby", "Joining a flash mob",
            "Going on an adventure", "Participating in a spontaneous event", "Exploring a new place",
            "Going on a surprise trip", "Joining a mystery tour", "Participating in a surprise event"
        ]
    },
    'neutral': {
        'movies': [
            "The Social Network", "Julie & Julia", "The Intern", "Chef", 
            "Little Miss Sunshine", "The Pursuit of Happyness", "The Intern",
            "The Secret Life of Walter Mitty", "About Time", "The Hundred-Foot Journey",
            "The King's Speech", "The Imitation Game", "The Theory of Everything",
            "The Secret Life of Pets", "The Intern", "The Greatest Showman", "The Help",
            "The Social Network", "Julie & Julia", "The Intern",
            "The Pursuit of Happyness", "The Hundred-Foot Journey", "The King's Speech"
        ],
        'places': [
            "Art museum", "Quiet café", "Countryside", "Botanical garden", "City park",
            "Bookstore", "Coffee shop", "Local farmer's market", "Community center",
            "Public library", "Historical district", "Nature trail", "A peaceful beach",
            "A scenic overlook", "A quaint village", "A botanical garden",
            "A quiet park", "A serene garden", "A local café", "A peaceful library",
            "A tranquil garden", "A quiet retreat", "A scenic park", "A peaceful nature reserve"
        ],
        'songs': [
            "Imagine by John Lennon", "Let It Be by The Beatles", 
            "Breathe Me by Sia", "Here Comes the Sun by The Beatles",
            "What a Wonderful World by Louis Armstrong", "Lean on Me by Bill Withers",
            "Count on Me by Bruno Mars", "Three Little Birds by Bob Marley",
            "Don't Stop Believin' by Journey", "Good Riddance (Time of Your Life) by Green Day",
            "Here Comes the Sun by The Beatles", "Imagine by John Lennon",
            "Let It Be by The Beatles", "Breathe Me by Sia"
        ],
        'foods': [
            "Pho", "Greek salad", "BLT sandwich", "Quiche", "Caesar salad",
            "Caprese salad", "Hummus and pita", "Smoothie bowl", "Avocado toast",
            "Chia pudding", "Granola bars", "Fruit smoothie", "Rice paper rolls",
            "Mediterranean platter", "Sushi rolls", "Veggie wrap",
            "Quinoa salad", "Fruit salad", "Pasta salad", "Grilled vegetables",
            "Vegetable stir-fry", "Mediterranean bowl", "Grilled chicken salad"
        ],
        'activities': [
            "Meditation", "Crossword puzzle", "Biking", "Documentary", 
            "Organizing", "Gardening", "Listening to podcasts", "Cooking new recipes",
            "Exploring local attractions", "Volunteering at a shelter", "Birdwatching",
            "Taking a leisurely walk", "Practicing mindfulness", "Doing yoga", "Journaling",
            "Reading a book", "Watching a documentary", "Exploring a new hobby",
            "Taking a nature walk", "Engaging in a creative project", "Participating in a community event"
        ]
    }
}

sample_recommendations = []

for emotion, data in recommendations.items():
    for movie in data['movies']:
        sample_recommendations.append((emotion, f"Watch '{movie}'", 1))
    for place in data['places']:
        sample_recommendations.append((emotion, place, 2))
    for song in data['songs']:
        sample_recommendations.append((emotion, f"Listen to '{song}'", 3))
    for food in data['foods']:
        sample_recommendations.append((emotion, food, 4))
    for activity in data['activities']:
        sample_recommendations.append((emotion, activity, 5))

cursor.executemany('INSERT INTO recommendations (emotion, recommendation, category_id) VALUES (?, ?, ?)', sample_recommendations)

conn.commit()
conn.close()