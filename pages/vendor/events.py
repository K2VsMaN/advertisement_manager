from nicegui import ui
from components.sidebar import show_sidebar


def show_advert_card():
    with ui.card().on(type="click", handler=lambda: ui.navigate.to("/view_advert")).classes("w-80 p-6 rounded-2xl shadow-md cursor-pointer"):
        with ui.row().classes("items-center space-x-4"):
            ui.image("/assets/CD1.jpeg").classes("w-14 h-14 rounded-lg")
            with ui.column().classes("items-start"):
                ui.label("LLC Records").classes("font-semibold text-lg")
                ui.label("Kumasi, Ghana").classes("text-sm").style("margin-top: -10px;")
        ui.label("Sound Engineer").style("font-size: 1.2rem; font-weight: bold")
        ui.label("Contract").style("font-size: 0.9rem; color: #000;")
        ui.label("Mixing, Mastering, Production").classes("")
        with ui.row().classes("justify-between items-center flex flex-row space-x-8"):
            ui.label("$5000/monthly")
            ui.button("Apply Now", on_click=lambda: ui.navigate.to('/view_advert')).props("flat dense no-caps").classes("px-2 py-2 bg-green text-white")

@ui.page("/vendor/events")
def show_vendor_events():
    ui.query('.nicegui-row').classes('flex-nowrap')
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
       with ui.column().classes("w-[20%] h-full"):
           show_sidebar()
       with ui.column().classes("w-[80%] h-full"):
           with ui.column().classes('flex flex-col justify-center items-center w-full'):
            ui.label("Recent Job Posts").classes('text-4xl')
            ui.separator().classes('h-1 bg-green w-1/5 mb-8')
            with ui.grid(columns=3).classes('gap-10'):
                for i in range(6):
                    show_advert_card()