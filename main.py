from scraper import *


class Word:
    def __init__(self, letters):
        self.word = letters
        self.word_type = ""
        self.definition = []

input_string = "Diaphanous Despot"
#"Debacle, Debauch, Debunk, Defunct, Demagogue, Denigrate, Derivative, Despot"
words_scraped_count = 0
with open("words.txt", "r") as file:
    wordlist = file.read().split("\n\n")
file.close()

Words = []
scraped_words = []

for word in wordlist:
    new_word = Word(word)
    Words.append(new_word)

print("made the words into classes")

for word in Words:
    scraped_words.append(ScrapeWord(word))
    words_scraped_count += 1
#print("\n\n".join(scraped_words))
#print(words_scraped_count)

with open("words_scraped.txt", "w") as file:
    file.write("\n\n".join(scraped_words))
file.close()
print("Done")
