import json
import os

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
        base_dir = os.path.dirname(os.path.abspath(file_path))
        project_dir = os.path.dirname(base_dir)

        bosses = {}
        for name, entry in data.items():
            # Prefer explicit image path from JSON and resolve it from project root.
            image_relative = entry.get('image')
            if image_relative:
                image_path = os.path.join(project_dir, image_relative)
            else:
                generated = f"{name.lower().replace(',', '').replace(' ', '_')}.jpg"
                image_path = os.path.join(project_dir, "images", generated)

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
