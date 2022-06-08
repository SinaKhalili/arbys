from threading import Thread
from time import sleep
import readline

readline.parse_and_bind("tab: complete")


def check_for_arb(amount: int, logs):
    """
    Check for arb amount
    """
    sleep(amount)
    logs["btc"].append("SOMETHING HERE")


def get_input(logs):
    """
    This is the prompt
    """
    inp = ""

    while inp != "exit":
        inp = input("> ")
        if inp == "help":
            print("-----BOOMberg Terminal-----")
            print("Commmands:")
            print("\t", "help: ", "Print this message and exit")
            print("\t", "monitor: ", "Monitor the logs")
            print("\t", "exit: ", "Leave")

        if inp == "monitor":
            print("\n".join(logs["btc"]))

    print("Moritorus Te Saluto")


if __name__ == "__main__":
    logs = {"btc": []}
    arb_checker = Thread(target=check_for_arb, args=(2, logs))
    arb_checker.start()
    get_input(logs)

    arb_checker.join()
    print("bye")
