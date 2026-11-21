from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ProgramaForm


def crear_programa(request):
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            programa = form.save()
            messages.success(request, f"Programa «{programa.nombre}» creado correctamente.")
            return redirect("crear_programa")
    else:
        form = ProgramaForm()
    return render(request, "myapp/programa_form.html", {"form": form})
