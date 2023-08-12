img = """\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#+*###%%%%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@##%@@@@@@@@#@@@@@@@@@@@@@@
@@@@@@@%%###%%=@@@@@@@@@@**@@@@@@@@@@@@@
@@@@%**#%@@%%#-#@@@**@@@@-%%*#####*#%@@@
@@@**%@%%%@@@#@*+@@+#@@@==**@@@@@@@%**@@
@@@**@@@@%%++==#%=@+#@@=-#%@@@@@@@@@@=*@
@@@@+*%@@@@%#*==+*++*%=#@%#**%@@@@@@=#@@
@@@@@%+-=**#%%%%*====:+@*#@@@@@@@@#*#@@@
@@@@@#*%@@@%##*+**::: .-@@%#*#%@@#*@@@@@
@@#*#@@@@%##%%@@#-:==:-#++*#*==*@@@@@@@@
@@+@@@@@##@@@@%*-*@@@@*#@@@@@@@*+@@@@@@@
@@%+%@@@@@@@%+*+*@@@@@@=#@@@@@@@-@@@@@@@
@@@%*%%##%#@*%@%=@@@@@@@=@@@@@@#%@@@@@@@
@@@@@@@##*%@@@@@++%%%@@@@@@@@#*@@@@@@@@@
@@@@@@@@@@@@@@@@@%###+@%*#@#*#@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@##%%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
"""


def add_border(ascii_art):
    lines = ascii_art.split("\n")
    bordered_art = []
    for line in lines:
        bordered_line = "[[" + line + "]],"
        bordered_art.append(bordered_line)
    return "\n".join(bordered_art)


if __name__ == "__main__":
    print(add_border(img))
