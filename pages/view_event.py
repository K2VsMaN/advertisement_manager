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
]

# Optional (kept from your snippet; not required for this layout)
ui.add_head_html('''
<style>
.event-card { border-radius: 12px; overflow: hidden; background: #fff; width: 16rem; display: flex; flex-direction: column; box-shadow: 0 6px 16px rgba(0,0,0,.08); transition: transform .25s ease, box-shadow .25s ease; }
.event-card:hover { transform: translateY(-4px); box-shadow: 0 10px 20px rgba(0,0,0,.12); }
.image-wrap { position: relative; height: 160px; overflow: hidden; }
.image-wrap img { width: 100%; height: 100%; object-fit: cover; transition: transform .5s ease; display: block; }
.event-card:hover .image-wrap img { transform: scale(1.05); }
.tag-badge { position: absolute; top: 10px; left: 10px; background: #fee2e2; color: #b91c1c; padding: 4px 10px; border-radius: 9999px; font-weight: 700; font-size: 11px; letter-spacing: .04em; }
.title-clamp { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
</style>
''')

def show_view_event_page():
    current_location = 'Accra'
    ui.label(f'Events in {current_location}').classes('text-2xl font-bold mb-6 text-center')

    # Two-column detail view
    for event in events:
        with ui.element('section').classes('w-full py-6'):
            with ui.element('div').classes('mx-auto max-w-5xl w-full px-6'):
                # Grid: image left, details right; stacked on small screens
                with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-10 items-start'):
                    # Left: image with margin (via grid gap and padding)
                    with ui.element('div').classes('w-full md:pr-6'):
                        ui.element('img').props(
                            f'src="{event["image"]}" '
                            'loading="lazy" '
                            f'alt="{event["title"]}" '
                            'onerror="this.onerror=null;this.src=\'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1200&auto=format&fit=crop\';"'
                        ).classes('w-full h-auto rounded-xl shadow-md object-cover')

                    # Right: details
                    with ui.element('div').classes('flex flex-col gap-3'):
                        ui.label(event['title']).classes('text-2xl md:text-3xl font-bold leading-snug')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('place').classes('text-gray-600')
                            ui.label(event['location']).classes('text-base whitespace-normal break-words')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('event').classes('text-gray-600')
                            ui.label(event['date']).classes('text-base')

                        with ui.element('div').classes('flex items-start gap-2 text-gray-700'):
                            ui.icon('payments').classes('text-gray-600')
                            ui.label(event['price']).classes('text-base font-semibold')

                        ui.button('Get tickets') \
                            .classes('mt-4 self-start rounded-full px-6 py-3 font-bold') \
                            .props('color=orange text-color=white push ripple')

show_view_event_page()
ui.run()