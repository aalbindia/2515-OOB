import pytest
from unittest.mock import patch, mock_open
from week7.game import Game  # Adjust the import if needed

JSON_FILE = """
[
    {
        "question": "MEDIUM question (general category)?",
        "correct_answer": "correct",
        "incorrect_answers": ["wrong", "false", "incorrect"],
        "category": "general",
        "difficulty": "medium"
    },
    {
        "question": "HARD question (other category)?",
        "correct_answer": "correct",
        "incorrect_answers": ["wrong", "false", "incorrect"],
        "category": "other",
        "difficulty": "hard"
    }
]
"""

@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
@patch("builtins.input", side_effect=["", "", "10"])
@patch("random.shuffle")
def game(mock_random, mock_input, mock_file):
    """We create a rigged game where the answers are 1 and then 4"""
    g = Game(category="general")  # Make sure this matches the category in the mock data
    print(f"Loaded questions: {g.questions}")  # Debugging line
    # Force the answer to question 1
    g.questions[0].answer_id = 1
    # Force the answer to question 2 (if there are two questions)
    if len(g.questions) > 1:
        g.questions[1].answer_id = 4
    # Now we know all the answers!
    return g


def test_game(game):
    """Send various user inputs and check the resulting game"""
    
    assert len(game.questions) == 1  # There should be at least 1 question loaded

    # If there are two questions, force the answer to question 2
    if len(game.questions) > 1:
        game
