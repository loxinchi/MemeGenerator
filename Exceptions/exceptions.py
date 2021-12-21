"""Custom exception classes for different types of exceptions."""


class WrongIngestorError(NotImplementedError):
    """WrongIngestorError file type for ingestor."""

    def __init__(self, *args) -> None:
        """Summary of WrongIngestorError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Return `str(self)`."""
        return f"{self.message}." if self.message else "Using the wrong type of ingestor."


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
            return f"{self.message}." if self.message else "Unsupported quote file Type."


class ImageBrokenError(OSError, ValueError):
    """Image remake failures."""

    def __init__(self, *args) -> None:
        """Summary of ImageBrokenError.

        :param *args: Any values.
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Return `str(self)`."""
        if self.message:
            return f"{self.message}." if self.message else "Image is broke, try another one."
