from nicegui import ui 

from components.header import show_header
from pages.home import show_home_page
from pages.add_event import show_add_event_page
from pages.edit_event import show_edit_event
from pages.view_event import show_view_event


#ui.page - This decorator marks a function to be a page builder.

@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    
@ui.page("/add_event")
def add_event_page():
    show_header()
    show_add_event_page()

@ui.page("/edit_event")
def add_edit_page():
    show_header()
    show_edit_event()

@ui.page("/view_event")
def add_view_page():
    show_header()
    show_view_event()
    

ui.run()