from game import *
from os import system
from time import sleep

def get_valid_num(string, lo, hi):
    a = input(string)
    while (not a.isdigit()) or int(a) >= hi or int(a) < lo:
        a = input("please enter a valid input.")
    return int(a)


def get_valid_card_choice(game: Game):
    card_choice_index = get_valid_num("Please choose the card", 0, len(game.current_player().cards) + 1)
    while card_choice_index != len(
            game.current_player().cards) and not game_state.is_valid_play(
        game.current_player().cards[card_choice_index]):
        card_choice_index = get_valid_num(
            "Cannot play card " + str(
                game.current_player().cards[card_choice_index]) + " please select a valid card",
            0, len(game.current_player().cards) + 1)
    if card_choice_index != len(game.current_player().cards):
        return True, game.current_player().cards[card_choice_index]
    else:
        return False, None


def get_valid_color_choice():
    color_choice_index = get_valid_num(
        "Please choose the color " + str(
            [str(i) + ":" + str(color) for i, color in enumerate(CardColor.normal_colors())]),
        0, len(CardColor.normal_colors()))
    return CardColor.normal_colors()[color_choice_index]


def print_current_player_info(game: Game):
    print("Top Card: ", game.top_card)
    print(game.current_player())
    print(len(game.current_player().cards),"Draw a card")


if __name__ == '__main__':
    num_players = get_valid_num("Welcome! please enter the number of players (2-4)", 0, 5)
    game_state = Game(["player" + str(i + 1) for i in range(num_players)])
    while not game_state.game_end:
        print_current_player_info(game_state)
        no_draw, card = get_valid_card_choice(game_state)
        if not no_draw:
            card = game_state.draw_single_card()
            print("Drawn card is", card)
            if game_state.is_valid_play(card):
                if get_valid_num("Enter 1 to play current card and 0 to pass", 0, 2) == 0:
                    game_state.change_turn()
                    continue
            else:
                print(card, "cannot be played")
                game_state.change_turn()

        if card.color == CardColor.SPECIAL:
            color_choice = get_valid_color_choice()
            game_state.play_special_card(card, color_choice)
        else:
            game_state.play_normal_card(card)
        sleep(2)
        system("clear")
        input("Press any key to continue")
    print("The winner is", game_state.winner.name)
