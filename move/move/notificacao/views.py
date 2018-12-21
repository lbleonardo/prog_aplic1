from django.shortcuts import render, HttpResponse

# Create your views here.
def registrarSetor(request):
    if request.method == 'GET':
        return render(request, 'notificacao/formulario-registro.html', {})
    elif request.method == 'POST':
        nome = request.POST['nome']
        ep = request.POST['ep']
        setor = Setor(nome=nome, esferaPublica=ep)
        setor.save()
        return HttpResponse("<h1> Você é danado</h1>")
    else:
        return HttpResponse("<h1>Eu vou cadastrar o setor</h1>")

