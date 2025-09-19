from nicegui import ui
import requests
from utils.api import base_url

# Example data for events (now with location)
events = [
    {
        'image': '/assets/CD1.jpeg',
        'title': 'Ako Adjei Lit Up 4.0',
        'date': 'Fri, Sep 26. 6PM - Sat 12AM',
        'location': 'Kukun, Accra',
        'price': 'Free',
        'tag': None,
    },
    # add more events if needed...
]

def show_view_event_page(id):
    response = requests.get(f"{base_url}/adverts/{id}")
    json_data = response.json()
    ev = json_data["data"]
    ui.query(".nicegui-content").classes("m-0 p-0")
    # current_location = 'Accra'
    # ui.label(f'Events in {current_location}').classes('text-2xl font-bold mb-6 text-center')

    # Two-column detail view for each event
    with ui.element('section').classes('w-full py-6 mt-10') as section_container:
        with ui.element('div').classes('mx-auto max-w-5xl w-full px-6 '):
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-10 items-start'):
                # Left: image
                with ui.element('div').classes('w-full md:pr-6'):
                    img_el = ui.image(ev['flyer']) \
                        .classes('w-full h-auto rounded-xl shadow-md object-cover') \
                        .props(f'alt="{ev["title"]}"')

                # Right: details + actions
                with ui.element('div').classes('flex flex-col gap-3'):
                    title_lbl = ui.label(ev['title']).classes('text-2xl md:text-3xl font-bold leading-snug')

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('place').classes('text-gray-600')
                        location_lbl = ui.label(ev['description']).classes('text-base whitespace-normal break-words')

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('event').classes('text-gray-600')
                        date_lbl = ui.label(ev['advert_date']).classes('text-base')

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('payments').classes('text-gray-600')
                        price_lbl = ui.label(ev['price']).classes('text-base font-semibold')

                    # Actions: Get tickets | Edit | Delete
                    with ui.element('div').classes('mt-4 flex flex-wrap gap-3'):
                        ui.button('Get tickets', on_click=lambda e, t=ev['title']: ui.notify(f'Tickets flow for: {t}')) \
                            .classes('rounded-full px-6 py-3 font-bold') \
                            .props('color=orange text-color=white push ripple')

                        edit_btn = ui.button('Edit',on_click=lambda: ui.navigate.to("/edit_event")) \
                            .classes('rounded-full px-5 py-3 font-semibold') \
                            .props('color=grey-7 text-color=white push')

                        delete_btn = ui.button('Delete') \
                            .classes('rounded-full px-5 py-3 font-semibold') \
                            .props('color=red text-color=white push')

                    # -------- Delete confirm dialog --------
                    with ui.dialog() as del_dlg, ui.card().classes('min-w-[320px] max-w-[90vw]'):
                        ui.label('Delete this event?').classes('text-lg font-bold')
                        ui.label(f'"{ev["title"]}" will be removed. This action cannot be undone.') \
                            .classes('text-gray-600 mb-4')

                        with ui.row().classes('justify-end gap-2'):
                            ui.button('Cancel', on_click=del_dlg.close).props('flat')

                            def confirm_delete():
                                response = requests.delete(f"{base_url}/adverts/{id}")
                                if response.status_code == 200:
                                    ui.navigate.to("/")

                            ui.button('Delete', on_click=lambda e: confirm_delete()) \
                                .props('color=red text-color=white push')

                    delete_btn.on('click', lambda e, d=del_dlg: d.open())

