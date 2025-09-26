from nicegui import ui, app

def _sign_out():
    app.storage.user.clear()
    ui.navigate.to("/")


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

    def on_search():
        # ui.notify(f'Searching for: {search_box.value}', type='positive')

        with ui.element('header').classes(
        'fixed top-0 left-0 w-full z-50 bg-black/50 backdrop-blur-md shadow-md'
    ):
            with ui.element('div').classes('mx-auto max-w-7xl w-full px-6'):
                with ui.row().classes('items-center justify-between py-3 gap-4'):

                # ------------------ LEFT: Logo Section ------------------
                    with ui.row().classes('items-center gap-4'):
                        with ui.element('a').classes(
                        'flex items-center gap-2 nav-link text-white'
                    ).props('href="/"'):
                            ui.icon('local_activity').classes('text-3xl text-[#f64209]')
                        ui.label('Ste').classes('font-bold text-2xl text-white')
                        ui.label('llar').classes('text-[#f64209] text-2xl font-semibold -ml-2')

                # ------------------ CENTER: Search Bar ------------------
                # ui.input(placeholder='Search...').classes('text-white').style('color:white;').props('flat dense').classes('w-full max-w-md rounded-md p-2 border border-gray-600 text-sm placeholder-white text-white')
                # Input field
                ui.input(placeholder='Search...') \
                    .classes('text-white') \
                    .style('color: white;')  # This ensures text is white during typing

                # Inject global style for placeholder + focus behavior
                ui.add_head_html('''
                <style>
                    input::placeholder {
                        color: white !important;
                        opacity: 1;
                    }

                    input:focus {
                        color: white !important;
                        caret-color: white !important;
                    }
                </style>
                ''')




                # ------------------ RIGHT: Actions ------------------
                with ui.row().classes('items-center gap-6'):

                    ui.button("CREATE EVENT", on_click=lambda: ui.navigate.to("/vendor/add_event")) \
                        .classes("create-btn uppercase rounded-xl px-3 py-3 font-bold tracking-widest leading-tight") \
                        .style("background:#f64209; color:white; letter-spacing: 0.15em; align-items:center; height:38px;") \
                        .props("flat dense no-caps push ripple")

                    if app.storage.user.get("access_token"):
                        ui.button(text="Signout",on_click=_sign_out, color="red")
                    else:
                        ui.link('Sign In', '/vendor/signin').classes('nav-link text-white/90')
