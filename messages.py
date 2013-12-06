ENTER = """

<Press Enter to continue>"""

def print_messages(*messages):
  """Print a bunch of messages."""
  for m in messages:
    raw_input(m + ENTER)


WELCOME = '''
*******************************************************************************
><><><><><><><><><><><><><><><>PICKETT<><><><><><><><><><><><><><><><><><><><><
*******************************************************************************
*****************************By Ray Weiss**************************************
*******************************************************************************
**************************Press Enter To Start*********************************
*******************************************************************************
              '''

LAST_NAME = '\nWhat is your last name boy? :> '

EXPLANATION = '''
You are a young boy of the age of 10.
Your parents are going to Europe for the summer.
They aren't taking you.
You are informed you are being sent to a summer camp for 3 weeks.

~Mountian Head Camp~

'''

BUS_LOADING = '''
You are taken to the park where the bus is loading up kids.
Your parents shove you onto the bus.
You take a seat on the bus, several kids are talking amongst themselves.

You start playing your portable Game Kid.
A boy walks up to you looking angry.
Hey you, give me that Game Kid. Now.'''

CRACK = 'CRACK!'

GAME_KID_LOST = '''You lost your Game Kid.
You erase the memory from your mind.'''

WEEK_ONE = {
  1: [
    'Week One: Day One',

    '''
You Arrive to Mountian Head Camp.

The bus stops, a guy that must be a counselor gets on the bus.

Troid:
    'Alright kids, we're here, get off the bus and go to your bunks, no roughhousing!
    At least not on this bus, anything goes when you get off of this bus, just please,
    get off the bus.''',

    '''
You get off the bus and find your bunk mates.

There are 10 other boys in your bunk.

There seem to be 10 other girls in your age group.

You are shuffled up to the Theater for Orientation.''',

    '''
The theater darkens, the two camp directors, Barry & Sherry Fandling approach the stage.

They are wearing Ulthra Weissman T-Shirts, a popular singer amongst older people.

Barry Fandling:
    'I want to welcome everyone to Mountian Head camp this year! Is everyone excited
    for this summer?

The theater erupts in cheers, Barry puts his arm around Sherry.

Sherry Fandling:
    This is our fifth year since we've bought the camp, and with your help, this is going
    to be the best summer yet! We've built new and improved facilities this year and
    everything is "ordained" to perfection!

Barry Fandling:
    Alright we would now like everyone to join us in our camp alma-mater. If you don't
    know the words, follow along with the programs under the benches.''',

    '''
Mountain Head Alma-Mater:

    ~Oh Hello Vast And Wondrous Universe~

    ~Oh How Does The Vast Void Reveal Itself~

    ~When The Light Reverses It's Once Sacred Purpose~

    ~Then We Will All Know True Power & Discipline~''',

    '''
The lights turn back on.

Barry Fandling:
    And with that we would like to welcome you to what we hope will be the best summer of
    your life! We hope you treat your fellow campers and staff with the same love and care
    we put into the camp and the surrounding grounds.

Sherry Fandling:
    Don't be silly sweetie, everyone just go have fun! Yay!''',


    ],
  }

LEAVING_THEATER = '''

You leave the theater and see:
'''

REQUEST_A_NUMBER = '''
Please choose a number. :>
'''

BAD_NUMBER_MESSAGE = 'Your answer must be between 1 and %d'
