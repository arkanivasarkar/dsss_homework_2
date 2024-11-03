import random

def generate_random_number(min: int, max: int):
    """
    Return a random integer in between the given range of min-max.
    """
    return random.randint(min, max)


def generate_random_operation():
    """
    Return a random choice between the strings '+', '-', and '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate_operation(number_1: int, number_2: int, operation: str):
    """
    Function to calculate the operation with the given numbers and return the problem title and result.
    """

    problem = f"{number_1} {operation} {number_2}" #Problem title

    # Perform operations with the two numbers according to the operation type.
    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    else:
        result = number_1 * number_2

    return problem, result



def math_quiz():
    """
    Function for Math Quiz Game which calls calculate_operation() function for calculation.
    """
    score = 0
    num_trials = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_trials):
        number_1 = generate_random_number(1, 10)    # select a random number from 1 to 10
        number_2 = generate_random_number(1, 5)     # select a random number from 1 to 5
        operation = generate_random_operation()     # an operation is chosen randomly

        # Calculate result
        PROBLEM, ANSWER = calculate_operation(number_1, number_2, operation)  

        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        try:
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

        # Executed if user input is not an integer
        except:                             
            print(f"Incorrect input provided. Input should be an integer.")

    print(f"\nGame over! Your score is: {score}/{num_trials}")


if __name__ == "__main__":
    math_quiz()
