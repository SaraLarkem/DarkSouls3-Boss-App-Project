import json

class Boss:
    def __init__(self, name, location, difficulty, weaknesses, lore, image, prerequisites=None):
        self.name = name
        self.location = location
        self.difficulty = difficulty
        self.weaknesses = weaknesses
        self.lore = lore
        self.image = image
        self.prerequisites = prerequisites if prerequisites else []
        self.defeated = False
        self.phase_tips = {"phase_1": "", "phase_2": ""}
        self.points = 0

    def mark_defeated(self):
        self.defeated = True
        self.points += 10

def load_bosses_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        bosses = {}
        for name, entry in data.items():
            # Construct the image path based on the boss name
            image_path = f"images/{name.lower().replace(',', '').replace(' ', '_')}.jpg"

            # Create a Boss object using the data from the JSON
            boss = Boss(
                name=name,
                location=entry.get('location', ''),
                difficulty=entry.get('difficulty', 0),
                weaknesses=entry.get('weaknesses', []),
                lore=entry.get('lore', ''),
                image=image_path,
                prerequisites=entry.get('prerequisites', [])
            )
            # Assign additional properties
            boss.phase_tips = entry.get('phase_tips', {})
            boss.points = entry.get('points', 0)
            boss.defeated = entry.get('defeated', False)

            # Add the boss to the dictionary with the boss name as the key
            bosses[name] = boss

        return bosses
