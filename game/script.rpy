# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("You")


# The game starts here.

label start:
    scene bedroom
"You are lying in your bed, groggy since you have just awoken from a long coma."
"You look over to your left to see a calendar on your bedside table, next to a postcard from your boyfriend from the past."
"You read the postcard, which says 'We LOVE you, and missed you so much. Welcome back from your 2 year coma!'"
"You look at the calendar, and see that it is the 29th of August, 2028. You also notice that today is labelled as 'The Perfect Day' on your calendar."
"Panic settles in as you realise that you have no memory of the last 2 years, however you seem to feel familiar in this room and bed, so you decide to explore ."

Would you rather explore the bathroom or the kitchen first?
If the player chooses the bathroom, the game will continue with the following code:
    scene bathroom
"You are now in the bathroom, you smell the scent of your favourite shampoo and you see your toothbrush"
Would you like to brush your teeth or take a shower?
If the player chooses to brush their teeth, the game will continue with the following code:
"Your brush your teeth and the toothpaste tastes disgusting and rotten, you spit it out and rinse, only to find that the water is brown and dirty. "
e " Ew, this is fucking disgusting, what a good way to start my perfect day"
If the player chooses to take a shower, the game will continue with the following code:
    "You take a shower and feel your greasy hair, so you decide to wash it with shampoo. However you get soap in your right eye, after noticing that the water is brown and dirty ."
e " OW, what the hell my eye hurts, what a good way to start my perfect day"

If the player chooses the kitchen, the game will continue with the following code:
    scene kitchen
"You are now in the kitchen, this is where you and your boyfriend used to cook together, you see a note on the fridge that says 'I love you, and I will always be here for you, even if you don't remember me. -Your boyfriend'"
"Memories come flooding back to you, and you recollect your love, feeling a tug at your heart."
"However, your stomach cuts you off before you can think any more, growling greedily"
"You look in the fridge and spot some leftover foods and takeaway"
Would you like to make a sandwich using the leftover foods or eat the takeaway?
If the player chooses to make a sandwich, the game will continue with the following code:
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
