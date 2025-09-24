from nicegui import ui, events
from datetime import datetime
from components.sidebar import show_sidebar
from utils.api import base_url

@ui.page("/vendor/edit_event")
def show_edit_event_page():
    # flyer_content = None

    # def edit_event(data, files):
    #     response = requests.put(f"{base_url}/adverts/{id}", data=data, files=files)
    #     if response.status_code == 200:
    #         ui.navigate.to("/")
    #     print(response.json())

    # def handle_flyer_upload(e:events.UploadEventArguments):
    #     nonlocal flyer_content
    #     flyer_content = e.content.read()
    ui.add_head_html('''
    <style>
        body {
            background-color: #f0f2f5;
        }
    </style>
''')
    ui.query(".nicegui-content").classes("m-0 p-0")
    ui.query(".nicegui-row").classes('flex-nowrap')
    with ui.row().classes("w-full h-screen flex flex-row justify-between items-center"):
        with ui.column().classes("w-[20%] h-full"):
            show_sidebar()
        with ui.column().classes("w-[80%] h-full"):
            with ui.card().classes('w-full bg-white shadow-xl rounded-2xl p-6'):
                ui.label('Edit Event').classes('text-3xl font-bold text-gray-800 text-center mb-6')

                # Event Title
                ui.label('Event Title').classes('text-lg font-semibold text-gray-700 mt-4')
                event_title = ui.input(value=['title'], placeholder='e.g. Startup Launch Party').props('outlined rounded-md dense').classes('w-full transition-all duration-300 hover:shadow-md')

                # Event Description
                ui.label('Event Description').classes('text-lg font-semibold text-gray-700 mt-4')
                event_description = ui.textarea(value=['description'], placeholder='Write a brief overview of your event...').props('outlined rounded-md autogrow').classes('w-full transition-all duration-300 hover:shadow-md')

                # Event Date
                ui.label('Event Date').classes('text-lg font-semibold text-gray-700 mt-4')
                event_date = ui.input(value=['date'], placeholder='Select a date').props('type=date outlined rounded-md dense').classes('w-full transition-all duration-300 hover:shadow-md')

                # Start and End Times on the same row
                with ui.row().classes('w-full gap-4 mt-4'):
                    # Start Time
                    with ui.column().classes('flex-1'):
                        ui.label('Start Time').classes('text-lg font-semibold text-gray-700')
                        start_time = ui.input(value=['start_time'], placeholder='Select start time').props('type=time outlined rounded-md dense').classes('w-full')

                    # End Time
                    with ui.column().classes('flex-1'):
                        ui.label('End Time').classes('text-lg font-semibold text-gray-700')
                        end_time = ui.input(value=['end_time'], placeholder='Select end time').props('type=time outlined rounded-md dense').classes('w-full')

                # --- Category and Price on the same row ---
                with ui.row().classes('w-full gap-4 mt-4'):
                    # Category
                    with ui.column().classes('flex-1'):
                        ui.label('Category').classes('text-lg font-semibold text-gray-700')
                        category = ui.input('', placeholder='e.g. Technology').props('outlined rounded-md dense').classes('w-full')

                    # Price
                    with ui.column().classes('flex-1'):
                        ui.label('Price').classes('text-lg font-semibold text-gray-700')
                        price = ui.input(placeholder='e.g. 50').props('type=number outlined rounded-md dense').classes('w-full')    

                # Image Upload Section (you might want to display the current image and allow a new one to be uploaded)
                ui.label('Event Flyer').classes('text-lg font-semibold text-gray-700 mt-4')
                # This upload component can be used to replace the existing image
                ui.upload(on_upload=lambda e: ui.notify(f'New image "{e.name}" uploaded')).props('flat bordered').classes('w-full').style('border: 2px dashed #ccc; padding: 20px;')

                with ui.row().classes('w-full justify-center mt-8 gap-4'):
                    # The "Create" button is changed to "Save Changes"
                    ui.button('Save Changes', color='primary'
                    #           , on_click=lambda:edit_event({
                    #     "title": event_title.value,
                    #     "description": event_description.value,
                    #     "category": category.value,
                    #     "price": price.value,
                    #     "advert_date": event_date.value,
                    #     "start_time": start_time.value,
                    #     "end_time": end_time.value},
                    #     files={"flyer": flyer_content
                    # })
                    ).classes('text-lg font-semibold py-3 px-8 rounded-md shadow-lg transition-transform transform hover:scale-105 hover:shadow-2xl')
                    
                    # Add a secondary button for "Cancel" or "Delete"
                    ui.button('Cancel', color='secondary').classes('text-lg font-semibold py-3 px-8 rounded-md').props('flat')


