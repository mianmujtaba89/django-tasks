from django.shortcuts import render, redirect
from .forms import DownloadForm

from django.views.generic import TemplateView


def aws(url):
    pass


def gcp(url):
    pass


def azure(url):
    pass


def handle_download_form(request):

    if request.method == 'POST':

        form = DownloadForm(request.POST)

        if form.is_valid():

            option = form.cleaned_data['drop_down']
            url = form.cleaned_data['url']

            if option == 'AWS':
                aws(url)
            elif option == 'GCP':
                gcp(url)
            elif option == 'AZURE':
                azure(url)

            return redirect('success')
    else:
        form = DownloadForm()
    context = {
        'form': form,
    }
    return render(request, 'download.html', context)


def handle_download_form_html(request):

    if request.method == 'POST':

        form_data = request.POST
        print(form_data)
        option = form_data['option']
        url = form_data['url']

        if option == 'AWS':
            aws(url)
        elif option == 'GCP':
            gcp(url)
        elif option == 'AZURE':
            azure(url)

        return redirect('success')
    else:
        return render(request, 'download0.html')


class SuccessView(TemplateView):
    template_name = 'success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Download process completed successfully!'
        return context