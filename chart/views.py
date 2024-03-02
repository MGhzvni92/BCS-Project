from django.shortcuts import render
from bcs.models import Cow, BcsData
from django.contrib.auth.decorators import login_required


@login_required
def show_chart(request):
    cow_id = request.GET.get('cow_id')
    if not cow_id:
        return render(request, 'chart/show_chart.html')

    try:
        cow = Cow.objects.get(code=cow_id)
    except Cow.DoesNotExist:
        return render(request, 'chart/show_chart.html', {'message': 'not found'})

    categories_datetime = BcsData.objects.filter(cow_id=cow_id).values_list('create_date', flat=True)
    categories = [date_obj.strftime('%Y-%m-%d') for date_obj in categories_datetime]
    values = BcsData.objects.filter(cow_id=cow_id).values_list('score', flat=True)

    context = {
        'cow': cow,
        'categories': list(categories),
        'values': list(values)
    }

    return render(request, 'chart/show_chart.html', context=context)

