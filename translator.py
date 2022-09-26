import requests
import sys
import time

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

word_array2 = ["Ruhrgebiet",
"Beschäftigten",
"Ländern",
"wissenschaftlichen",
"vereint",
"Fakultäten",
"Spektrum",
"europäischen",
"Studiengänge",
"angeboten",
"Untereinander",
"Fakultät",
"fachübergreifende",
"schärfen",
"bewährtes",
"Förderung",
"Nachwuchs",
"hervorrangende",
"Ruhr"]



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
    
    print("Position: " + position + "\n" + "Original Text: " + original_text + "\n")
    for translation in translation_array:
        if translation["featured"] == True:
            print( "Translation: " + translation["text"].replace("\"", "\'"))
            print("Examples: ")
            for example in translation["examples"]:
                print("DE: " + example["src"].replace("\"", "\'"))
                print("EN: " + example["dst"].replace("\"", "\'"))

    

for word in word_array:
    print(word +";\"")
    trans(word=word)
    time.sleep(5)
    print("\"")
