import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(len(animals_data))

for animal in animals_data:
  try:
    name = animal["name"]
    print(f"Name: {name}")
    diet = animal["characteristics"]["diet"]
    print(f"Diet: {diet}")
    location = animal["locations"][0]
    print(f"Location: {location}")
    typ = animal["characteristics"]["type"]
    print(f"Type: {typ}")
    print()

  except KeyError:
    print()

