import translator as tr

t = tr.Translator()

stop=False

while(stop!=True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Scegli: ")

    # Add input control here!

    if int(txtIn) == 1:
        entry = input("Inserisci la nuova parola e la relativa traduzione: ")
        t.handleAdd(entry)

    if int(txtIn) == 2:
        entry = input("Inserisci la parola aliena: ")
        t.handleTranslate(entry)

    if int(txtIn) == 3:
        entry = input("Inserisci la parola aliena con un '?' al posto di un qualsiasi carattere: ")
        t.handleWildCard(entry)

    if int(txtIn) == 4:
        t.__str__()

    if int(txtIn) == 5:
        stop=True
