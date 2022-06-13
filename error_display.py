from colors import colors

ERROR_MESSAGE_WIDTH = 40

def generateHeader(headerText):
    display = headerText
    whitespace = "⠀" * (ERROR_MESSAGE_WIDTH-len(display))
    return display+whitespace

def displayError(message):
    head = colors.HRED+colors.BOLD+colors.GOLD+generateHeader("ERROR!!!")+colors.NONE
    print(head)
    endStringBefore = -1
    endString = -1
    for c in range(0, len(message), ERROR_MESSAGE_WIDTH-1):
        endStringBefore = endString
        if (c < len(message)-ERROR_MESSAGE_WIDTH):
            endString = message.rfind(" ", 0, c+ERROR_MESSAGE_WIDTH+1)
        else:
            endString = len(message)
        print(message[endStringBefore+1:endString])
    print
