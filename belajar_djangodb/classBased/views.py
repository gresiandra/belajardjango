from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexClass(View):
    
    template_name = 'classBased/classBased.html'
    context = {
        'heading':'Ini views dengan menggunakan ClasBased'
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['heading'] = 'ini POST'
        return render(request, self.template_name, self.context)
