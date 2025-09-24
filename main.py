from nicegui import ui, app

from components.header import show_header
from pages.home import show_home_page
from pages.view_event import show_view_event_page
from pages.view_event_2 import show_view_event_page_2
from pages.home_2 import show_home_page_2
from pages.home_3 import show_home_page_3
from components.footer import show_footer
from pages.vendor.dashboard import *
from pages.vendor.add_event import *
from pages.vendor.edit_event import *
from pages.vendor.events import *
<<<<<<< HEAD
from pages.vendor.signup import *
from pages.vendor.signin import *
from pages.user_signup import *
=======
from pages.vendor.dashboard import *
<<<<<<< HEAD
from pages.vendor.dashboard_2 import *
=======
>>>>>>> fe011a17d1282bc066c75d531356c6415d14dfd3
>>>>>>> 14647ac976834dce6021d17862ea4c7daf6e3eef

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

#ui.page - This decorator marks a function to be a page builder.

@ui.page("/")
def home_page():
    show_header()
    show_home_page()
    show_home_page_3()
    show_home_page_2()
    show_footer()
    

@ui.page("/view_event")
def add_view_page(id=""):
    show_header()
    show_view_event_page(id)
    show_view_event_page_2()
    show_footer()
    
    
@ui.page("/vendor/dashboard")
def dashboard():
    show_header()
    show_vendor_dashboard()
    show_vendor_dashboard_2()
    show_footer()

ui.run()