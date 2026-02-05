from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from .forms import CVUploadForm
from .models import Analysis
from .services.cv_agent import CVAnalyzerAgent
from django.shortcuts import redirect

def home_view(request):
    error_message = None

    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save()
            agent = CVAnalyzerAgent()

            try:
                result = agent.analyze(
                    pdf_path=analysis.cv_file.path,
                    target_position=analysis.get_target_position_display()
                )
                analysis.result_json = result
                analysis.save(update_fields=["result_json"])
                return render(request, 'result.html', {'analysis': analysis})

            except Exception as e:
                error_message = str(e)
    else:
        form = CVUploadForm()

    return render(request, 'home.html', {'form': form, 'error': error_message})


def history_view(request):
    analyses = Analysis.objects.order_by('-created_at')
    return render(request, 'history.html', {'analyses': analyses})


def analysis_detail_view(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id)
    return render(request, 'result.html', {'analysis': analysis})


def download_summary_view(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id)
    result = analysis.result_json or {}

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="cv_analysis_{analysis.id}.pdf"'
    )

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>Resumen Optimizado</b>", styles["Heading2"]))
    content.append(Paragraph(result.get("optimized_summary", ""), styles["Normal"]))

    content.append(Paragraph("<br/><b>Fortalezas</b>", styles["Heading2"]))
    for item in result.get("strengths", []):
        content.append(Paragraph(f"- {item}", styles["Normal"]))

    content.append(Paragraph("<br/><b>Errores Detectados</b>", styles["Heading2"]))
    for item in result.get("errors", []):
        content.append(Paragraph(f"- {item}", styles["Normal"]))

    content.append(Paragraph("<br/><b>Sugerencias</b>", styles["Heading2"]))
    for item in result.get("suggestions", []):
        content.append(Paragraph(f"- {item}", styles["Normal"]))

    doc.build(content)
    return response



def delete_analysis_view(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id)
    analysis.delete()
    return redirect("history")