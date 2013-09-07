import os, sys, argparse
from dialogue import Dialogue
from colorama import Fore, Back, Style, init
init()
functions = {}

### DISPLAY UTILS
def setColorPrompt():
    sys.stdout.write(Fore.CYAN)

def setColorOutput():
    sys.stdout.write(Back.BLUE)

def setColorReset():
    sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)

def printOutput(text):
    setColorOutput()
    print text
    setColorReset()

### FUNCTIONALITY

def help():
    print """
    ?     help
    p     Print prompt and reply for this node
    ep    Edit Prompt
    er    Edit Reply
    
    o     print Options from this node (prompts only)
    a     Add an option
    d n   Descend to option #n
    r n   Remove option #n
    
    b     go Back to the previous node

    s     Save the current tree state
    x     eXit (without saving)
    """
functions['?'] = help

def printNode():
    print "PROMPT:"
    printOutput(current.prompt)
    print "RESPONSE:"
    printOutput(current.response)
functions['p'] = printNode

def editPrompt():
    print "PROMPT:"
    print current.prompt
    current.prompt = raw_input("New Prompt > ")
    print "Edited."
functions['ep'] = editPrompt

def editResponse():
    print "RESPONSE:"
    print current.response
    current.response = raw_input("New Response > ")
    print "Edited."
functions['er'] = editResponse

def printOptions():
    print "Prompts from here:"
    for i, option in enumerate(current.options):
        printOutput("  {}: {}".format(i, option.prompt))
functions['o'] = printOptions

def addOption():
    prompt =   raw_input("prompt   > ")
    response = raw_input("response > ")
    newOption = Dialogue(response, prompt)
    current.options.append(newOption)
    print "Added."
functions['a'] = addOption

def descend(optiondex):
    global current
    try:
        last = current
        current = current.options[int(optiondex)]
        history.append(last)
    except ValueError:
        print "Descend failed (bad node number?)"
functions['d'] = descend

def removeOption(optiondex):
    try:
        current.options.pop(int(optiondex))
    except ValueError:
        print "Remove failed (bad node number?)"
functions['r'] = removeOption

def goBack():
    global current
    try:
        current = history.pop()
        print "Went back."
    except IndexError:
        print "Already at root."
functions['b'] = goBack

def saveTree():
    with open(filename, 'wb') as f:
        root.save(f)
    print "Saved."
functions['s'] = saveTree

def exitTreedit():
    sys.exit(0)
functions['x'] = exitTreedit

### ARGUMENT PARSING AND SETUP

parser = argparse.ArgumentParser(description="Editor for 72 dialog trees")
parser.add_argument('treename', type=str, help="Name of tree to edit or create")
parser.add_argument('-c', action='store_true', help="Create a new tree")

args = parser.parse_args()

if args.c == True:
    if os.path.exists(args.treename):
        print "Err: dialog tree to be created already exists!"
        sys.exit(1)
    else:
        initresponse = raw_input("initial response > ")
        root = Dialogue(initresponse)
else:
    try:
        with open(args.treename, 'rb') as f:
            root = Dialogue.load(f)
    except IOError:
        print "Err: dialog tree could not be loaded. Perhaps create it?"
        sys.exit(2)

# Root must now exist, whether we just created it or loaded it in
# We now start up the main loop
print "TREEDIT - '?' for help, 'x' to exit"

# set up the history thing
history = []
current = root
filename = args.treename

### MAIN LOOP

while True:
    setColorPrompt()
    cmd = raw_input("treedit> ").split(" ")
    setColorReset()
    args = cmd[1:]

    try:
        functions[cmd[0]](*args)
    except TypeError:
        print "Bad command usage. '?' for help."
    except KeyError:
        print "Not a command. '?' for help."