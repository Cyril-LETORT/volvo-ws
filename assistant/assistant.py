"""
Develop a class called NutritionalAssistant that will help users to track their daily
food intake and provide nutritional information about the food they eat.
The class should have the following methods:

1. __init__(self, name: str, age: int, weight: float, height: float
2. add_meal(self, calories: int)
3. get_calories(self) -> int
4. get_bmr(self) -> float
5. set_preferences(self, preferences: str)
6. set_allergies(self, allergies: str)
7. create_suggestion(self)
  Using OpenAI's API, the create_suggestion method should generate a suggestion based
  on the user's preferences and allergies.
8. run(self)
  The run method should provide a CLI style interface for the user to interact with the
  assistant. The user should be able to add meals, get nutritional information, set
  preferences and allergies, and generate a suggestion.
"""

import requests
from assistant.const import API_KEY, PROJECT_ID

class NutritionalAssistant:
  pass
