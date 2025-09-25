from nicegui import ui
from components.header import show_header

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
@ui.page("/all_events")
def show_all_events():
    city = 'Accra'
    with ui.element('div').classes('w-full flex justify-end'):
                        # ui.button('Home')\
                            # .props("flat dense no-caps push ripple")\
        # .classes("uppercase rounded-full  px-6 py-4 font-bold tracking-widest leading-tight mt-6 ml-auto text-center")\
        # .style("color:#f64209 !important; letter-spacing:0.15em; max-width:180px; border:0.5px solid #f64209")
        with ui.element('section').classes('w-full py-10 bg-gray-50 mt-20'):
                    ui.query(".nicegui-content").classes("m-0 p-0")
                    with ui.element('div').classes('mx-auto max-w-7xl w-full mb-30'):
                        ui.label('Ghana Events').classes('text-6xl font-extrabold mb-8 text-start text-orange-600')

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