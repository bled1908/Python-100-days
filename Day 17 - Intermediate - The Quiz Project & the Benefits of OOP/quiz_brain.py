class QuizBrain:
    
    def __init__(self, questions_list):
        """
        Initializes the QuizBrain object.

        Args:
            questions_list (list): A list of question objects to be used in the quiz.

        Attributes:
            question_number (int): Tracks the current question number in the quiz.
            questions_list (list): Stores the list of question objects.
            score (int): Tracks the user's score throughout the quiz.
        """
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        
    def still_has_questions(self):
        """
        Checks if there are more questions left in the quiz.

        Returns:
            bool: True if there are questions remaining, False otherwise.
        """
        return self.question_number < len(self.questions_list)
  
    def next_question(self):
        """
        Presents the next question to the user, takes their answer as input, 
        and checks if it is correct.
        """
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer against the correct answer and updates the score if correct.

        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer to the question.

        Side Effects:
            Updates the score if the user's answer is correct.
            Prints feedback and the current score.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}\n")
            
            
        