from engine.nodes import LiteralNode, BlockNode
from engine.debug import TemplateSyntaxException
from engine.control_nodes import IfNode, ForNode
from engine.special_nodes import IncludeNode, ExecNode, ExprNode


def build_tree(token_list, filename):
    root_node = BlockNode()
    current_node = root_node

    for t in token_list:
        if t.startswith('{%'):
            t = t[2:-2].strip()
            if t.startswith('include '):
                current_node.add_child(IncludeNode(t[8:]))
            elif t.startswith('exec '):
                exec_node = ExecNode(t[5:].strip())
                current_node.add_child(exec_node)
            elif t.startswith('for '):
                if ' in ' not in t:
                    raise TemplateSyntaxException('for loop must include the `in` keyword', filename)
                for_node = ForNode(*(t[4:]).split(' in ', 1))
                current_node.add_child(for_node)
                current_node = for_node
            elif t.startswith('if '):
                if_node = IfNode(t[3:])
                current_node.add_child(if_node)
                current_node = if_node
            elif t.startswith('elif '):
                if not isinstance(current_node, IfNode):
                    raise TemplateSyntaxException('{% elif %} must follow an {% if ... %}', filename)
                current_node.add_elif(t[5:], filename)
            elif t == 'else':
                if not isinstance(current_node, IfNode):
                    raise TemplateSyntaxException('{% else %} must follow an {% if ... %}', filename)
                current_node.add_else(filename)
            elif t == 'end if':
                if not isinstance(current_node, IfNode):
                    raise TemplateSyntaxException('{% end if %} not expected', filename)
                current_node = current_node.parent
            elif t == 'end for':
                if not isinstance(current_node, ForNode):
                    raise TemplateSyntaxException('{% end for %} not expected', filename)
                current_node = current_node.parent
            else:
                raise TemplateSyntaxException('{% ' + t + ' %} is not a valid command', filename)
        elif t.startswith('{{'):
            current_node.add_child(ExprNode(t[2:-2].strip()))
        else:
            current_node.add_child(LiteralNode(t))
    if current_node != root_node:
        raise TemplateSyntaxException('end expected, not found', filename)

    return root_node
