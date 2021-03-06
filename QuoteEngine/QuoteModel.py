"""Represent models for QuoteModel objects and their close approaches.

The `QuoteModel` class represents a quote object. Each has a quote and an author name.
"""


class QuoteModel:
    """A `QuoteModel` object contains quote and Author.

    `QuoteModel` object capsules semantic and physical parameters about the object,
    such as its quote body (required), author name (required).
    """

    def __init__(self, body, author) -> None:
        """Create a new `QuoteModel`.

        :param body: a quote.
        :param author: author name of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"<quote:{self.body}, author:{self.author}>"
