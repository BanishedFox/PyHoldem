suites = ["Hearts", "Spades", "Clubs", "Diamonds"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
royalty = ["Ace", "Jack", "Queen", "King"]

completedDeck = []

for each in suites:
    for num in numbers:
        completedDeck.append(((num)+(" of ")+(each)))
    for royal in royalty:
        completedDeck.append(((royal)+(" of ")+(each)))
