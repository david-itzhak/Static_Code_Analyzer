class ArgumentError(Exception):
    def __str__(self):
        return "Command line argument with directory isn't provided"
