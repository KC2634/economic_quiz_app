# Economic Quiz App

##Introduction

I work at UK Greetings, we supply greetings cards to retailers across the UK. I work in the Consumer Insight department where we look at how economic factors correlate to the greetings card market. Knowledge on what is happening in the UK economy is imperative for our team. There are lots of economic jargon used, this can be tricky to remember what each economic indicator measures. Therefore, I decided to develop an Economic Quiz app to test my team on economic measures.

Economic quiz app is a desktop application built using python and tkinter. The app asks the user for their name and deploys 3 questions with multiple choice answers where the user can choose the answer. It is not intended to be a teaching tool; rather a short quiz created to see what the user already knows and is only 3 questions long as our department is very fast paced so anything longer would not be useful.

Before submission, if any questions are not answered the app displays an error message. This is a key component for my app because some of my team are less technical, having this error message ensures they know all questions have been answered so they don’t have to retake the quiz. The user’s name is cleaned and checked against 4 validation functions, if any of the validations are not met another error message is displayed before the user can proceed. This ensures the data stored is clear and easy to read, which is important when creating visualisations. When all questions are answered and the name is valid, the name, date, time, score and selected answers are written to a CSV file. This storage format is used across the business and is easily accessible. 

My app focuses on the input collection, validation and storage, features such as data visualisation have not taken place at this stage. 

## Design
### GUI

Figure 1 shows the Figma wireframe used at the beginning of the design stage of my quiz. It demonstrates the intended user journey throughout the quiz. Starting at entering the user’s name and answers, to an error message being displayed. Then submitting their valid name and all answers. Then displaying the Thank you screen where their score is present, the user can press the quit button.

This Figma was used to display the screen layout, input validation and flow before implementation. It does not represent the final interface of the app; I adjusted based on the screen layout present with a laptop.

![Figure 1: Wireframe demonstrating the intended user journey](Figma.png)
**Figure 1:** Wireframe

### Persona File

I created a persona file (Figure 2) to document an intended user, this allowed me to think further about the needs of the user. For example, I ensured my app was able to be displayed on a laptop screen as I know my intended user uses a laptop. This adheres to the user and business needs.

![Figure 2:Persona Profile of intended user](Persona_Profile.png)
![Figure 2:Persona Profile of intended user](Persona_Profile_Interests.png)
**Figure 2:** Persona File

### Functional and Non-functional Requirements
#### Functional Requirements


