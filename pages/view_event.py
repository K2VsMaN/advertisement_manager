from nicegui import ui

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

def show_view_event_page():
    ui.query(".nicegui-content").classes("m-0 p-0")
    # current_location = 'Accra'
    # ui.label(f'Events in {current_location}').classes('text-2xl font-bold mb-6 text-center')

    # Two-column detail view for each event
    for idx, ev in enumerate(events):
        with ui.element('section').classes('w-full py-6 mt-10') as section_container:
            with ui.element('div').classes('mx-auto max-w-5xl w-full px-6 '):
                with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-10 items-start'):
                    # Left: image
                    with ui.element('div').classes('w-full md:pr-6'):
                        img_el = ui.image(ev['image']) \
                            .classes('w-full h-auto rounded-xl shadow-md object-cover') \
                            .props(f'alt="{ev["title"]}"')

                    # Right: details + actions
                    with ui.element('div').classes('flex flex-col gap-3'):
                        title_lbl = ui.label(ev['title']).classes('text-2xl md:text-3xl font-bold leading-snug')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('place').classes('text-gray-600')
                            location_lbl = ui.label(ev['location']).classes('text-base whitespace-normal break-words')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('event').classes('text-gray-600')
                            date_lbl = ui.label(ev['date']).classes('text-base')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('payments').classes('text-gray-600')
                            price_lbl = ui.label(ev['price']).classes('text-base font-semibold')

                        # Actions: Get tickets | Edit | Delete
                        with ui.element('div').classes('mt-4 flex flex-wrap gap-3'):
                            ui.button('Get tickets', on_click=lambda e, t=ev['title']: ui.notify(f'Tickets flow for: {t}')) \
                                .classes('rounded-full px-6 py-3 font-bold') \
                                .props('color=orange text-color=white push ripple')

                            edit_btn = ui.button('Edit') \
                                .classes('rounded-full px-5 py-3 font-semibold') \
                                .props('color=grey-7 text-color=white push')

                            delete_btn = ui.button('Delete') \
                                .classes('rounded-full px-5 py-3 font-semibold') \
                                .props('color=red text-color=white push')

                        # -------- Edit dialog --------
                        # with ui.dialog() as edit_dlg, ui.card().classes('min-w-[340px] max-w-[90vw]'):
                        #     ui.label('Edit event').classes('text-lg font-bold mb-2')

                        #     title_in = ui.input('Title', value=ev['title']).classes('w-full')
                        #     date_in = ui.input('Date & time', value=ev['date']).classes('w-full')
                        #     location_in = ui.input('Location', value=ev['location']).classes('w-full')
                        #     price_sel = ui.select(['Free', 'Paid', 'RSVP'], value=ev['price'], label='Price').classes('w-full')
                        #     tag_sel = ui.select(['', 'Sponsored', 'Almost full', 'Going fast'],
                        #                         value=ev.get('tag') or '', label='Tag (optional)') \
                        #                  .props('clearable use-input').classes('w-full')
                        #     image_in = ui.input('Image URL', value=ev['image']).classes('w-full')

                        #     with ui.row().classes('justify-end gap-2 mt-4'):
                        #         ui.button('Cancel', on_click=edit_dlg.close).props('flat')

                        #         def save_changes():
                        #             # Update data
                        #             ev['title'] = title_in.value
                        #             ev['date'] = date_in.value
                        #             ev['location'] = location_in.value
                        #             ev['price'] = price_sel.value
                        #             ev['tag'] = tag_sel.value if tag_sel.value else None
                        #             ev['image'] = image_in.value

                        #             # Update UI
                        #             title_lbl.set_text(ev['title'])
                        #             date_lbl.set_text(ev['date'])
                        #             location_lbl.set_text(ev['location'])
                        #             price_lbl.set_text(ev['price'])
                        #             img_el.set_source(ev['image'])

                        #         ui.button('Save', on_click=lambda e: (save_changes(), edit_dlg.close())) \
                        #             .props('color=orange text-color=white push ripple')

                        # edit_btn.on('click', lambda e, d=edit_dlg: d.open())

                        # -------- Delete confirm dialog --------
                        with ui.dialog() as del_dlg, ui.card().classes('min-w-[320px] max-w-[90vw]'):
                            ui.label('Delete this event?').classes('text-lg font-bold')
                            ui.label(f'"{ev["title"]}" will be removed. This action cannot be undone.') \
                                .classes('text-gray-600 mb-4')

                            with ui.row().classes('justify-end gap-2'):
                                ui.button('Cancel', on_click=del_dlg.close).props('flat')

                                def confirm_delete():
                                    # Remove from data and UI
                                    events.pop(idx)
                                    section_container.delete()
                                    ui.notify('Event deleted', type='warning')
                                    del_dlg.close()

                                ui.button('Delete', on_click=lambda e: confirm_delete()) \
                                    .props('color=red text-color=white push')

                        delete_btn.on('click', lambda e, d=del_dlg: d.open())

ui.run()