# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("You")

image bg bed = "Hospital Bed.WEBP"
image bg sink = "Sink.jpg"
image bg shower = "Shower.jpg"
image calendar = "Card and letter.jpeg"
image bg fridge = "kitchen.jpg"
image normal bed = "normal bed.jpg"


label start:
show bg bed
"You are lying in your bed, groggy since you have just awoken from a long coma."
"You look over to your left to see a calendar on your bedside table, next to a postcard from your boyfriend from the past."
show calendar
"You read the postcard, which says 'We LOVE you, and missed you so much. Welcome back from your 2 year coma!'"
"You look at the calendar, and see that it is the 29th of August, 2028. You also notice that today is labelled as 'The Perfect Day' on your calendar."
show bg bed
"Panic settles in as you realise that you have no memory of the last 2 years, however you seem to feel familiar in this room and bed, so you decide to explore ."


    # ADD CHOICE FOR KITCHEN OR BATHROOM

    # IF BATHROOM
scene Sink
show bg sink
    # HMM IM HUNGRY, CHECK THE FRIDGE AND THEN ADD THIS CODE
show bg fridge

    # IF KITCHEN
show kitchen
scene kitchen
show kitchen
"You are now in the kitchen, this is where you and your boyfriend used to cook together, you see a note on the fridge that says 'I love you, and I will always be here for you, even if you don't remember me. -Your boyfriend'"
"Memories come flooding back to you, and you recollect your love, feeling a tug at your heart."
"However, your stomach cuts you off before you can think any more, growling greedily"
"You look in the fridge and spot some leftover foods and takeaway"
"Would you like to make a sandwich using the leftover foods or eat the takeaway?"

Would you rather explore the bathroom or the kitchen first?
# If the player chooses the bathroom, the game will continue with the following code:
    scene bathroom
"You are now in the bathroom, you smell the scent of your favourite shampoo and you see your toothbrush"
Would you like to brush your teeth or take a shower?
If the player chooses to brush their teeth, the game will continue with the following code:
"Your brush your teeth and the toothpaste tastes disgusting and rotten, you spit it out and rinse, only to find that the water is brown and dirty. "
e " Ew, this is fucking disgusting, what a good way to start my perfect day"
If the player chooses to take a shower, the game will continue with the following code:
    "You take a shower and feel your greasy hair, so you decide to wash it with shampoo. However you get soap in your right eye, after noticing that the water is brown and dirty ."
e " OW, what the hell my eye hurts, what a good way to start my perfect day



    # WAKE UP

return

# If the player chooses to make a sandwich, the game will continue with the following code:
    "You make a sandwich with the leftover foods, starting by toasting the bread, which you realise to be mouldy."
    "Once the bread is toasted, you try to take it out of the toaster, but it is stuck, so you use a knife ."
    e "Holy shit"
    "The fork burns and gives your hand a slight electric shock, burning your toaster and causing a loud BANG, you scurry out of the kitchen in fear, with an empty stomach"
    e "What a good way to start my perfect day"
    
# If the player chooses to eat the takeaway, the game will continue with the following code:
    "You open the takeaway box, excited to eat, however it looks almost empty, until you spot a couple sad looking dumplings ."
    "You take a bite of the dumpling, only to realise that the inside is completely mouldy and rotten"
    e "Yeuck this is awful, what a good way to start my perfect day"

    return

