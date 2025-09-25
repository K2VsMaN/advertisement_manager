from nicegui import ui 

# Shared data
events = [
    {
        'image': '/assets/CD1.jpeg',
        'title': 'Ako Adjei Lit Up 4.0',
        'date': 'Fri, Sep 26. 6PM - Sat 12AM',
        'location': 'Kukun, Accra',
        'price': 'Free',
        'tag': None,
    },
    {
        'image': '/assets/CD4.png',
        'title': 'Afro Flavors Food Festival 25',
        'date': 'Sun, Sep 14. 11AM - 9PM',
        'location': 'Ghud Park, Accra',
        'price': 'Free',
        'tag': None,
    },
    {
        'image': '/assets/CD6.jpg',
        'title': 'DETTY DEN HOUSE PARTY',
        'date': 'Sat, Sep 13. 7:30PM - Sun 2:45AM',
        'location': 'Oyibi, Greater Accra Region, Ghana, Oyibi',
        'price': 'RSVP',
        'tag': None,
    },
    {
        'image': '/assets/CD8.jpeg',
        'title': 'CUPS AND ARTS FESTIVAL',
        'date': 'Sat, Dec 6. 10AM - Sun 2:30AM',
        'location': "Afro's Event, Accra",
        'price': 'Paid',
        'tag': None,
    },
]

# Hover stroke effect (keeps original classes)
ui.add_head_html('''
<style>
.view-stroke { position: relative; }
.view-stroke::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;          /* respects rounded-xl */
  border: 2px solid rgba(249,115,22,0); /* orange-500 transparent */
  transform: scale(0.985);
  transition: border-color .25s ease, transform .25s ease;
  pointer-events: none;
}
.view-stroke:hover::before,
.view-stroke:focus-within::before {
  border-color: rgba(249,115,22,.9); /* orange ring on hover */
  transform: scale(1);
}
</style>
''')

# -------- LISTING PAGE --------
@ui.page('/')
def show_view_event_page_2():
    city = 'Accra'
    with ui.element('section').classes('w-full py-10 bg-gray-50'):
        with ui.element('div').classes('mx-auto max-w-7xl w-full mt-20 1`mb-30'):
            ui.label(f'Similar Events in {city}').classes('text-2xl font-bold mb-8 text-center')

            with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-10 mt-30'):
                for idx, ev in enumerate(events):
                    # Original styling + view-stroke + clickable
                    with ui.element('div').classes(
                        'group bg-white rounded-xl shadow-md overflow-hidden '
                        'transition-all duration-300 hover:shadow-lg h-full flex flex-col relative '
                        'view-stroke cursor-pointer'
                    ).props('tabindex=0 role=link aria-label="View details"') as card:
                        card.on('click', lambda e, i=idx: ui.navigate.to(f'/event/{i}'))

                        # Image + optional tag
                        with ui.element('div').classes('relative h-40 w-full overflow-hidden'):
                            ui.image(ev['image']).classes(
                                'h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105'
                            )
                            if ev.get('tag'):
                                ui.label(ev['tag']).classes(
                                    'absolute top-2 left-2 text-xs bg-red-100 text-red-600 font-semibold px-2 py-1 rounded-full'
                                )

                        # Content (unchanged)
                        with ui.element('div').classes('p-4 flex flex-col gap-1 grow'):
                            ui.label(ev['title']).classes('font-semibold text-md leading-snug')
                            ui.label(ev['date']).classes('text-sm text-gray-600')
                            with ui.element('div').classes('flex items-start gap-2 text-sm text-gray-600'):
                                ui.icon('place').classes('text-gray-500 flex-shrink-0 mt-[2px]')
                                ui.label(ev['location']).classes('flex-1 min-w-0 whitespace-normal break-words leading-snug')
                            ui.label(ev['price']).classes('text-sm text-gray-800 font-semibold')

