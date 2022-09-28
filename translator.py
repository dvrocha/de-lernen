import requests
import sys
import time
import codecs

headers = {
        'content-type': 'application/json',
    }

word_array = [
"unersetzliche",
"leicht",
"verstehen",
"lassen",
"innerhalb",
"bezahlt",
]


output_text = ""

def trans(word):
    build_url = "https://linguee-api-v2.herokuapp.com/api/v2/translations?query=" + word + "&src=de&dst=en&guess_direction=true&follow_corrections=always"
    requestget = requests.get(build_url, headers=headers)
    #print(requestget.json())
    y = requestget.json()
    global output_text
    #print(json.dumps(y, indent=2))
    #print(y)
    if not y:
        return
    if 'message' in y:
        return
    #print(output_text)
    output_text += word +";\""
    #Pos
    for translation in y:
        position = (translation["pos"])
        #Text Original
        original_text = (translation["text"])
        #Translation
        translation_array = (translation["translations"])
        
        output_text += "<br><b> - Position:</b> " + position + "\n<br>" + "<b> - Original Text:</b>" + original_text + "\n<br>"
        for translation in translation_array:
            if translation["featured"] == True:
                output_text += "<br><b>Translation:</b> " + translation["text"].replace("\"", "\'")
                output_text += "<br>Examples: "
                for example in translation["examples"]:
                    output_text += "<br><b>DE:</b> " + example["src"].replace("\"", "\'")
                    output_text += "<br><b>EN:</b> " + example["dst"].replace("\"", "\'")
                    #print("<br>\n")
                output_text += "<br>"
                output_text += "\n"
                
    output_text += "\""
    output_text += "\n"    


    

for word in word_array:
    trans(word=word)
    time.sleep(1)

print(output_text)

f = codecs.open("sample.txt", "w", "utf-8")
f.write(output_text)
