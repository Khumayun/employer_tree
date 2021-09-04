from django.views.generic import ListView
from .models import Employer


class EmployerListView(ListView):
	model = Employer
	template_name = 'employer_list.html'
