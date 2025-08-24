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
    HTML_text += '<li class="cards__item">'
    HTML_text += '<div class="card__title">'
    HTML_text += f"{animal["name"]}<br/></div>\n"
    HTML_text += '<p class="card__text">'
    HTML_text += f"<strong>Diet: </strong> {animal["characteristics"]["diet"]}<br/>\n"

    HTML_text += f"<strong>Location: </strong> {animal["locations"][0]}<br/>\n"

    HTML_text += f"<strong>Type: </strong> {animal["characteristics"]["type"]}<br/>\n"
    HTML_text += '</p>'
    HTML_text += "</li>\n"

  except KeyError:
    HTML_text += "</li>\n"

#print(HTML_text)

new_HTML = old_HTML.replace("__REPLACE_ANIMALS_INFO__", HTML_text)

# Creating a new HTML file with the new HTML text
with open("animals.html", "w") as animal_HTML:
  animal_HTML.write(new_HTML)




