# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define college_friend  = Character("Friend")
default role = "dev"

# The game starts here.

label start:
    play music "music/adventurous/Dirac.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg uni

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    with dissolve

    # These display lines of dialogue.

    python:
        youname = renpy.input("What is your name?")
        youname = youname.strip()

        if not youname:
            youname = "eileen"

    you "Hi, My name is [youname]. I am in the final semester and looking to get a job, Luckily there is going to be a campus placement really soon."


    play music "music/tense/Franklin.mp3"
    scene bg lecturehall
    show sylvie green normal
    college_friend "Hey [youname]!"

    show sylvie green normal at left
    college_friend "Why were you not in the party last night?"

    you "Dude, I was prepareing for placements."

    show sylvie green surprised at right
    college_friend "Oh man!!! I totally forgot about that."

    you "Dude, You really need to be preared. It's not going to be easy."

    college_friend "I am still confused about what role I should apply for."

    college_friend "Have you decided?"

    menu:

        "I really love coding.":
            jump coding

        "I love to break my friend's code.":
            jump tester

label coding:

    you "I really love coding."
    you "I am appling for dev roles."
    $ role = 'dev'

    jump interview

label tester:

    you "I love to break my friend's code."
    you "I am appling for QA roles."
    $ role = 'tester'

    jump interview

define interviewer = Character("Interviewer")

label interview:
    play music "music/investigative/Esam.mp3"
    scene bg whitehouse
    show eileen happy at right

    interviewer "I am [interviewer], I work as team lead at Unicorn Inc."

    you "Hi [interviewer], I am [youname], I am looking for a [role] role."

    interviewer "Sounds good, So what should we start with today?"

    menu:
        "I really like algos.":
            jump dev_interview

        "I really like puzzles.":
            jump qa_interview



# Green represents - A person thinking

label dev_interview:

    if role == 'dev':

        interviewer 'Given a 2d grid map of \'1\'s (land) and \'0\'s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'

        you 'Thinking...'

        you '...I know this...' (what_color="#8c8")

        you '...This is a DFS problem...' (what_color="#8c8")

        you '......' (what_color="#8c8")

        you '...Let me write a simple dfs approach...' (what_color="#8c8")

        you '......' (what_color="#8c8")

        you '...Let me recheck this code...' (what_color="#8c8")

        you '...Looks good to me...' (what_color="#8c8")

        you 'Here is how we solve this '

        jump selected

    else:

        interviewer 'Given a number n, find sum of first n natural numbers. To calculate the sum, we will use a recursive function recur_sum().'

        you 'Thinking...'

        you '...Do we need to use recursion?...' (what_color="#8c8")

        you '...I might be able to do it without recursion...' (what_color="#8c8")

        interviewer 'You need to use recursion!'

        you '...Let me write some code...' (what_color="#8c8")

        you '......' (what_color="#8c8")

        you '...For some reason my code is running forever...' (what_color="#8c8")

        you '...I don\'t think I can solve this...'

        jump rejected


label qa_interview:
        if role == 'tester':

            interviewer 'There are 1000 wine bottles. One of the bottles contains poisoned wine. A rat dies after one hour of drinking the poisoned wine. How many minimum rats are needed to figure out which bottle contains poison in hour.'

            you 'Thinking...'

            you '...I know this...' (what_color="#8c8")

            you '...This is a binary representation problem...' (what_color="#8c8")

            you '......' (what_color="#8c8")

            you '...Let me tell you how we can use 10 rats to solve this problem...' (what_color="#8c8")

            you '......' (what_color="#8c8")

            you '...Here is the solution...'

            jump selected

        else:

            interviewer 'You have two ropes coated in an oil to help them burn. Each rope will take exactly 1 hour to burn all the way through. However, the ropes do not burn at constant rates—there are spots where they burn a little faster and spots where they burn a little slower, but it always takes 1 hour to finish the job.'

            interviewer 'With a lighter to ignite the ropes, how can you measure exactly 45 minutes?'

            you 'Thinking...' 

            you '...Why don\'t we just use the datetime library to measure 45 minutes...' (what_color="#8c8")

            you '...Who uses candles, I always use my mobile...' (what_color="#8c8")

            you '...I don\'t think I can solve this...'

            jump rejected


label rejected:

    play music "music/sad/Dairen.mp3"

    interviewer "I don't think you are prepared for this"

    "I suggest you try again in 6 months."

    "Life is going to be hard now!!!..."

    # This ends the game.

    return

label selected:

    play music "music/joyful/Asturias.mp3"
    interviewer "I think you are well prepared."

    interviewer "We can pay you 70k and you start next week. Good luck."

    "Life is set!!!..."

    # This ends the game.

    return
