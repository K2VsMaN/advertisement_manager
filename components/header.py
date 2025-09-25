from nicegui import ui, app

def show_header():
    ui.add_head_html('''
    <style>
      .nav-link { text-decoration: none !important; }
      .create-btn {
        background: #f64209 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 9999px !important;
        padding: 0.5em 1.5em !important;
        letter-spacing: 1px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        align-items: center;
        display: flex;
        height: 48px;
      }
      .search-input input {
        background: transparent !important;
        color: white !important;
      }
    </style>
    ''')

    with ui.element('header').classes(
        'fixed top-0 left-0 w-full z-50 bg-black/50 backdrop-blur-md shadow-md' # Add fixed where neccessary
    ):
        with ui.element('div').classes('mx-auto max-w-7xl w-full px-6'):
            with ui.row().classes('items-center justify-between py-3 gap-4'):
                # Logo and All Events select side by side
                with ui.row().classes('items-center gap-4'):
                    with ui.element('a').classes(
                        'flex items-center gap-2 nav-link text-white'
                    ).props('href="/"'):
                        ui.icon('local_activity').classes('text-3xl text-[#f64209]')
                        ui.label('Ste').classes('font-bold text-2xl text-white')
                        ui.label('llar').classes('text-[#f64209] text-2xl font-semibold -ml-2')
                    

                # Navigation links and buttons
                with ui.row().classes('items-center gap-6'):

                    # CREATE EVENT button correctly aligned
                    ui.button("CREATE EVENT", on_click=lambda: ui.navigate.to("/vendor/add_event")) \
                        .classes("create-btn uppercase rounded-xl px-3 py-3 font-bold tracking-widest leading-tight") \
                        .style("background:#f64209; color:white; letter-spacing: 0.15em; align-items:center; height:38px;") \
                        .props("flat dense no-caps push ripple")
                    if app.storage.user.get("access_token"):
                        ui.button("Signout")
                    else:
                        ui.link('Sign In', '/vendor/signin').classes('nav-link text-white/90')