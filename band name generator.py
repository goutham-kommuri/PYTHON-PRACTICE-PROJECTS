import random

# Lists of adjectives and nouns
adjectives = ["Electric", "Dark", "Golden", "Silent", "Wild"]
nouns = ["Echo", "Flame", "Wave", "Spirit", "Skyline"]

# Function to generate a single band name
def generate_band_name():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj} {noun}"

# Generate and print 10 band names
for _ in range(10):
    print(generate_band_name())

