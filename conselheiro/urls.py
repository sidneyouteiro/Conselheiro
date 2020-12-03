from django.urls import path
from .views import * 


urlpatterns = [
    path('atualizarEmail/<int:pk>/',AtualizarEmail.as_view(template_name='user_update_form.html'),name='attEmailPage'),
    path('atualizarTracking/<int:pk>/',AtualizarTracking.as_view(template_name='tracking_update_form.html'),name='attTrackingPage'),
    path('deletarTracking/<int:pk>/',DeletarTracking.as_view(template_name='tracking_delete_form.html'),name='delTrackingPage'),
    path('adicionarAtivos/',addAtivos,name='addAtivosPage'),
    path('perfil/',perfil, name='perfilPage'),
    path('',home, name='homePage'),
]