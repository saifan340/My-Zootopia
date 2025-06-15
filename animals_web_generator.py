import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

data = load_data('animals_data.json')

def generate_animals_html(output):
     with open("animals_template.html", "r") as file:
          html_content =file.read()
     updated_html_content =html_content.replace("__REPLACE_ANIMALS_INFO__", output)
     with open('animals_data.html', 'w') as file:
         file.write(updated_html_content)



output=''
if data:
   for animal_data in data:
       output +='<li class="cards__item">'
       if 'name' in animal_data:
           output += f"Name: {animal_data['name']}<br/>\n"
       if 'characteristics' in animal_data and 'diet' in animal_data['characteristics']:
           output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
       if 'locations' in animal_data:
           locations=animal_data["locations"]
           output += f"Location: {locations[0]}<br/>\n"
       if 'characteristics' in animal_data and 'type' in animal_data['characteristics']:
           output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
       output +='</li>'
   print(output)
generate_animals_html(output)