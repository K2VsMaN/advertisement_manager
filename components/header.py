from nicegui import ui 
def show_header():
    with ui.row():
        ui.link("Home", "/")
        ui.link("Add_Event","/add_event")
        ui.link("Edit_Event", "/edit_event")
        ui.link("View_Event", "/view_event")