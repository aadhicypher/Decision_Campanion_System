from django.shortcuts import render, redirect
from .models import Decision, Option
from django.contrib.auth.decorators import login_required

@login_required
def decision_form(request):
    if request.method == "POST":
        category = request.POST.get("category")
        options_input = request.POST.get("options")

        decision = Decision.objects.create(
            user=request.user,
            category=category,
            context="Decision based on " + category
        )

        options_list = [opt.strip() for opt in options_input.split(",")]

        for opt in options_list:
            Option.objects.create(decision=decision, name=opt)

        request.session["decision_id"] = decision.id

        return redirect("questions_page")

    return render(request, "core/decision_form.html")


@login_required
def questions_page(request):
    decision_id = request.session.get("decision_id")
    decision = Decision.objects.get(id=decision_id)
    options = [opt.name for opt in decision.options.all()]

    # Temporary static questions (later dynamic)
    questions = [
        "How well does this option meet your main goal?",
        "How cost-effective is this option?",
        "How reliable is this option?",
    ]

    if request.method == "POST":
        # Just print scores for now
        for key, value in request.POST.items():
            if "__" in key:
                print(key, value)

        return redirect("decision_form")

    return render(request, "core/questions_page.html", {
        "questions": questions,
        "options": options
    })