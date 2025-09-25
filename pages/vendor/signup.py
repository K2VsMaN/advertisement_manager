from nicegui import ui, run
import requests
from utils.api import base_url


_signup_btn: ui.button = None


def _run_signup(data):
    return requests.post(f"{base_url}/users/signup", data=data)


async def _signup(data):
    _signup_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    _signup_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/vendor/signin")
    elif response.status_code == 409:
        return ui.notify(message="User already exists!",type="warning")


@ui.page("/vendor/signup")
def show_signup():
    global _signup_btn
    ui.add_head_html(
        '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Gwendolyn:wght@400;700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lavishly+Yours&family=Stoke:wght@300;400&display=swap" rel="stylesheet">'
    )

    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    with ui.element("main").classes(
        "w-full h-screen flex flex-col justify-center items-center p-4"
    ):
        with ui.card().classes(
            "w-[40%] bg-gray-100 justify-center items-center shadow-lg"
        ):
            ui.label("Stellar").classes("text-xl font-bold text-orange-900")
            ui.label("Sign Up").classes("text-xl font-bold text-orange-500")
            ui.separator().classes("w-[10%] h-0.5 bg-orange-500 mb-4")
            with ui.row().classes("gap-0 mb-2"):
                ui.button(
                    text="Vendor",
                    on_click=lambda: ui.navigate.to("/vendor/signup"),
                    icon="store",
                ).props("flat dense no-caps").classes("text-white px-8 py-2").style(
                    "background:#f64209"
                )
                ui.button(
                    text="User",
                    on_click=lambda: ui.navigate.to("/signup"),
                    icon="person_add",
                ).props("flat dense no-caps").classes("bg-white text-orange px-2 py-2")
            username = (
                ui.input(placeholder="Username")
                .props("type=name borderless")
                .classes("w-[80%] bg-white px-4")
            )
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
            confirm_password = (
                ui.input(
                    placeholder="Confirm Password",
                    password=True,
                    password_toggle_button=True,
                )
                .props("type=password borderless")
                .classes("w-[80%] bg-white px-4")
            )
            ui.checkbox(
                text="Accept our terms and conditions and privacy policy"
            ).classes("text-gray-600 text-sm")
            _signup_btn = (
                ui.button(
                    text="Sign Up",
                    on_click=lambda: _signup(
                        {
                            "username": username.value,
                            "email": email.value,
                            "password": password.value,
                            "confirm_password": confirm_password.value,
                            "role": "vendor"
                        }
                    ),
                )
                .classes("w-[80%] text-white py-2")
                .props("flat dense no-caps")
                .style("background:#f64209;")
            )
            with ui.row().classes("text-gray-600 gap-0 space-x-2"):
                ui.label("Already have an account?")
                ui.link("Login", "/vendor/signin").classes(
                    "text-orange-500 no-underline"
                )
