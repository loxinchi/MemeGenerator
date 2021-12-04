class UnsupportedFileTypeError(NotImplementedError):
    """Unsupported file type for ingestor."""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}.'
        else:
            return 'UnsupportedFileTypeError has been raised'
