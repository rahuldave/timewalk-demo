def greet(
    name: str,  # Who to greet
    excited: bool = False,  # End with an exclamation mark
) -> str:  # The greeting
    "Build a greeting for one person."
    return "Hello, " + name + ("!" if excited else ".")


def shout(
    name: str,  # Who to greet
) -> str:  # The greeting, excited and in capitals
    "Greet one person loudly."
    return greet(name, excited=True).upper()
