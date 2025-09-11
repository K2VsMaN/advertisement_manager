from nicegui import ui, app

from components.header import show_header
from pages.home import show_home_page
from pages.add_event import show_add_event_page
from pages.edit_event import show_edit_event_page
from pages.view_event import show_view_event_page
from pages.view_event_2 import show_view_event_page_2
from pages.home_2 import show_home_page_2
from components.footer import show_footer

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

#ui.page - This decorator marks a function to be a page builder.

@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    show_home_page_2()
    show_footer()
    
@ui.page("/add_event")
def add_event_page():
    show_header()
    show_add_event_page()
    show_footer()

@ui.page("/edit_event")
def add_edit_page():
    show_header()
    show_edit_event_page()
    show_footer()

@ui.page("/view_event")
def add_view_page():
    show_header()
    show_view_event_page()
    show_view_event_page_2()
    show_footer()
    

ui.run()