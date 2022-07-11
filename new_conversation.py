# functions

def respond_to_user_name(user):
    if(user == "bill"):
        print("sup homie :)")
    elif(user == "scott"):
        print("not you again")
    elif(user == "mike"):
        print("the master returns! praise jebus!")
    elif(user == "gary"):
        print("welcome to the man with the incredible beard")
    else:
        print("idk who the fuck you are")
        exit()

def get_user_name():
    user = input("What's your name?\n")

    respond_to_user_name(user)

    return user

def ask_question_number_1():
    response1 = input("how are you doing today?\n")

    respond_to_question_one(response1)

    return response1

def respond_to_question_one(response1):
    if(response1 == "good"):
        print("well good for you!")
    elif(response1 == "great"):
        print("calm down there skipper, no need to brag")
    elif(response1 == "fine"):
        print("as to be expected")
    elif(response1 == "okay"):
        print("isnt that how we all feel?")
    elif(response1 == "bad"):
        print("well no one really cares to hear why")
    else:
        print("Is that some kind of liberal emotion im too american to understand?")
        exit()

def ask_question_number_2():
    response2 = input("would you like to be a pepper too? yes/no\n")

    respond_to_question_two(response2)

    return response2

def respond_to_question_two(response2):
    if(response2 == "yes"):
        print("sadly you cannont be a pepper. but you may embrace the pepper. all hail dr pepper!")
    elif(response2 == "no"):
        print("you will be exterminated like the rest!")
    elif(response2 == "number 5"):
        print("no disassemble! O~O")
    else:
        print("so you have chosen... death.")
        exit()

def ask_question_number_3():
    response3 = input("what is the airspeed velocity of an unladen swallow?\n")

    respond_to_number_3(response3)

    return response3

def respond_to_number_3(response3):
    if(response3 == "11 meters per second"):
        print("Correct!")
    elif(response3 == "11mps"):
        print("Correct!")
    elif(response3 == "11"):
        print("you should probably mention its in meters per second but close enough")
    else:
        print("unfortunately you are flung into a valley to your inevitable death. sorry...")

def ask_final_question():
    final_response = input("is this program satisfactory?\n")

    respond_to_final_question(final_response)

    return final_response

def respond_to_final_question(final_response):
    if(final_response == "yes"):
        print("yay. i tried my best :D")
    elif(final_response == "no"):
        print("im sorry i thought this was america!")
    elif(final_response == "kinda"):
        print("thats fair, i guess")
    elif(final_response == "so far"):
        print("yeah we might have more to come in here. who knows really.")
    else:
        print("wow, okay. be that way")

# program start!!!

username = get_user_name()
question1 = ask_question_number_1()
question2 = ask_question_number_2()
question3 = ask_question_number_3()
final_question = ask_final_question()
exit()









#if 0 < x < 10:
    #print("x is a positive single digit number")


    #user = input("what is your name, hoe?\n")
