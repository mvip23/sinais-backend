from django.urls import path
from django.http import HttpResponse

def dashboard_view(request):
    """Dashboard principal do sistema"""
    return HttpResponse("""
    <html>
    <head><title>Sistema JAM - Dashboard</title></head>
    <body>
        <h1>🏢 Sistema JAM - Dashboard</h1>
        <p>✅ Sistema ERP funcionando!</p>
        <p>🔧 <a href="/admin/">Admin Django</a></p>
        <p>🏠 <a href="/">Voltar ao site</a></p>
    </body>
    </html>
    """)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
] 