from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import (
    Category,
    SubCategory,
    CategoryCriterion,
    Decision,
    Option,
    Criterion,
    Score,
    Result
)


# ==============================
# STEP 1 – Create Decision
# ==============================

@login_required
def decision_form(request):

    categories = Category.objects.all()

    if request.method == "POST":
        subcategory_id = request.POST.get("subcategory")
        options_input = request.POST.get("options")
        context = request.POST.get("context")

        subcategory = SubCategory.objects.get(id=subcategory_id)

        decision = Decision.objects.create(
            user=request.user,
            subcategory=subcategory,
            context=context
        )

        # Create options
        options_list = [opt.strip() for opt in options_input.split(",")]

        for opt in options_list:
            Option.objects.create(decision=decision, name=opt)

        # Copy template criteria into decision-specific criteria
        template_criteria = CategoryCriterion.objects.filter(
            subcategory=subcategory
        )

        for template in template_criteria:
            Criterion.objects.create(
                decision=decision,
                name=template.name,
                weight=template.default_weight,
                is_positive=template.is_positive
            )

        request.session["decision_id"] = decision.id

        return redirect("questions_page")

    return render(request, "core/decision_form.html", {
        "categories": categories
    })


# ==============================
# STEP 2 – Scoring Page
# ==============================

@login_required
def questions_page(request):

    decision_id = request.session.get("decision_id")

    if not decision_id:
        return redirect("decision_form")

    decision = get_object_or_404(Decision, id=decision_id)

    options = decision.options.all()
    criteria = decision.decision_criteria.all()

    if request.method == "POST":

        # 🔥 Remove old scores for this decision (important)
        Score.objects.filter(option__decision=decision).delete()

        # Save fresh scores
        for criterion in criteria:
            for option in options:
                field_name = f"{criterion.id}__{option.id}"
                value = request.POST.get(field_name)

                if value:
                    Score.objects.create(
                        option=option,
                        criterion=criterion,
                        value=int(value)
                    )

        # 🔥 Calculate final scores (strictly for this decision)
        results = {}

        for option in options:
            total = 0

            # FIXED: Filter by BOTH option AND this decision's criteria
            option_scores = Score.objects.filter(
                option=option,
                criterion__decision=decision
            )

            for score in option_scores:
                total += score.value * score.criterion.weight

            results[option] = total

        if not results:
            return redirect("decision_form")

        best_option = max(results, key=results.get)

        # Remove old result if exists
        Result.objects.filter(decision=decision).delete()

        Result.objects.create(
            decision=decision,
            chosen_option=best_option,
            total_score=results[best_option]
        )

        return redirect("result_page")

    return render(request, "core/questions_page.html", {
        "decision": decision,
        "options": options,
        "criteria": criteria
    })


# ==============================
# STEP 3 – Result Page
# ==============================

@login_required
def result_page(request):

    decision_id = request.session.get("decision_id")

    decision = get_object_or_404(Decision, id=decision_id)
    result = get_object_or_404(Result, decision=decision)

    return render(request, "core/result_page.html", {
        "decision": decision,
        "result": result
    })