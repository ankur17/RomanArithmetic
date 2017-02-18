from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from view.evaluate import evaluat




def basic(request):
	t = loader.get_template('myanswer/basic.html')
	c = dict()
	if 'list' in request.POST:
		c['input1'] = request.POST['OneInput']
		c['input2'] = request.POST['TwoInput']
		c['OpValue'] = request.POST['Operation']
		c['Result'] = evaluat(c['input1'],c['input2'],c['OpValue'])

	else:
		c['Result'] = 'Your Answer here'
	return HttpResponse(t.render(c, request))

