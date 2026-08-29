# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("You")
define d = Character("David")

image bg bed = "Hospital Bed.WEBP"
image bg sink = "Sink.jpg"
image bg shower = "Shower.jpg"
image calendar = "Card and letter.jpeg"
image bg fridge = "kitchen.jpg"
image normal bed = "normal bed.jpg"
image garden = "garden.jpg.webp"
image toaster = "toaster.jpg.webp"


label start:
scene hospital
show bg bed
"You are lying in your bed, groggy since you have just awoken from a long coma."
"You look over to your left to see a calendar on your bedside table, next to a postcard from your boyfriend from the past."
scene calendar

show calendar
"You read the postcard, which says 'We LOVE you, and missed you so much. Welcome back from your 2 year coma!'"
"You look at the calendar, and see that it is the 29th of August, 2028. You also notice that today is labelled as 'The Perfect Day' on your calendar."

scene hospital
show bg bed
"Panic settles in as you realise that you have no memory of the last 2 years, however you seem to feel familiar in this room and bed, so you decide to explore ."


    # ADD CHOICE FOR KITCHEN OR BATHROOM

    # IF BATHROOM
scene Sink
show bg sink
    # HMM IM HUNGRY, CHECK THE FRIDGE AND THEN ADD THIS CODE
scene fridge
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

#Would you rather explore the bathroom or the kitchen first?
# If the player chooses the bathroom, the game will continue with the following code:
scene bathroom
show bg sink
"You are now in the bathroom, you smell the scent of your favourite shampoo and you see your toothbrush"
#Would you like to brush your teeth or take a shower?
#If the player chooses to brush their teeth, the game will continue with the following code:
"Your brush your teeth and the toothpaste tastes disgusting and rotten, you spit it out and rinse, only to find that the water is brown and dirty. "
e " Ew, this is fucking disgusting, what a good way to start my perfect day"
#If the player chooses to take a shower, the game will continue with the following code:
scene shower
show bg shower
"You take a shower and feel your greasy hair, so you decide to wash it with shampoo. However you get soap in your right eye, after noticing that the water is brown and dirty ."
e " OW, what the hell my eye hurts, what a good way to start my perfect day"



# If the player chooses to make a sandwich, the game will continue with the following code:
scene toaste
show toaster
"You make a sandwich with the leftover foods, starting by toasting the bread, which you realise to be mouldy."
"Once the bread is toasted, you try to take it out of the toaster, but it is stuck, so you use a knife ."
e "Holy shit"
"The fork burns and gives your hand a slight electric shock, burning your toaster and causing a loud BANG, you scurry out of the kitchen in fear, with an empty stomach"
e "What a good way to start my perfect day"
    
# If the player chooses to eat the takeaway, the game will continue with the following code:
scene takeaway
show bg fridge
"You open the takeaway box, excited to eat, however it looks almost empty, until you spot a couple sad looking dumplings ."
"You take a bite of the dumpling, only to realise that the inside is completely mouldy and rotten"
e "Yeuck this is awful, what a good way to start my perfect day"

scene bed
show normal bed
"You fall back into reality, realising everything has been a dream, thank goodness."
"You decide to get out of bed and experience the day, forgetting all about that perfect day nonsense."
 
scene garden 
show garden 
"You go outside to the garden, and see your boyfriend waiting for you, smiling and waving at you."
e "Hello David! You wouldn't believe the funny dream I just had!"
d "Hello darling, you can tell me all about it later, at a special somwehere."
d "I love you so much, and always will. Will you marry me and make me the happiest man alive?" 
e "NO, I would much rather marry your brother."
e "Just kidding, of course I will marry you, I love you so much David. I am the happiest woman alive."
e "Turns out, the perfect day was real after all!"


return