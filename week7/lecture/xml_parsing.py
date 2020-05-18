from bs4 import BeautifulSoup

my_file = open("text_files/famous_quotes.xml", encoding="utf-8")

my_text = my_file.read()

for (index, character) in enumerate(my_text):
    try:
        encoder = character.encode("ascii")
    except:
        print(index, character, ord(character))
        if ord(character) == 8220:
            my_text = my_text.replace(character, '"')
        if ord(character) == 8221:
            my_text = my_text.replace(character, '"')

my_xml = BeautifulSoup(my_text, "xml")

my_quotes = my_xml.find_all("quote_item")

for quote in my_quotes:
    print(quote.person.get_text())
    print("said " + quote.quote.get_text())