import json

def read_HTML(file_path):
  """ Reads the data from the HTML file"""
  with open(file_path, "r") as handle:
    return handle.read()

old_HTML = read_HTML("animals_template.html")

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

#print(len(animals_data))

# to store the HTML text
HTML_text = ""

# To generate the display info from the json file
for animal in animals_data:
  try:
    # Appending data to the HTML string
    HTML_text += f"Name: {animal["name"]}\n"

    HTML_text += f"Diet: {animal["characteristics"]["diet"]}\n"

    HTML_text += f"Location: {animal["locations"][0]}\n"

    HTML_text += f"Type: {animal["characteristics"]["type"]}\n"
    HTML_text += "\n"

  except KeyError:
    HTML_text += "\n"

#print(HTML_text)

new_HTML = old_HTML.replace("__REPLACE_ANIMALS_INFO__", HTML_text)

# Creating a new HTML file with the new HTML text
with open("animals.html", "w") as animal_HTML:
  animal_HTML.write(new_HTML)




