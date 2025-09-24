from nicegui import ui


@ui.page("/vendor/signup")
def show_signup():
    ui.add_head_html('<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">')

    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    with ui.element("main").classes('w-full h-screen flex flex-col justify-center items-center p-4'):
        with ui.card().classes('w-[40%] bg-gray-100 justify-center items-center shadow-lg'):
            ui.label("Stellar").classes('text-xl font-bold text-gray-800')
            ui.label("Sign Up").classes('text-xl font-bold text-orange-500')
            ui.separator().classes('w-[10%] h-0.5 bg-orange-500 mb-4')
            with ui.row().classes("gap-0 mb-2"):
                ui.button(text="Vendor", on_click=lambda: ui.navigate.to('/vendor/signup'), icon="store").props(
                    "flat dense no-caps"
                ).classes('bg-orange-500 text-white px-8 py-2')
                ui.button(text="User", on_click=lambda: ui.navigate.to('/signup'), icon="person_add").props(
                    "flat dense no-caps"
                ).classes('bg-white text-orange-500 px-2 py-2')
            ui.input(placeholder="Email").props('type=email borderless').classes('w-[80%] bg-white px-4')
            ui.input(placeholder="Password", password=True, password_toggle_button=True).props('type=password borderless').classes('w-[80%] bg-white px-4')
            ui.input(placeholder="Confirm Password", password=True, password_toggle_button=True).props('type=password borderless').classes('w-[80%] bg-white px-4')
            ui.checkbox(text="Accept our terms and conditions and privacy policy").classes('text-gray-600 text-sm')
            ui.button(text="Sign Up").classes('w-[80%] text-white py-2').props('flat dense no-caps').style("background:#f64209;")
            with ui.row().classes('text-gray-600 gap-0 space-x-2'):
                ui.label("Already have an account?")
                ui.link("Login", "/vendor/signin").classes('text-orange-500 no-underline')