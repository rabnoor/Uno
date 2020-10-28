from card import *
import random

from player import Player


class Game:
    INITIAL_NUMBER_CARDS = 7

    def __init__(self, player_names):
        self.deck = Game.create_initial_deck()
        self.played_cards = []
        self.num_players = len(player_names)
        self.players = [self.create_player(player) for player in player_names]
        self.game_end = False
        self.current_turn = random.randint(0, self.num_players - 1)
        self.reverse = False
        self.used_cards = []
        self.top_card = self.get_top_card()
        self.winner = None

    def create_player(self, player_name):
        cards = []
        for i in range(Game.INITIAL_NUMBER_CARDS):
            cards.append(self.deck.pop())
        return Player(player_name, cards)

    @staticmethod
    def create_initial_deck():
        deck = []
        for color in CardColor.normal_colors():
            for value in CardValue.normal_values() + CardValue.action_values():
                if value == CardValue.ZERO:
                    deck.append(Card(color, value))
                else:
                    deck.append(Card(color, value))
                    deck.append(Card(color, value))

        for value in CardValue.special_values():
            for i in range(4):
                deck.append(Card(CardColor.SPECIAL, value))
        random.shuffle(deck)
        return deck

    def get_top_card(self):
        top_card = self.deck.pop()
        extras = []
        while top_card.value not in CardValue.normal_values() or top_card.color not in CardColor.normal_colors():
            extras.append(top_card)
            top_card = self.deck.pop()
        self.deck.extend(extras)
        self.used_cards.append(top_card)
        return top_card

    def next_player_turn(self):
        current_turn = self.current_turn
        if self.reverse:
            current_turn -= 1
            if current_turn == -1:
                current_turn = self.num_players - 1
        else:
            current_turn = (current_turn + 1) % self.num_players
        return current_turn

    def change_turn(self):
        self.current_turn = self.next_player_turn()

    def current_player(self):
        return self.players[self.current_turn]

    def is_valid_play(self, card):
        return card.value == self.top_card.value or card.color == self.top_card.color or card.color == CardColor.SPECIAL

    def get_n_cards(self, n):
        if n > len(self.deck):
            self.deck.extend(self.used_cards)
            random.shuffle(self.deck)
            self.used_cards.clear()
        return [self.deck.pop() for _ in range(n)]

    def play_normal_card(self, card):
        if not self.is_valid_play(card) or card.color == CardColor.SPECIAL or card not in self.current_player().cards:
            return False

        self.top_card = card
        self.current_player().remove_card(card)
        if self.current_player().is_winner():
            self.game_end = True
            self.winner = self.current_player()
        self.used_cards.append(card)
        if card.value == CardValue.SKIP:
            self.change_turn()
        elif card.value == CardValue.REVERSE:
            self.reverse = not self.reverse
        elif card.value == CardValue.PLUS2:
            self.players[self.next_player_turn()].add_cards(self.get_n_cards(2))
            self.change_turn()

        self.change_turn()
        return True

    def draw_single_card(self):
        drawn_card = self.get_n_cards(1)
        self.current_player().add_cards(drawn_card)
        return drawn_card[0]

    def play_special_card(self, card, color_choice):
        if card.color != CardColor.SPECIAL:
            return False

        self.top_card = card
        self.current_player().remove_card(card)
        if self.current_player().is_winner():
            self.game_end = True
            self.winner = self.current_player()
        self.used_cards.append(card)
        self.top_card.color = color_choice
        if card.value == CardValue.PLUS4:
            self.players[self.next_player_turn()].add_cards(self.get_n_cards(4))
            self.change_turn()
        self.change_turn()
        return True


if __name__ == '__main__':
    if len(Game().deck) != 108:
        print("error: there are not 108 cards in the deck")
