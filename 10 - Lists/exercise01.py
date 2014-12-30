# exercise prompt as follows:
# Expand the test.py program so it has a menu giving the option of taking
# the test, viewing the list of questions and answers, and an option to
# quit. Also, add a new question to ask, "What noise does a truly advanced
# machine make?" with the answer of "ping".


questions = [["What color is the daytime sky on a clear day? ", "blue"],
             ["What is the answer to life, the universe and everything? ",
              "42"],
             ["What is a three letter word for a mouse trap? ", "cat"],
             ["What noise does a truly advanced machine make? ", "ping"]]

# This will test a single question
# it takes a single question in
# it returns True if the user typed the correct answer, otherwise false


def check_question(question_and_answer):
    # extract the question and the answer from the list
    # This function takes a list with two elements, a question and an answer.
    question = question_and_answer[0]
    answer = question_and_answer[1]
    # give the question to the user
    given_answer = input(question)
    # compare the user's answer to the tester's answer
    if answer == given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct was:", answer)
        return False

# This will run through all the questions


def run_test(questions):
    if len(questions) == 0:
        print("No questions were given.")
        # the return exist the function
        return
    index = 0
    right = 0
    while index < len(questions):
        # Check the question
        # Note that this is extracting a question and answer list from the list
        # of lists.
        if check_question(questions[index]):
            right = right + 1
        # go to the next question
        index = index + 1
    # notice the order of the computation, first multiply, then divide
    print("You got", right * 100 / len(questions),
          "% right out of", len(questions))

# Begin running program here
option = 0
while option != 9:
    print("--------------------")
    print("1. Take the test")
    print("2. View the questions and answers")
    print("9. Quit")
    option = int(input("Pick an item from the menu: "))
    if option == 1:
        # Run the test
        run_test(questions)
    elif option == 2:
        # Prints a very ugly list.  How would one fix this?
        print(questions)
    else:
        print("You selected an invalid item!")
print("Goodbye")
