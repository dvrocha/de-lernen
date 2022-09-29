import requests
import codecs
from bs4 import BeautifulSoup
import time



word_array = [
"Hochzeit",
"weinen",
"Verlobter",
"worüber",
"aufgeregt",
"furchtbar",
"überhaupt",
"ständig",
"niesen",
"während",
]

output_text = ""
for word in word_array:
    time.sleep(3)
    url_base = "https://www.linguee.com/english-german/search?source=german?destination=english?&query=" + word
    page = requests.get(url_base)
    soup = BeautifulSoup(page.text, "html.parser")
    print(word)
    results = soup.find(id="dictionary")

    translations = results.find_all("div", class_="lemma featured")
    output_text += word + ";\""
    for translation in translations:
        output_text += "\n<br><b> - Position: </b>" + translation.find("span", class_="tag_wordtype").text.strip()
        output_text += "\n<br><b>DE: </b> " + translation.find("a", class_="dictLink").text.strip()
        output_text += "\n<br><b>EN: </b> " + translation.find("a", class_="dictLink featured").text.strip()

        examples = translation.find_all("span", class_="tag_e")       
        if examples:
            output_text += "\n<br><b>Examples: </b>"
            for example in examples:
                output_text += "\n<br><b>DE: </b>" + example.find("span", class_="tag_s").text.strip()
                output_text += "\n<br><b>EN: </b>" + example.find("span", class_="tag_t").text.strip()
                if examples.index(example) == len(examples)-1:
                    output_text += "\n<br><br>"
                else:
                    output_text += "\n<br>-"
        else:
            output_text += "\n<br><br>"
        
    output_text += "\"\n"
            


#print(output_text)

f = codecs.open("sample.txt", "w", "utf-8")
f.write(output_text)

write_history = codecs.open("translator_history.txt", "a", "utf-8")
write_history.write("\n" + str(word_array))
