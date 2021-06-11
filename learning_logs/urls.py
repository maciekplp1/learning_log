"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index_view, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics_view, name='topics'),
    # Detailed page for a single topic.
    path('topics/<int:topic_id>/', views.topic_view, name="topic"),
    # Page for adding new topics.
    path('new_topic/', views.new_topic_view, name='new_topic'),
    # Page for adding new entry.
    path('new_entry/<int:topic_id>', views.new_entry_view, name='new_entry'),
    # Page for edditing an entry.
    path('edit_entry/<int:entry_id>', views.edit_entry_view, name='edit_entry'),
]