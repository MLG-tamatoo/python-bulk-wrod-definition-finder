from bs4 import BeautifulSoup
import requests

def ScrapeWord(word):

    print("sending request for word " + word.word)
    source = requests.get("https://www.merriam-webster.com/dictionary/" + word.word).text
    soup = BeautifulSoup(source, 'lxml')

    definitions_list = []
    final_definitions = []
    word_type = ""


    page = soup.find("div", {"class": "outer-container"})
    real_page = page.find("div", {"class": "main-container"})
    content = real_page.find("div", {"id": "definition-wrapper"})
    definition = content.find("div", {"class": "row"})
    left_side = definition.find("div", {"id", "left-content"})

    try:
        word_header = left_side.find("div", {"class", "row entry-header"})
        word_header_stuff = word_header.find("div", {"class", "col-12"})
        span = word_header_stuff.find("span", {"class", "fl"})
        word_type = span.find("a", {"class", "important-blue-link"}).string
        word.word_type = word_type

    except:
        word_type = "error"

    dts = left_side.findAll("span", {"class", "dt"})
    try:
        for definition in dts:
            dtText = definition.find("span", {"class", "dtText"})
            definition_parts = []
            for text in dtText.contents:
                #print(type(text))
                if (text.string != None):
                    definition_parts.append(text.string)
            definitions_list.append(definition_parts)
            #print(definitions_list)
    except:
        definitions_list = ["error"]
    for definition_part_list in definitions_list:
        end_string = ""
        for part in definition_part_list:
            end_string = end_string + part
        final_definitions.append(end_string)
    #print(final_definitions)
    #print("\n")

    return_string = word.word + " - " + word_type + " - " + " or ".join(final_definitions[0:2])

    return return_string
