import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):

        self.card1 = Card("Spade", 1)
        self.card2 = Card("Heart", 6)
        self.card3 = Card("Diamond", 12)
        self.card4 = Card("Club", 4)
        self.cards = [self.card1, self.card2, self.card3, self.card4]

        self.card_game = CardGame()

    def test_check_for_ace__true(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)
    
    
    def test_check_for_ace__false(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card3, self.card4)
        self.assertEqual(self.card3, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 23", result)

    