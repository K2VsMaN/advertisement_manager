from nicegui import ui,app

def _sign_out():
    app.storage.user.clear()
    ui.navigate.to("/")

def show_sidebar():
    """
    Creates a static sidebar for the vendor dashboard using a ui.column.
    """
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.column().classes('bg-gray-100 p-4 w-[20%] shadow-lg h-full justify-between items-center fixed'):
        # Top section with branding and vendor info
        with ui.column().classes('w-full items-center mb-6'):
            ui.link("Stellar", "/vendor/dashboard").classes('text-4xl font-extrabold no-underline').style("color:#f64209")
            ui.label("Vendor Dashboard").classes('text-lg font-bold text-gray-800')
        
        ui.separator().classes('w-full h-0.5 mb-6').style("background:#f64209")

        # Navigation links section
        with ui.column().classes('w-full space-y-4 flex-grow'):
            # Dashboard
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-orange-100 transition-colors p-2 rounded-lg'):
                ui.icon('dashboard').classes('text-orange-600')
                ui.link('Dashboard', '/vendor/dashboard').classes('text-gray-700 font-semibold no-underline text-lg')
            
            # Events (Manage and Create)
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-orange-100 transition-colors p-2 rounded-lg'):
                ui.icon('event').classes('text-orange-600')
                ui.link('Events', '/vendor/events').classes('text-gray-700 font-semibold no-underline text-lg')
            
            # Analytics
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-orange-100 transition-colors p-2 rounded-lg'):
                ui.icon('analytics').classes('text-orange-600')
                ui.link('Analytics', '/vendor/analytics').classes('text-gray-700 font-semibold no-underline text-lg')
            
            # Settings
            with ui.row().classes('w-full items-center cursor-pointer hover:bg-orange-100 transition-colors p-2 rounded-lg'):
                ui.icon('settings').classes('text-orange-600')
                ui.link('Settings', '/vendor/settings').classes('text-gray-700 font-semibold no-underline text-lg')
            
        # Logout button at the bottom
        with ui.column().classes('w-full items-center mt-auto'):
            ui.separator().classes('w-full h-0.5 mb-6').style("background:#f64209")
            with ui.row().classes('w-full items-center cursor-pointer p-2 rounded-lg hover:bg-red-100 transition-colors'):
                ui.icon('logout').classes('text-red-600')
                ui.button(text='Logout', on_click=_sign_out, color='red').classes('bg-transparent text-red-600 font-semibold shadow-none text-lg').props('flat no-caps')

    