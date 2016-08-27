from engine.nodes import Node
from html import escape


class IncludeNode(Node):

    def __init__(self, reference):
        super().__init__()
        self.reference = reference

    def eval(self, context):
        from engine.render import render
        read_file = render(self.reference, context)
        return read_file

    def __str__(self):
        return 'IncludeNode({})'.format(self.reference)


class ExprNode(Node):

    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def eval(self, context):
        return escape(str(eval(self.expression, {}, context)))

    def __str__(self):
        return 'ExprNode({})'.format(self.expression)


class ExecNode(Node):
    def __init__(self, statement):
        super().__init__()
        self.statement = statement

    def eval(self, context):
        exec(self.statement, {}, context)
        return ''

    def __str__(self):
        return 'ExecNode({})'.format(self.statement)
