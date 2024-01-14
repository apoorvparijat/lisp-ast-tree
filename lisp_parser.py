import re

from parser_objects import Node, NumberToken, ParenToken, SymbolToken


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
        return self.ast_tree(
            self.tokenise()
        )

    def ast_tree(self, tokens):
        if len(
                tokens
        ) == 0:
            return None
        ast_ = Node(
            tokens[1]
        )
        mid_tokens = tokens[2: -1]
        i = 0
        while i < len(
                mid_tokens
        ):
            token = mid_tokens[i]
            if token.value == "(":
                next_expression, j = self.get_next_expression_tokens(
                    mid_tokens,
                    i
                )
                ast_.children.append(
                    self.ast_tree(
                        next_expression
                    )
                )
                i = j - 1
            else:
                if token.value == "+":
                    ast_.children.append(
                        Node(
                            token
                        )
                    )  # SymbolNode
                elif token.value == ")":
                    pass
                elif token:
                    ast_.children.append(
                        Node(
                            token
                        )
                    )  # NumberNode
                i += 1
        return ast_

    def get_next_expression_tokens(self, tokens, start_index):
        j = start_index
        tokens_to_call = []
        counter = 1
        while (j < len(
                tokens
        )):
            if tokens[j].value == "(":
                counter += 1
            elif tokens[j].value == ")":
                counter -= 1
            if counter == 0:
                break
            tokens_to_call.append(
                tokens[j]
            )
            j += 1
        return tokens_to_call, j

    def as_list(self):
        root_node = self.parse()
        return self.tree_to_list(
            root_node
        )

    def tree_to_list(self, root_node):
        out = []

        if not root_node:
            return out

        current_node = root_node
        out.append(
            current_node.value
        )
        if current_node.children:
            for child_node in current_node.children:
                if len(
                        child_node.children
                ) > 0:
                    out.append(
                        self.tree_to_list(
                            child_node
                        )
                    )
                else:
                    out.append(
                        child_node.value
                    )
        return out
