import os, sys, argparse
from dialogue import Dialogue

functions = {}

### FUNCTIONALITY

def help():
    print """
    ?   help
    p   Print prompt and reply for this node
    ep  Edit Prompt
    er  Edit Reply
    
    o   print Options from this node (prompts only)
        also use this to descend to child nodes
    a   Add an option (child node)
    r   Remove an option (child node)
    
    b   go Back to the previous node

    s   Save the current tree state
    x   eXit (without saving)
    """
functions['?'] = help

def printNode():
    print "PROMPT:"
    print current.prompt
    print "RESPONSE:"
    print current.response
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
    global current
    print "Prompts from here:"
    for i, option in enumerate(current.options):
        print "  {}: {}".format(i, option.prompt)
    print "Descend to option or Cancel?"
    goto = raw_input("number or 'c' > ")
    try:
        last = current
        current = current.options[int(goto)]
        history.append(last)
    except ValueError:
        print "Staying here."
functions['o'] = printOptions

def addOption():
    prompt =   raw_input("prompt   > ")
    response = raw_input("response > ")
    newOption = Dialogue(response, prompt)
    current.options.append(newOption)
    print "Added."
functions['a'] = addOption

def removeOption():
    global current
    print "Prompts from here:"
    for i, option in enumerate(current.options):
        print "  {}: {}".format(i, option.prompt)
    print "Delete option or Cancel?"
    goto = raw_input("number or 'c' > ")
    try:
        current = current.options.pop(int(goto))
    except ValueError:
        print "Did nothing."
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
    with open(args.treename, 'wb') as f:
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

### MAIN LOOP

while True:
    cmd = raw_input("treedit> ")

    if cmd in functions.keys():
        functions[cmd]()
    else:
        print "Not a real command. '?' for help."