## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_explain_functionality
  
## explain_functionality
  * ask_capabilities
    - utter_explain_functionality

## ask weather
  * ask_weather
    - utter_ask_location
  * inform{"location": "San Francisco"}
    - action_get_weather
  * goodbye
    - utter_goodbye
    
## greet + goodbye
  * greet
    - utter_return_greeting
    - utter_explain_bot
    - utter_explain_functionality
  * goodbye
    - utter_goodbye
    
## bot challenge
  * bot_challenge
     - utter_explain_bot
     - utter_explain_functionality 

## ask about mike
  * ask_about_mike
     - utter_respond_about_mike
     - utter_explain_functionality

## ask work experience
  * ask_work_experience
    - utter_work_experience

## ask skill set
  * ask_skill_set
    - utter_skill_set
    
## ask desired roles
  * ask_desired_roles
    - utter_desired_roles

## * ask contact info + no resume
  * ask_contact_info
    - utter_email
    - utter_github
    - utter_resume_desired
  * inform