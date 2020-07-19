## greet
* greet
  - utter_return_greeting
  - utter_explain_functionality

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
    - utter_other_info_desired

## ask skill set
  * ask_skill_set
    - utter_skill_set
    - utter_other_info_desired
    
## ask desired roles
  * ask_desired_roles
    - utter_desired_roles
    - utter_other_info_desired

## * ask contact info + no resume
  * ask_contact_info
    - utter_email
    - utter_github
    - utter_resume_desired
  * deny
    - utter_other_info_desired

## ask contact info + request resume
  * ask_contact_info
    - utter_email
    - utter_github
    - utter_resume_desired
  * affirm
    - utter_ask_email
  * inform{"email":"mediocrecomedy@gmail.com"}
    - action_email_resume
    - utter_other_info_desired
    
## greet + ask functionality + ask work experience + ask contact info
  * greet
    - utter_return_greeting
  * bot_challenge
    - utter_explain_bot
    - utter_explain_functionality
  * ask_work_experience
    - utter_work_experience
    - utter_other_info_desired
  * ask_contact_info
    - utter_email
    - utter_github
    - utter_resume_desired
  * deny
    - utter_other_info_desired
  
## greet + bot challenge + ask work experience + ask skills + ask contact info + email resume
  * greet
     - utter_return_greeting
  * bot_challenge
    - utter_explain_bot
    - utter_explain_functionality
  * ask_work_experience
    - utter_work_experience
    - utter_other_info_desired
  * ask_skill_set
    - utter_skill_set
    - utter_other_info_desired
  * ask_contact_info
    - utter_email
    - utter_github
    - utter_resume_desired
  * affirm
    - utter_ask_email
  * inform{"email":"guido.vanrawesome@gmail.com"}
    - action_email_resume
    - utter_other_info_desired
  * deny
    - utter_goodbye

## bot_challenge + ask skills + ask work experience + ask contact info + email resume
  * bot_challenge
    - utter_explain_bot
    - utter_explain_functionality
  * ask_skill_set
    - utter_skill_set
    - utter_other_info_desired
  * ask_work_experience
    - utter_work_experience
    - utter_other_info_desired
  * ask_contact_info
    - utter_email
    - utter_github
    -utter_resume_desired
  * affirm
    - utter_ask_email
  * inform{"email":"guido.vanrawesome@gmail.com"}
    - action_email_resume
    - utter_other_info_desired
  * goodbye
    - utter_goodbye

## ask about mike + ask contact info + email resume + ask work experience + goodbye 
  * bot_challenge
    - utter_explain_bot
    - utter_explain_functionality
  * ask_contact_info
    - utter_email
    - utter_github
    -utter_resume_desired
  * affirm
    - utter_ask_email
  * inform{"email":"guido.vanrawesome@gmail.com"}
    - action_email_resume
  * ask_work_experience
    - utter_work_experience
    - utter_other_info_desired
  * deny
    - utter_goodbye
    