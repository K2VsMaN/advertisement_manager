from nicegui import ui

@ui.page('/vendor/signin')
def show_signin_page():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    ui.query('.nicegui-row').classes('flex-nowrap')
    with ui.element("main").classes('w-full h-screen flex flex-col justify-center items-center p-4'):
        with ui.card().classes('w-[40%] bg-gray-100 justify-center items-center shadow-lg'):
            ui.label("Stellar").style('font-family: "Gwendolyn", cursive; font-weight: 700; font-style: normal').classes('text-xl font-bold text-gray-800')
            ui.label("Sign In").classes('text-xl font-bold text-orange-900')
            ui.separator().classes('w-[10%] h-0.5 bg-orange-800 mb-4')
            
            ui.input(placeholder="Email").props('type=email borderless').classes('w-[80%] bg-white px-4')
            ui.input(placeholder="Password", password=True, password_toggle_button=True).props('type=password borderless').classes('w-[80%] bg-white px-4')
            
            with ui.row().classes('flex flex-row justify-between items-center w-[80%]'):
                ui.checkbox(text="Remember me").classes('text-gray-600 text-sm w-1/2')
                ui.link("Forgot Password").classes('w-1/2 text-orange no-underline')
            ui.button(text="Login").classes('w-[80%] bg-orange text-white').props('flat dense no-caps')
            with ui.row().classes('text-gray-600 gap-0 space-x-2'):
                ui.label("Don't have an account?")
                ui.link("Sign Up", "/vendor/signup").classes('text-orange no-underline')