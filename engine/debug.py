

class TemplateSyntaxException(Exception):

	def __init__(self, message, template=None, line=None):

		if line is not None:
			message = 'line {} '.format(line) + message

		if template is not None:
			message = '[{}] '.format(template) + message

		super().__init__(message, template)
