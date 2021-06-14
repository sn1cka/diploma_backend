import requests
from django.shortcuts import render
from django.views.generic import TemplateView

from main.settings import DOMAIN, PROTOCOL


class DjoserActivationView(TemplateView):
	def dispatch(self, request, *args, **kwargs):
		template_name = "activation.html"
		uid = kwargs.get("uid", None)
		token = kwargs.get("token", None)

		success = False
		if token and uid:
			payload = {'uid': uid, 'token': token}

			url = '{0}://{1}{2}'.format(PROTOCOL, DOMAIN, "/api/users/activation/")
			response = requests.post(url, data=payload)
			success = response.status_code == 204

		return render(request, template_name, {"is_success": success})