# -------- VIEW PAGE WITH GET TICKETS / EDIT / DELETE --------
@ui.page('/event/{event_id}')
def view_page(event_id: str):
    try:
        idx = int(event_id)
        ev = events[idx]
    except Exception:
        ui.label('Event not found').classes('text-red-600 text-xl p-6')
        ui.link('Back to events', '/').classes('text-blue-600 underline p-6')
        return

    with ui.element('section').classes('w-full py-10 mt-30'):
        with ui.element('div').classes('mx-auto max-w-5xl w-full px-6'):
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-10 items-start'):
                # Left: image
                with ui.element('div').classes('w-full md:pr-6'):
                    img_el = ui.image(ev['image']).classes('w-full h-auto rounded-xl shadow-md object-cover') \
                        .props(f'alt="{ev["title"]}"')

                # Right: details + actions
                with ui.element('div').classes('flex flex-col gap-3'):
                    title_lbl = ui.label(ev['title']).classes('text-2xl md:text-3xl font-bold leading-snug')

                    # Optional tag chip
                    tag_lbl = ui.label(ev['tag'] or '').classes(
                        'inline-block text-xs bg-red-100 text-red-600 font-semibold px-2 py-1 rounded-full'
                    )
                    if not ev.get('tag'):
                        tag_lbl.visible = False

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('place').classes('text-gray-600')
                        location_lbl = ui.label(ev['location']).classes('text-base whitespace-normal break-words')

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('event').classes('text-gray-600')
                        date_lbl = ui.label(ev['date']).classes('text-base')

                    with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                        ui.icon('payments').classes('text-gray-600')
                        price_lbl = ui.label(ev['price']).classes('text-base font-semibold')

                    # Actions
                    with ui.row().classes('mt-4 gap-3'):
                        ui.button('Back to Events', on_click=lambda e: ui.navigate.to('/')) \
                            .classes('rounded-full px-5 py-3 font-semibold') \
                            .props('color=grey-7 text-color=white push')

                        ui.button('Get tickets', on_click=lambda e, t=ev['title']: ui.notify(f'Tickets flow for: {t}')) \
                            .classes('rounded-full px-6 py-3 font-bold') \
                            .props('color=orange text-color=white push ripple')

                        edit_btn = ui.button('Edit').classes('rounded-full px-5 py-3 font-semibold') \
                            .props('color=blue text-color=white push')

                        delete_btn = ui.button('Delete').classes('rounded-full px-5 py-3 font-semibold') \
                            .props('color=red text-color=white push')

                    # ---- Edit dialog ----
                    with ui.dialog() as edit_dlg, ui.card().classes('min-w-[340px] max-w-[90vw]'):
                        ui.label('Edit event').classes('text-lg font-bold mb-2')

                        title_in = ui.input('Title', value=ev['title']).classes('w-full')
                        date_in = ui.input('Date & time', value=ev['date']).classes('w-full')
                        location_in = ui.input('Location', value=ev['location']).classes('w-full')
                        price_sel = ui.select(['Free', 'Paid', 'RSVP'], value=ev['price'], label='Price').classes('w-full')
                        tag_sel = ui.select(['', 'Sponsored', 'Almost full', 'Going fast'],
                                            value=ev.get('tag') or '', label='Tag (optional)') \
                                 .props('clearable use-input').classes('w-full')
                        image_in = ui.input('Image URL', value=ev['image']).classes('w-full')

                        with ui.row().classes('justify-end gap-2 mt-4'):
                            ui.button('Cancel', on_click=edit_dlg.close).props('flat')

                            def save_changes():
                                # Update data
                                ev['title'] = title_in.value
                                ev['date'] = date_in.value
                                ev['location'] = location_in.value
                                ev['price'] = price_sel.value
                                ev['tag'] = tag_sel.value if tag_sel.value else None
                                ev['image'] = image_in.value

                                # Update UI immediately
                                title_lbl.set_text(ev['title'])
                                date_lbl.set_text(ev['date'])
                                location_lbl.set_text(ev['location'])
                                price_lbl.set_text(ev['price'])
                                img_el.set_source(ev['image'])

                                if ev.get('tag'):
                                    tag_lbl.set_text(ev['tag'])
                                    tag_lbl.visible = True
                                    tag_lbl.update()
                                else:
                                    tag_lbl.visible = False
                                    tag_lbl.update()

                                ui.notify('Event updated', type='positive')

                            ui.button('Save', on_click=lambda e: (save_changes(), edit_dlg.close())) \
                                .props('color=orange text-color=white push ripple')

                    edit_btn.on('click', lambda e, d=edit_dlg: d.open())

                    # ---- Delete confirm dialog ----
                    with ui.dialog() as del_dlg, ui.card().classes('min-w-[320px] max-w-[90vw]'):
                        ui.label('Delete this event?').classes('text-lg font-bold')
                        ui.label(f'"{ev["title"]}" will be removed. This action cannot be undone.') \
                            .classes('text-gray-600 mb-4')

                        with ui.row().classes('justify-end gap-2'):
                            ui.button('Cancel', on_click=del_dlg.close).props('flat')

                            def confirm_delete():
                                events.pop(idx)
                                ui.notify('Event deleted', type='warning')
                                del_dlg.close()
                                ui.navigate.to('/')

                            ui.button('Delete', on_click=lambda e: confirm_delete()) \
                                .props('color=red text-color=white push')

                    delete_btn.on('click', lambda e, d=del_dlg: d.open())


ui.run()