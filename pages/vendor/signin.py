from nicegui import ui, run, app
import requests
from utils.api import base_url

_login_btn: ui.button = None


def _run_login(data):
    return requests.post(f"{base_url}/users/login", data=data)


async def _login(data):
    _login_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_login, data)
    print(response.status_code, response.content)
    _login_btn.props(remove="disable loading")
    if response.status_code == 200:
        json_data = response.json()
        app.storage.user["access_token"] = json_data["access_token"]
        if json_data["role"] == "vendor":
            return ui.navigate.to("/vendor/dashboard")
        else:
            return ui.navigate.to("/")


@ui.page("/vendor/signin")
def show_signin_page():
    global _login_btn
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">'
    )

    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.element("main").classes(
        "w-full h-screen flex flex-col justify-center items-center p-4"
    ):
        with ui.card().classes(
            "w-[40%] bg-gray-100 justify-center items-center shadow-lg"
        ):
            ui.label("Stellar").classes("text-xl font-bold text-orange-600")
            ui.label("Sign In").classes("text-xl font-bold text-orange-500")
            ui.separator().classes("w-[10%] h-0.5 bg-orange-500 mb-4")

            email = (
                ui.input(placeholder="Email")
                .props("type=email borderless")
                .classes("w-[80%] bg-white px-4")
            )
            password = (
                ui.input(
                    placeholder="Password", password=True, password_toggle_button=True
                )
                .props("type=password borderless")
                .classes("w-[80%] bg-white px-4")
            )

            with ui.row().classes("flex flex-row justify-between items-center w-[80%]"):
                ui.checkbox(text="Remember me").classes("text-gray-600 text-sm w-1/2")
                ui.link("Forgot Password").classes("w-1/2 text-orange-500 no-underline")
            _login_btn = (
                ui.button(
                    text="Login",
                    on_click=lambda: _login(
                        {"email": email.value, "password": password.value}
                    ),
                )
                .classes("w-[80%] text-white")
                .props("flat dense no-caps")
                .style("background:#f64209;")
            )
            with ui.row().classes("text-gray-600 gap-0 space-x-2"):
                ui.label("Don't have an account?")
                ui.link("Sign Up", "/vendor/signup").classes(
                    "text-orange-500 no-underline"
                )
