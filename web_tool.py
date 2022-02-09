from tkinter.ttk import Style
import webbrowser
import validators
import sys
from colorama import Fore, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
init()

y = ["yes", "y", "Y", "YES"]
n = ["no", "n", "N", "NO"]

def main():
    global name
    web = input(f"[{Fore.RED}Website{Style.RESET_ALL}] ")
    url = validators.url(web)

    if url == True:
        print(f"[{Fore.GREEN}Found{Style.RESET_ALL}] {Fore.BLUE}{web}{Style.RESET_ALL}")


        yn = input(f"[{Fore.CYAN}Open{Style.RESET_ALL}] ")
        if yn in y:
            webbrowser.open(web)
            main()

        elif yn in n:
            main()

        else:
            main()

        main()
    
    else:
        print(f"[{Fore.LIGHTBLUE_EX}x{Style.RESET_ALL}] Not found any website called '{web}'")

    main()

main()