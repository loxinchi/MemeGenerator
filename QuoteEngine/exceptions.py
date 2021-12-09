# *Invalid File, Invalid Text Input (e.g. too long)


class UnsupportedFileTypeError(NotImplementedError):
    """Unsupported file type for ingestor."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{self.message}."
        else:
            return "Invalid File Type."


class AuthorNoneTypeError(NotImplementedError):
    """Empty value for mandatory author attribute."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"{self.message}."
        else:
            return "Author is a mandatory field."
