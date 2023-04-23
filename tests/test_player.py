class Player:
    def __init__(self, player_id, player_type, letter):
        self.player_id = player_id
        self.player_type = player_type
        self.letter = letter

    def test_player():
        player1 = Player(1, "human", "S")
        assert player1.player_id == 1
        assert player1.player_type == "human"
        assert player1.letter == "S"

        player2 = Player(2, "computer", "O")
        assert player2.player_id == 2
        assert player2.player_type == "computer"
        assert player2.letter == "O"
        