from django.shortcuts import render
from bcs.models import Cow, BcsData


def show_chart(request):
    cow_id = request.GET.get('cow_id')
    if not cow_id:
        return render(request, 'chart/show_chart.html')

    categories = BcsData.objects.filter(cow_id=cow_id).values_list('create_date', flat=True)
    values = BcsData.objects.filter(cow_id=cow_id).values_list('score', flat=True)

    context = {
        "categories": list(categories),
        'values': list(values)
    }

    return render(request, 'chart/show_chart.html', context=context)

