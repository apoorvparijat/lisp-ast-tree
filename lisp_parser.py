import re

from lisp_token import NumberToken, ParenToken, SymbolToken


class LispParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def tokenise(self) -> list:
        # Return array of tokens
        tokenised = []
        string_len = len(
            self.input_string
        )
        i = 0

        while i < string_len:
            char = self.input_string[i]
            if char == "(":
                # paren node
                i += 1
                tokenised.append(
                    ParenToken(
                        "("
                    )
                )
            elif char == ")":
                # paren node
                i += 1
                tokenised.append(
                    ParenToken(
                        ")"
                    )
                )
            elif char == " ":
                # whitespace ignore
                i += 1
                pass
            elif char == "+":
                # symbol node
                i += 1
                tokenised.append(
                    SymbolToken(
                        "+"
                    )
                )
            elif char.isdigit():
                # number node
                regex = re.compile(
                    r"([0-9]+)(.*)"
                )
                match = regex.match(
                    self.input_string[i:]
                )
                if match:
                    i += len(
                        match.group(
                            1
                        )
                    )
                    tokenised.append(
                        NumberToken(
                            int(
                                match.group(
                                    1
                                )
                            )
                        )
                    )
            else:
                # remaining symbol token
                regex = re.compile(
                    r"([a-zA-Z]+)(.*)"
                )
                match = regex.match(
                    self.input_string[i:]
                )
                if match:
                    i += len(
                        match.group(
                            1
                        )
                    )
                    tokenised.append(
                        SymbolToken(
                            match.group(
                                1
                            )
                        )
                    )
        return tokenised

    def parse(self):
        # Return root node of AST tree
        return []

    def tree_as_list(self):
        # Return list representation of AST tree
        return []