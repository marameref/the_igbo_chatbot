import json
import random
import os

class Chatbot:
    def __init__(self, dataset_path=None):
        # Default path to the dataset if none is provided
        if dataset_path is None:
            # Get the absolute path to the 'data/igbo_faq.json' relative to the 'app' folder
            dataset_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'igbo_faq.json')
        
        # Debugging: Print the absolute path of the dataset
        print("Dataset Path:", os.path.abspath(dataset_path))
        
        # Load dataset from the JSON file when the chatbot is initialized
        self.dataset = self.load_dataset(dataset_path)

    def load_dataset(self, path):
        """Load dataset from a JSON file."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"Error: The dataset file at '{path}' could not be found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: The file at '{path}' is not a valid JSON file.")
            raise

    def get_response(self, user_input):
        """
        Match user input with a question and return a response.
        :param user_input: User's input query for the chatbot.
        :return: Chatbot's response.
        """
        user_input_lower = user_input.lower()

        # Loop through the dataset and check for matching questions
        for item in self.dataset:
            for question in item["questions"]:
                if user_input_lower in question.lower():
                    return random.choice(item["answers"])

        # If no match found, return fallback response
        return "Ndo! Enyemaka anaghị dị maka ajụjụ a ugbu a. Biko nwalee ajụjụ ọzọ."