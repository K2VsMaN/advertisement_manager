from nicegui import ui

def show_header():
    # Ensure links have no underline everywhere
    ui.add_head_html('''
    <style>
      .nav-link { text-decoration: none !important; }
    </style>
    ''')

    with ui.element('header').classes(
        'fixed top-0 left-0 w-full z-50 '
        'bg-black/50 backdrop-blur-md shadow-md'
    ):
        with ui.element('div').classes('mx-auto max-w-7xl w-full px-6'):
            with ui.row().classes('items-center justify-between py-3'):
                # Brand: logo + text side by side (both clickable)
                with ui.element('a').classes(
                    'flex items-center gap-2 nav-link text-white'
                ).props('href="/"'):
                    ui.icon('public').classes('text-2xl')
                    ui.label('Stellar') \
                        .classes('font-bold text-xl drop-shadow') \
                        .style('text-shadow: 0 1px 1px rgba(0,0,0,.35);')

                # Nav links
                base = (
                    'nav-link text-white/90 no-underline '
                    'px-3 py-2 rounded-md transition-all duration-200 '
                    'hover:text-white hover:bg-white/15 hover:shadow-sm'
                )
                with ui.row().classes('items-center gap-2'):
                    ui.link('Home', '/').classes(base)
                    ui.link('Add Event', '/add_event').classes(base)
                    ui.link('Edit Event', '/edit_event').classes(base)
                    ui.link('View Event', '/view_event').classes(base)

# show_header()
# ui.run()