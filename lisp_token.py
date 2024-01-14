class Token:
    def __init__(self, value):
        self.value = value


class SymbolToken(
    Token
):
    def __init__(self, value):
        super().__init__(
            value
        )


class NumberToken(
    Token
):
    def __init__(self, value):
        super().__init__(
            value
        )


class ParenToken(
    Token
):
    # For left and right braces
    def __init__(self, value):
        super().__init__(
            value
        )
