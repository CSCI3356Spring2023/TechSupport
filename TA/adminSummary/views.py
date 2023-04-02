from django.shortcuts import render

def admin_summary_view(response):
    return render(response, "admin_summary.html", {})
