from nicegui import ui
from components.sidebar import show_sidebar
from datetime import datetime  # Import for time-based greeting


# Optional helper function to get greeting based on current time
def get_time_based_greeting(name: str) -> str:
    hour = datetime.now().hour
    if hour < 12:
        part = "Good morning"
    elif hour < 17:
        part = "Good afternoon"
    else:
        part = "Good evening"
    return f"{part}, {name}"


@ui.page("/vendor/dashboard")
def show_vendor_dashboard():
    username = "Nathan"  #Replace this with actual session/user system if available

    with ui.row().classes("w-full"):
        # Sidebar column (20%)
        with ui.column().classes("w-[20%]"):
            show_sidebar()

        # Main content column (80%)
        with ui.column().classes("w-[80%]"):
            
            # Dynamic greeting message based on time of day
            greeting_message = get_time_based_greeting(username)
            ui.label(greeting_message) \
                .classes('text-5xl font-extrabold text-[#1E1B4B] mb-2')

            # Section subtitle
            ui.label('Create your first event') \
                .classes('text-2xl font-semibold text-[#4B5563] mb-10')

            # Two side-by-side cards
            with ui.row().classes('gap-8 w-full max-w-6xl'):

                # Card 1: Create faster with AI
                with ui.card().classes('flex flex-col justify-between p-6 rounded-xl bg-[#F1F5FF] w-full max-w-md'):
                    ui.image('assets/event-ai.png') \
                        .classes('rounded-lg mb-6 object-cover w-full h-auto')
                    
                    ui.label('Create faster with AI') \
                        .classes('text-xl font-semibold text-[#111827] mb-1')

                    ui.label("Answer a few questions to generate an event that’s\nready to publish in minutes") \
                        .classes('text-[#6B7280] leading-tight')

                    ui.icon('add_circle') \
                        .classes('text-[#D1D5DB] text-3xl mt-auto self-end')

                # Card 2: Start from scratch
                with ui.card().classes('flex flex-col justify-between p-6 rounded-xl bg-[#FFF1F0] w-full max-w-md'):
                    ui.image('assets/event-scratch.png') \
                        .classes('rounded-lg mb-6 object-cover w-full h-auto')

                    ui.label('Start from scratch') \
                        .classes('text-xl font-semibold text-[#111827] mb-1')

                    ui.label("Craft every detail from ticket types to reserved seating\nand more advanced tools") \
                        .classes('text-[#6B7280] leading-tight')

                    ui.icon('add_circle') \
                        .classes('text-[#D1D5DB] text-3xl mt-auto self-end')
