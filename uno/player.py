class Player:
    def __init__(self, name, cards):
        self.cards = cards
        self.name = name

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_card(self, card):
        self.cards.remove(card)

    def is_winner(self):
        return len(self.cards) == 0

    def __str__(self):
        return "Player name: " + self.name + " " + "\n" + "Player Cards: \n" + "\n".join(
            [str(idx) + str(card) for idx, card in enumerate(self.cards)])
