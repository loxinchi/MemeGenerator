"""Custom exception classes for different types of exceptions."""


class UnsupportedFileTypeError(NotImplementedError):
    """Unsupported file type for ingestor."""

    def __init__(self, *args):
        """Summary of UnsupportedFileTypeError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """Return `str(self)`."""
        if self.message:
            return f"{self.message}."
        else:
            return "Invalid File Type."


class AuthorNoneTypeError(NotImplementedError):
    """Empty value for mandatory author attribute."""

    def __init__(self, *args):
        """Summary of AuthorNoneTypeError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """Return `str(self)`."""
        if self.message:
            return f"{self.message}."
        else:
            return "Author is a mandatory field."
