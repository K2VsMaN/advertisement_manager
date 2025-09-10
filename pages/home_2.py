from nicegui import ui

def show_home_page_2():
    # Example data
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
            'image': '/assets/CD2.jpeg',
            'title': "Seli's Bistro presents Monthly Life Band Music with Cedi Band",
            'date': 'Fri, Sep 12. 7PM - Sat 12AM',
            'location': "Seli's Bistro, Accra",
            'price': 'Free',
            'tag': None,
        },
        {
            'image': '/assets/CD3.jpeg',
            'title': 'Update on the Economy Webinar Series',
            'date': 'Fri, Sep 19. 6:45PM - Sun 9PM',
            'location': 'University of Ghana (Legon)-Amphitheatre, Accra',
            'price': 'Paid',
            'tag': 'Sponsored',
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
            'image': '/assets/CD5.jpg',
            'title': 'Games Jams',
            'date': 'Fri, Sep 26. 2:30PM - 11:45PM',
            'location': 'Lakeside Estate , Tema',
            'price': 'Paid',
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
            'image': '/assets/CD7.jpg',
            'title': 'Guinness Ghana DJ Awards 2025',
            'date': 'Sat, Nov 29. 3PM - 11:45PM',
            'location': 'The Palms Convention Center, Accra',
            'price': 'Paid',
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

    city = 'Accra'

    with ui.element('section').classes('w-full py-10 bg-gray-50'):
        with ui.element('div').classes('mx-auto max-w-7xl w-full px-6'):
            ui.label(f'Events in {city}').classes('text-2xl font-bold mb-8 text-center')

            with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-10'):
                for ev in events:
                    with ui.element('div').classes(
                        'group bg-white rounded-xl shadow-md overflow-hidden '
                        'transition-all duration-300 hover:shadow-lg h-full flex flex-col relative'
                    ):
                        # Image with optional tag and edit button
                        with ui.element('div').classes('relative h-40 w-full overflow-hidden'):
                            img = ui.image(ev['image']) \
                                .classes('h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105') \
                                .props(f'alt="{ev["title"]}"')

                            tag_lbl = ui.label(ev['tag'] or '').classes(
                                'absolute top-2 left-2 text-xs bg-red-100 text-red-600 font-semibold px-2 py-1 rounded-full'
                            )
                            if not ev.get('tag'):
                                tag_lbl.visible = False

                            # Edit button (pencil)
                            edit_btn = ui.button(icon='edit') \
                                .classes('absolute top-2 right-2 bg-white/90 min-w-0 p-2 rounded-full') \
                                .props('flat round dense')

                        # Content
                        with ui.element('div').classes('p-4 flex flex-col gap-1 grow'):
                            title_lbl = ui.label(ev['title']).classes('font-semibold text-md leading-snug')
                            ui.label(ev['date']).classes('text-sm text-gray-600')

                            with ui.element('div').classes('flex items-start gap-2 text-sm text-gray-600'):
                                ui.icon('place').classes('text-gray-500 flex-shrink-0 mt-[2px]')
                                location_lbl = ui.label(ev['location']).classes('flex-1 min-w-0 whitespace-normal break-words leading-snug')

                            price_lbl = ui.label(ev['price']).classes('text-sm text-gray-800 font-semibold mt-auto')

                        # Edit dialog for this card
                        with ui.dialog() as dlg, ui.card().classes('min-w-[320px] max-w-[90vw]'):
                            ui.label('Edit event').classes('text-lg font-bold mb-2')

                            title_in = ui.input('Title', value=ev['title']).classes('w-full')
                            date_in = ui.input('Date & time', value=ev['date']).classes('w-full')
                            location_in = ui.input('Location', value=ev['location']).classes('w-full')
                            price_sel = ui.select(['Free', 'Paid', 'RSVP'], value=ev['price'], label='Price').classes('w-full')
                            tag_sel = ui.select(['', 'Sponsored', 'Almost full', 'Going fast'],
                                                value=ev.get('tag') or '', label='Tag (optional)') \
                                         .props('clearable use-input') \
                                         .classes('w-full')
                            image_in = ui.input('Image URL', value=ev['image']).classes('w-full')

                            with ui.row().classes('justify-end gap-2 mt-4'):
                                ui.button('Cancel', on_click=dlg.close).props('flat')
                                def save_changes():
                                    # Update data
                                    ev['title'] = title_in.value
                                    ev['date'] = date_in.value
                                    ev['location'] = location_in.value
                                    ev['price'] = price_sel.value
                                    ev['tag'] = tag_sel.value if tag_sel.value else None
                                    ev['image'] = image_in.value

                                    # Update UI
                                    title_lbl.set_text(ev['title'])
                                    location_lbl.set_text(ev['location'])
                                    price_lbl.set_text(ev['price'])
                                    img.set_source(ev['image'])

                                    if ev.get('tag'):
                                        tag_lbl.set_text(ev['tag'])
                                        tag_lbl.visible = True
                                        tag_lbl.update()
                                    else:
                                        tag_lbl.visible = False
                                        tag_lbl.update()

                                ui.button('Save', on_click=lambda e: (save_changes(), dlg.close())) \
                                    .props('color=orange text-color=white push ripple')

                        # Open dialog on edit button
                        edit_btn.on('click', lambda e, d=dlg: d.open())

show_home_page_2()
ui.run()