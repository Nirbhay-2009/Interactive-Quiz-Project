# Scores for each personality category

scores = {
    "Analytical Thinker": 0,
    "Creative Innovator": 0,
    "Leader": 0,
    "Social Helper": 0
}


# Function to calculate score

def calculate_score(category):

    if category in scores:
        scores[category] += 1


# Function to get the final personality

def get_result():

    highest_score = max(scores.values())

    for category in scores:

        if scores[category] == highest_score:
            return category