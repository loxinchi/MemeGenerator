"""Custom exception classes for different types of exceptions."""


class WrongIngestorError(NotImplementedError):
    """Unsupported file type for ingestor."""

    def __init__(self, *args) -> None:
        """Summary of UnsupportedFileTypeError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Return `str(self)`."""
        return f"{self.message}." if self.message else "Invalid File Type."


class AuthorNoneTypeError(NotImplementedError):
    """Empty value for mandatory author attribute."""

    def __init__(self, *args) -> None:
        """Summary of AuthorNoneTypeError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Return `str(self)`."""
        return f"{self.message}." if self.message else "Author is a mandatory field."


class UnsupportedFileTypeError(NotImplementedError):
    """Empty value for mandatory author attribute."""

    def __init__(self, *args) -> None:
        """Summary of UnsupportedFileTypeError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Return `str(self)`."""
        if self.message:
            return f"{self.message}." if self.message else "Author is a mandatory field."
