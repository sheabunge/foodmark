from engine.nodes import BlockNode
from engine.debug import TemplateSyntaxException


class ForNode(BlockNode):
	def __init__(self, var, constraint):
		super().__init__()
		self.constraint = constraint
		self.var = var

	def eval(self, context):
		results = []

		for i in eval(self.constraint, {}, context):
			context[self.var] = i
			results += [child.eval(context) for child in self.children]

		return ''.join(results)

	def __str__(self):
		return 'ForNode({} in {})'.format(self.var, self.constraint)


class IfNode(BlockNode):
	def __init__(self, condition):
		super().__init__()
		self.conditions = [condition]
		self.children = [[]]
		self.has_else = False

	def add_elif(self, condition, filename):
		if self.has_else:
			raise TemplateSyntaxException('{% elif ... %} should not be placed after {% else %}', filename)
		self.conditions.append(condition)
		self.children.append([])

	def add_else(self, filename):
		if self.has_else:
			raise TemplateSyntaxException('{% else %} should not be placed after another {% else %}', filename)
		self.add_elif('True', filename)
		self.has_else = True

	def add_child(self, child):
		self.children[-1].append(child)
		child.parent = self

	def eval(self, context):
		for children, condition in zip(self.children, self.conditions):
			if not eval(condition, {}, context):
				return ''

			return ''.join(child.eval(context) for child in children)

	def __str__(self):
		return 'IfNode({})'.format(self.conditions[0])

	def __repr__(self):
		words = []
		first = True
		for children, condition in zip(self.children, self.conditions):
			if first:
				first = False
				words.append(str(self))
			else:
				words.append('ElifNode({})'.format(condition))
			for child in children:
				parts = repr(child).split('\n')
				words += ['  ' + part for part in parts]
		return '\n'.join(words)
