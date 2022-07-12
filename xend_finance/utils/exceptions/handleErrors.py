class BaseError(Exception):
    """_summary_: BaseError
    _description_: The base exception for xend_finance sdk
    _usage_:
        raise BaseError(errors)
    _example_:
        raise BaseError({message: "an error occurred"})
    """

    def __init__(self, errors={}):
        self.errors = errors

    def __str__(self):
        return self.errors
