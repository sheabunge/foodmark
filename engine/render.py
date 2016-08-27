from os.path import dirname, join, basename

from engine.tokenizer import tokenize
from engine.tree import build_tree


def compile_template(filename):
    """
    Compile a template into a node tree
    :param filename:
    :return: the root node
    """
    with open(filename) as f:
        source = f.read()

    filename_base = basename(filename)

    tokens = tokenize(source, filename_base)
    return build_tree(tokens, filename_base)


def render(filename, context):
    """
    Render a template with a given context
    :param filename:
    :param context:
    :return:
    """
    path = join(dirname(dirname(__file__)), 'templates', filename)
    root = compile_template(path)
    return root.eval(context)
