from engine.debug import TemplateSyntaxException

TOKEN_LITERAL = 0
TOKEN_EXPR = 1
TOKEN_ACTION = 2
TOKEN_COMMENT = 3


# Convert source code to list of tokens
def tokenize(source, filename):
    tokens = []
    token_start = 0
    token_end = 0
    cur = 0
    line = 1
    mode = TOKEN_LITERAL
    prev_char = ' '
    while True:
        char = source[cur]

        # Increment line counter every line
        if char == '\n':
            line += 1

        # Handle token split on {{ or {% or {#
        if prev_char == '{' and mode == TOKEN_LITERAL and (char == '{' or char == '%' or char == '#'):
            token_end = cur - 1  # Set end of token
            tokens.append(source[token_start:token_end])  # Add previous token
            token_start = cur - 1  # Set start of new token
            # Set to either expr or action mode
            mode = TOKEN_COMMENT if char == '#' else (TOKEN_EXPR if char == '{' else TOKEN_ACTION)

        # Handle token split on }} or %} or #}
        if char == '}' and (prev_char == '}' or prev_char == '%' or prev_char == '#'):
            # Make sure expr token is properly closed by %}
            if mode == TOKEN_EXPR and prev_char != '}':
                raise TemplateSyntaxException('expected }} got ' + prev_char + '}', filename, line)

            # Make sure action token is properly closed by }}
            if mode == TOKEN_ACTION and prev_char != '%':
                raise TemplateSyntaxException('expected %} got ' + prev_char + '}', filename, line)

            # Make sure comment token is properly closed by #}
            if mode == TOKEN_COMMENT and prev_char != '#':
                raise TemplateSyntaxException('expected #} got ' + prev_char + '}', filename, line)

            if mode == TOKEN_LITERAL:
                raise TemplateSyntaxException('unexpected ' + prev_char + '}', filename, line)

            token_end = cur + 1  # Set end of token
            if mode != TOKEN_COMMENT:
                tokens.append(source[token_start:token_end])  # Add previous token
            token_start = cur + 1  # Set start of new token
            mode = TOKEN_LITERAL

        prev_char = char  # Update previous char
        cur += 1  # Increment cursor
        if cur == len(source):
            token_end = cur  # Set end of token
            if mode != TOKEN_LITERAL:
                raise TemplateSyntaxException('unclosed tag', filename)
            tokens.append(source[token_start:token_end])  # Add previous token
            break
    return tokens

