# import random
# import time
#
# import speech_recognition as sr
#
#
# def recognize_speech_from_mic(recognizer, microphone):
#     """Transcribe speech from recorded from `microphone`.
#
#     Returns a dictionary with three keys:
#     "success": a boolean indicating whether or not the API request was
#                successful
#     "error":   `None` if no error occured, otherwise a string containing
#                an error message if the API could not be reached or
#                speech was unrecognizable
#     "transcription": `None` if speech could not be transcribed,
#                otherwise a string containing the transcribed text
#     """
#     # check that recognizer and microphone arguments are appropriate type
#     if not isinstance(recognizer, sr.Recognizer):
#         raise TypeError("`recognizer` must be `Recognizer` instance")
#
#     if not isinstance(microphone, sr.Microphone):
#         raise TypeError("`microphone` must be `Microphone` instance")
#
#     # adjust the recognizer sensitivity to ambient noise and record audio
#     # from the microphone
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#
#     # set up the response object
#     response = {
#         "success": True,
#         "error": None,
#         "transcription": None
#     }
#
#     # try recognizing the speech in the recording
#     # if a RequestError or UnknownValueError exception is caught,
#     #     update the response object accordingly
#     try:
#         response["transcription"] = recognizer.recognize_google(audio)
#     except sr.RequestError:
#         # API was unreachable or unresponsive
#         response["success"] = False
#         response["error"] = "API unavailable"
#     except sr.UnknownValueError:
#         # speech was unintelligible
#         response["error"] = "Unable to recognize speech"
#
#     return response
#
#
# if __name__ == "__main__":
#     # set the list of words, maxnumber of guesses, and prompt limit
#     WORDS = ["begin", "clear", "junior", "mango"]
#     NUM_GUESSES = 3
#     PROMPT_LIMIT = 3
#
#     # create recognizer and mic instances
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()
#
#     # get a random word from the list
#     word = begin
#
#     # format the instructions string
#     instructions = (
#         "say begin:\n"
#         "{words}\n"
#     ).format(words=', '.join(WORDS), n=NUM_GUESSES)
#
#     # show instructions and wait 3 seconds before starting the game
#     print(instructions)
#     time.sleep(3)
#
#     for i in range(NUM_GUESSES):
#         # get the guess from the user
#         # if a transcription is returned, break out of the loop and
#         #     continue
#         # if no transcription returned and API request failed, break
#         #     loop and continue
#         # if API request succeeded but no transcription was returned,
#         #     re-prompt the user to say their guess again. Do this up
#         #     to PROMPT_LIMIT times
#         for j in range(PROMPT_LIMIT):
#             print('Guess {}. Speak!'.format(i+1))
#             guess = recognize_speech_from_mic(recognizer, microphone)
#             if guess["transcription"]:
#                 break
#             if not guess["success"]:
#                 break
#             print("I didn't catch that. What did you say?\n")
#
#         # if there was an error, stop the game
#         if guess["error"]:
#             print("ERROR: {}".format(guess["error"]))
#             break
#
#         # show the user the transcription
#         print("You said: {}".format(guess["transcription"]))
#
#         # determine if guess is correct and if any attempts remain
#         guess_is_correct = guess["transcription"].lower() == word.lower()
#         user_has_more_attempts = i < NUM_GUESSES - 1
#
#         # determine if the user has won the game
#         # if not, repeat the loop if user has more attempts
#         # if no attempts left, the user loses the game
#         if guess_is_correct:
#             print("Correct! You win!".format(word))
#             break
#         elif user_has_more_attempts:
#             print("Incorrect. Try again.\n")
#         else:
#             print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
#             break



# import speech_recognition as sr
# print(sr.__version__)
#
# r = sr.Recognizer()
#
# mic = sr.Microphone()
#
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#
# r.recognize_google(audio)
#
#
import random
import time

import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which word.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("umm, what did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(guess["transcription"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            print("yeah! winner winner chicken dinner!".format(word))
            break
        elif user_has_more_attempts:
            print("nope. Try again.\n")
        else:
            print("Sorry loser.\nI was thinking of '{}'.".format(word))
            break

# # import pygame and sys module
# # for exiting the window we create
# import pygame, sys
# from letras import textToScreen
#
# # import some useful constants
# from pygame.locals import *
#
# # initialize pygame and font module
# pygame.init()
#
# # new drawing surface with width: 300 and height: 300
# displaySurface = pygame.display.set_mode((300, 300))
# # a caption for the window
# pygame.display.set_caption("my first game")
#
# # text on screen to be changed
# textToScreen(displaySurface, 'HOLA', 0, 0)
#
# # update display every run through, will slow down framrate if always updating
# # so I placed all drawing before checking for quit
# pygame.display.update()
#
# # will always loop
# while True:
#     # get all user events
#     for event in pygame.event.get():
#         # if quit, then end game and close window
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
