from django.shortcuts import render, get_object_or_404, redirect
from .models import ForwarderModel
from .forms import ForwarderForm


INVALID_ACCESS_CODE_MSG = 'Invalid access code'


def index(request):
    return redirect('https://yandex.ru')


def forwarder(request, slug):
    rule = get_object_or_404(ForwarderModel, slug=slug)
    form = ForwarderForm(request.POST or None)
    if request.method == 'POST':
        if form['access_code'].value() == rule.access_code:
            return redirect(rule.redirect_url)
        return render(request, 'main/forwarder.html',
                      {
                          'form': form,
                          'error_msg': INVALID_ACCESS_CODE_MSG,
                      }
                      )
    return render(request, 'main/forwarder.html', {'form': form})

