from nicegui import ui, events, run, app
from components.sidebar import show_sidebar
import requests
from utils.api import base_url


_create_event_btn: ui.button = None


def _run_create_event(data, files, token):
    return requests.post(
        f"{base_url}/adverts",
        data=data,
        files=files,
        headers={"Authorization": f"Bearer {token}"},
    )


async def _create_event(data, files):
    _create_event_btn.props(add="disable loading")
    response = await run.cpu_bound(
        _run_create_event, data, files, app.storage.user.get("access_token")
    )
    print(response.status_code, response.content)
    _create_event_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/vendor/events")
    elif response.status_code == 401:
        return ui.navigate.to("/vendor/signin")


@ui.page("/vendor/add_event")
def show_add_event_page():
    global _create_event_btn
    flyer_content = None

    def handle_flyer_upload(e: events.UploadEventArguments):
        nonlocal flyer_content
        flyer_content = e.content.read()

    ui.query(".nicegui-content").classes("m-0 p-0")
    ui.query(".nicegui-row").classes("flex-nowrap")
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
        with ui.column().classes("w-[20%] h-full"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full"):
            with ui.card().classes("w-full bg-white shadow-xl rounded-2xl p-6"):
                ui.label("Add An Event").classes(
                    "text-3xl font-bold text-orange-600 text-center mb-6"
                )

                # Event Title
                ui.label("Event Title").classes(
                    "text-lg font-semibold text-gray-700 mt-4"
                )
                event_title = (
                    ui.input("", placeholder="e.g. Startup Launch Party")
                    .props("outlined rounded-md dense")
                    .classes("w-full transition-all duration-300 hover:shadow-md")
                )

                # Event Description
                ui.label("Event Description").classes(
                    "text-lg font-semibold text-gray-700 mt-4"
                )
                event_description = (
                    ui.textarea(
                        "", placeholder="Write a brief overview of your event..."
                    )
                    .props("outlined rounded-md autogrow")
                    .classes("w-full transition-all duration-300 hover:shadow-md")
                )

                # Event Date and Location on the same row
                with ui.row().classes("w-full gap-4 mt-4"):
                    # Event Date
                    with ui.column().classes("flex-1"):
                        ui.label("Event Date").classes(
                            "text-lg font-semibold text-gray-700"
                        )
                        event_date = (
                            ui.input(value=["date"], placeholder="Select a date")
                            .props("type=date outlined rounded-md dense")
                            .classes("w-full")
                        )
                    # Event Location
                    with ui.column().classes("flex-1"):
                        ui.label("Event Location").classes(
                            "text-lg font-semibold text-gray-700"
                        )
                        event_location = (
                            ui.input(placeholder="e.g. 123 Main St, Anytown, USA")
                            .props("outlined rounded-md dense")
                            .classes("w-full")
                        )

                # Start and End Times on the same row
                with ui.row().classes("w-full gap-4 mt-4"):
                    # Start Time
                    with ui.column().classes("flex-1"):
                        ui.label("Start Time").classes(
                            "text-lg font-semibold text-gray-700"
                        )
                        start_time = (
                            ui.input("", placeholder="Select start time")
                            .props("type=time outlined rounded-md dense")
                            .classes("w-full")
                        )

                    # End Time
                    with ui.column().classes("flex-1"):
                        ui.label("End Time").classes(
                            "text-lg font-semibold text-gray-700"
                        )
                        end_time = (
                            ui.input(placeholder="Select end time")
                            .props("type=time outlined rounded-md dense")
                            .classes("w-full")
                        )

                    # --- Category and Price on the same row ---
                with ui.row().classes("w-full gap-4 mt-4"):
                    # Category
                    with ui.column().classes("flex-1"):
                        ui.label("Category").classes(
                            "text-lg font-semibold text-gray-700"
                        )
                        category = (
                            ui.input("", placeholder="e.g. Technology")
                            .props("outlined rounded-md dense")
                            .classes("w-full")
                        )

                    # Price
                    with ui.column().classes("flex-1"):
                        ui.label("Price").classes("text-lg font-semibold text-gray-700")
                        price = (
                            ui.input("", placeholder="e.g. 50")
                            .props("type=number outlined rounded-md dense")
                            .classes("w-full")
                        )

                # --- Image Upload Section ---
                ui.label("Event Flyer").classes(
                    "text-lg font-semibold text-gray-700 mt-4"
                )
                ui.upload(on_upload=handle_flyer_upload).props(
                    "flat bordered color=orange-600"
                ).classes("w-full").style("border: 2px dashed #ccc; padding: 20px;")

                with ui.row().classes("w-full justify-center mt-8"):
                    _create_event_btn = (
                        ui.button(
                            "Create Event",
                            color="primary",
                            on_click=lambda: _create_event(
                                {
                                    "title": event_title.value,
                                    "description": event_description.value,
                                    "category": category.value,
                                    "price": price.value,
                                    "advert_date": event_date.value,
                                    "start_time": start_time.value,
                                    "end_time": end_time.value,
                                    "location": event_location.value,
                                },
                                files={"flyer": flyer_content},
                            ),
                        )
                        .classes(
                            "text-lg font-semibold py-3 px-8 rounded-md shadow-lg transition-transform transform hover:scale-105 hover:shadow-2xl"
                        )
                        .props("flat dense no-caps")
                        .classes("text-white px-10")
                        .style("background:#f64209")
                    )
                    # .on('click', partial(ui.navigate.to, f'/adverts'))


ui.add_head_html(
    """
    <style>
        body {
            background-color: #f0f2f5;
        }
    </style>
"""
)
