from app import app

class with_request_context(object):
	def __init__(self, f):
		self.f = f
		self.app = app
		self.request = '/'
		self.__name__ = f.__name__ + 'with_request_context'


	def __call__(self, *args):
		with self.app.test_request_context(self.request):
			return self.f(*args)
