
class Node(object):
    def __init__(self):
        self.parent = None
        self.children = []

    def eval(self, context):
        raise NotImplementedError()

    def __str__(self):
        return 'GenericNode()'

    def __repr__(self):
        words = [str(self)]

        for child in self.children:
            parts = repr(child).split('\n')
            words += ['  ' + part for part in parts]

        return '\n'.join(words)


class LiteralNode(Node):
    def __init__(self, token):
        super().__init__()
        self.token = token

    def eval(self, context):
        return self.token

    def __str__(self):
        return 'LiteralNode({})'.format(repr(self.token[:30]))


class BlockNode(Node):
    def eval(self, context):
        return ''.join(child.eval(context) for child in self.children)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __str__(self):
        return 'BlockNode()'

