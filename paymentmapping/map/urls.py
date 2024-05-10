from django.urls import path
from .views import upload_csv,get_column_names,get_mapping_data,post_mapping_data
urlpatterns = [
    path('post_mapping_data',post_mapping_data.as_view()),
    path('view_mapping_data',get_mapping_data.as_view()),
    path('upload_csv',upload_csv),
    path('get_columns',get_column_names.as_view())]