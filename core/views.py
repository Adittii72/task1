from django.shortcuts import render
from .scraper import fetch_mock_case_details # Import our mock scraper
from .models import CaseQuery # Import our database model
import json

def case_search_view(request):
    context = {}
    if request.method == 'POST':
        # Get data from the submitted form 
        case_type = request.POST.get('case_type')
        case_number = request.POST.get('case_number')
        year = request.POST.get('year')

        # Call our mock scraper to get fake results
        results = fetch_mock_case_details(case_type, case_number, year)

        # Store the query and raw response in the database [cite: 24]
        CaseQuery.objects.create(
            case_type=case_type,
            case_number=case_number,
            year=year,
            parties_names=results.get('parties_names'),
            filing_date=results.get('filing_date'),
            next_hearing_date=results.get('next_hearing_date'),
            case_status=results.get('case_status'),
            raw_response=json.dumps(results) # Store the full response
        )

        # Pass the results to the template to be displayed [cite: 25]
        context['results'] = results
        context['query'] = {'case_type': case_type, 'case_number': case_number, 'year': year}

    return render(request, 'case_search.html', context)