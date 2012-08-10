from annoying.decorators import render_to, ajax_request

@render_to("base.html")
def home(request):
	return {}