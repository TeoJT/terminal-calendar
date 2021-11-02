class baseColors:

    HEADER    = '\033[95m'
    YELLOW    = '\033[93m'
    LRED      = '\033[91m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    GREEN     = '\033[32m'
    GOLD      = '\033[33m'
    RED       = '\033[31m'
    GREY      = '\033[90m'
    BLACK     = '\033[30m'
    NONE      = '\033[0m'
    WHITE     = '\033[29m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    


    HRED      = '\033[41m'
    HGREEN    = '\033[42m'
    HYELLOW   = '\033[43m'
    HBLUE     = '\033[44m'
    HPURPLE   = '\033[45m'
    HCYAN     = '\033[46m'
    HWHITE    = '\033[47m'


    # def test():
    #     print(self.HEADER + colors.ENDC + "None" + colors.ENDC)
    #     print(colors.HEADER + "Header" + colors.ENDC)
    #     print(colors.BLUE + "Blue" + colors.ENDC)
    #     print(colors.CYAN + "Cyan" + colors.ENDC)
    #     print(colors.GREEN + "Green" + colors.ENDC)
    #     print(colors.YELLOW + "Yellow" + colors.ENDC)
    #     print(colors.RED + "Red" + colors.ENDC)
    #     print(colors.BOLD + "Bold" + colors.ENDC)
    #     print(colors.UNDERLINE + "Underline" + colors.ENDC)
    #     print(colors.BOLD + colors.RED + "Com" + colors.BLUE + "bo")


    def dispAll():
        for i in range(100):
            print('\033[' + str(i) + 'm' + str(i))
    

class colors(baseColors):
    HIGHLIGHT       = baseColors.BLACK+baseColors.HWHITE
    HIGHLIGHT_RED   = baseColors.BLACK+baseColors.RED
    HIGHLIGHT_BLUE  = baseColors.WHITE+baseColors.BLUE
    EVENT_UPCOMING  = baseColors.BLACK+baseColors.HWHITE+baseColors.BOLD
    EVENT_SOON      = baseColors.WHITE+baseColors.HPURPLE+baseColors.BOLD
    EVENT_NOW       = baseColors.WHITE+baseColors.HRED+baseColors.BOLD