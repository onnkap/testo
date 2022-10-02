import unittest
from hangman import Hangman
class TestLengthCheck(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.hangman= Hangman()
  #Each test method starts with the keyword test_
  def test_check(self):
    self.assertEqual(self.hangman.count(5), "-----")
  def test_lcheck(self):
    word="стол"
    guess="с"
    so_far=""
    for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
      if guess == word[i]:
        new += guess
      else:
        new += so_far[i]
    place = new
    return place
    self.assertEqual(self.hangman.lettercheck,(guess,word,so_far), "c___")
if __name__ == "__main__":
  unittest.main()
