def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message,color))

def format_command(command):
    return command.replace("\n","").replace("\r","")

def ping():
    print_colored("PRINT Command", "green")
