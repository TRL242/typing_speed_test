from threading import Thread
from random_word import RandomWords
from tkinter import *
import pprint

# Generate a list of random words
rw = RandomWords()

try:
    rw_list = rw.get_random_words(minCorpusCount=5000, limit=500, maxLength=7)
except:
    rw_list = ['bicycle',
               'sanity',
               'giving',
               'Ambien',
               'blest',
               'began',
               'lighten',
               'ordeal',
               'detach',
               'slowest',
               'elect',
               'shampoo',
               'lasting',
               'jackass',
               'steal',
               'rabble',
               'Jamaica',
               'season',
               'highs',
               'begged',
               'cliff',
               'Ernie',
               'Rector',
               'Caesar',
               'ungodly',
               'torment',
               'shots',
               'rubric',
               'juggle',
               'shakier',
               'custard',
               'buffs',
               'sedate',
               'ruffian',
               'decorum',
               'Saxon',
               'Manual',
               'under',
               'knell',
               'Rivera',
               'matured',
               'Roxanne']
finally:
    print(len(rw_list))
    rw_list_string = ' '.join(rw_list)

# Initialize Fonts & Constants

MINUTE = 60000
HEAD_FONT = ("Helvetica", 36, "bold")
BODY_FONT = ("Helvetica", 15)


# Initialize Functions
def test_typing():
    # MAKE ARRAY OF TYPED WORDS
    word_entry.unbind('<KEY>')
    wpm.after(MINUTE, compare)


def compare():
    entry = word_entry.get("1.0", "end-1c")
    entry_list = entry.split(' ')
    real_wpm = 0
    pprint.pprint(entry_list)
    pprint.pprint(rw_list)
    for n in range(0, (len(entry_list) - 1)):
        if entry_list[n] != None:
            if entry_list[n] == rw_list[n]:
                real_wpm += 1

    wpm.config(text=f'Your WPM is {real_wpm}')


def retry():
    word_entry.delete("1.0", "end-1c")
    try:
        global rw_list
        rw_list = rw.get_random_words(minCorpusCount=5000, limit=500, maxLength=7)
    except:
        pass
    finally:
        global rw_list_string
        rw_list_string = ' '.join(rw_list)
    words_to_copy.config(text=rw_list_string)
    word_entry.bind('<KEY>', Thread(target=test_typing).start())


# Create TKinter window
window = Tk()
window.title('TYPY TEST!')
window.minsize(width=1000, height=700)
window.config(padx=100, pady=50)

# Style the TKinter Window
intro = Label(text='Type the following words as fast as you can in the box below!', font=HEAD_FONT)
intro.pack()
words_to_copy = Label(text=rw_list_string, font=BODY_FONT, wraplength=900)
words_to_copy.pack(pady=10)

wpm = Label(text='Start Typing to Calculate WPM', font=HEAD_FONT, fg='green')
wpm.pack()

# Create Entry Box

word_entry = Text(width=100, height=20, bg="light yellow")
word_entry.pack(pady=10)
word_entry.bind('<KEY>', Thread(target=test_typing).start())

# Retry Button
retry = Button(text="Click to Retry", command=retry)
retry.pack()

# END LOOP
window.mainloop()