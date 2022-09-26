import requests
import sys

headers = {
        'content-type': 'application/json',
    }

word_array = ["Auslöschen",
"aufzureißen",
"darf",
"feine",
"durchhalten",
"irgendwelche",
"Beschwerden",
"Ding",
"davon",
"lebendige",
"scheinst",
"Finte",
"durchschaut",
"Einzelheiten",
"Ahnung",
"Hitzkopf",
"AnFührer" ]

def trans(word):
    build_url = "https://linguee-api-v2.herokuapp.com/api/v2/translations?query=" + word + "&src=de&dst=en&guess_direction=true&follow_corrections=always"
    requestget = requests.get(build_url, headers=headers)
    #print(requestget.json())
    y = requestget.json()


    #print(json.dumps(y, indent=2))
    #Pos
    position = (y[0]["pos"])
    #Text Original
    original_text = (y[0]["text"])
    #Translation
    translation_array = (y[0]["translations"])
    
    print("Position: " + position + "\n" + "Original Text: " + original_text + "\n" + "Translation: ")
    for translation in translation_array:
        if translation["featured"] == True:
            print(translation["text"])
            print("Examples: ")
            print(translation["examples"])
    
    print("\n")


for word in word_array:
    print("Word: " + word)
    trans(word=word)
