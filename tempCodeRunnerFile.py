import sqlite3

def get_recommendations(emotion):
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT r.recommendation, c.name 
        FROM recommendations r 
        JOIN categories c ON r.category_id = c.id 
        WHERE r.emotion = ?
    ''', (emotion,))
    
    recommendations = cursor.fetchall()
    conn.close()

    if not recommendations:
        print(f"No recommendations found for emotion: {emotion}")
        return []


    categorized_recommendations = {'movie': [], 'place': [], 'song': [], 'food': [], 'activity': []}
    for recommendation, category in recommendations:
        if category in categorized_recommendations:
            categorized_recommendations[category].append(recommendation)


    selected_recommendations = []
    for category in categorized_recommendations:
        if categorized_recommendations[category]:
            selected_recommendations.append((random.choice(categorized_recommendations[category]), category))


    while len(selected_recommendations) < 5:
        for category in categorized_recommendations:
            if categorized_recommendations[category] and len(selected_recommendations) < 5:
                recommendation = random.choice(categorized_recommendations[category])
                if recommendation not in [rec[0] for rec in selected_recommendations]:
                    selected_recommendations.append((recommendation, category))

    return selected_recommendations