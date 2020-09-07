## happy path 1 (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_gratitude -->


## happy path 2 (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_gratitude -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: mood_great: not good -->
    - utter_cheer_up   <!-- predicted: utter_gratitude -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: mood_great: not good -->
    - utter_cheer_up   <!-- predicted: utter_gratitude -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_ask_again -->


## sad path 3 (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_gratitude -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_ask_again -->


## bot challenge (C:\Users\Lucky\AppData\Local\Temp\tmptiqjafpx\293761b85a4f42b0981545bcd18a7d8c_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: loan_enquiry: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_custid_input -->


