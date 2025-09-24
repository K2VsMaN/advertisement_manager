from nicegui import ui
from components.sidebar import show_sidebar
from datetime import datetime


def get_time_based_greeting(name: str) -> str:
    hour = datetime.now().hour
    if hour < 12:
        part = "Good Morning"
    elif hour < 17:
        part = "Good Afternoon"
    else:
        part = "Good Evening"
    return f"{part}, {name}"


@ui.page("/vendor/dashboard")
def show_vendor_dashboard():
    ui.query(".nicegui-content").classes("m-0 p-0")
    username = "Nathan"  # TODO: Replace with dynamic user/session in production

    # Mock data — replace with DB/API calls later
    total_tickets = 347
    total_categories = 18

    with ui.row().classes("w-full h-full mt-10"):
        # Sidebar (Left)
        with ui.column().classes("w-[20%] h-full"):
            show_sidebar()

        # Main content (Right)
        with ui.column().classes("w-[80%] p-10 overflow-y-auto"):

            # Time-based Greeting
            greeting_message = get_time_based_greeting(username)
            ui.label(greeting_message) \
                .classes('text-5xl font-extrabold text-[#1E1B4B] ml-24')

            # Section Subtitle
            ui.label('Create your first event') \
                .classes('text-2xl font-semibold text-[#4B5563] mt-2 mb-12 ml-24')

            #  Wrap each Card + KPI in a column, then place columns in row
            with ui.row().classes('gap-8 justify-center flex-wrap w-full'):

                # COLUMN 1: Scratch Card + Tickets KPI
                with ui.column().classes('items-center gap-4'):
                    # Card 1: Start from scratch
                    with ui.card().classes(
                        (
                            'flex flex-col justify-between p-6 rounded-xl bg-[#FFF1F0] w-full max-w-md '
                            'hover:shadow-lg hover:scale-105 transition-all duration-300 cursor-pointer group'
                        )
                    ).on('click', lambda: ui.navigate.to('/vendor/create-scratch')):

                        ui.image('assets/SH.png') \
                            .classes('rounded-lg mb-6 object-cover w-full h-40')

                        ui.label('Start from scratch') \
                            .classes('text-xl font-semibold text-[#111827] mb-2 group-hover:text-[#D97706] transition-colors')

                        ui.label("Craft every detail — from ticket types to reserved seating and advanced tools.") \
                            .classes('text-[#6B7280] text-sm leading-relaxed mb-4')

                        with ui.row().classes('items-center gap-2 mt-auto'):
                            ui.icon('edit_note').classes('text-[#D97706] text-2xl group-hover:scale-110 transition-transform')
                            ui.label('Build manually').classes('text-[#D97706] font-medium')

                    # ➕ KPI Stat below: Total Tickets
                    with ui.card().classes('bg-white p-5 rounded-xl shadow-sm border border-gray-100 w-full'):
                        ui.icon('confirmation_number').classes('text-4xl text-[#f55c2b] items-end ml-80')
                        ui.label(f'{total_tickets:,}').classes('text-3xl font-bold text-gray-800')
                        ui.label('Tickets Sold').classes('text-gray-500 mt-1')

                # COLUMN 2: AI Card + Categories KPI
                with ui.column().classes('items-center gap-4'):
                    # Card 2: Create faster with AI
                    with ui.card().classes(
                        'flex flex-col justify-between p-5 rounded-xl bg-[#F1F5FF] w-full max-w-md '
                        'hover:shadow-lg hover:scale-105 transition-all duration-300 cursor-pointer group'
                    ).on('click', lambda: ui.navigate.to('/vendor/create-ai')):

                        ui.image('assets/AI_1.png') \
                            .classes('rounded-lg mb-6 object-cover w-full h-40')

                        ui.label('Create faster with AI') \
                            .classes('text-xl font-semibold text-[#111827] mb-2 group-hover:text-[#3B82F6] transition-colors')

                        ui.label("Answer a few questions to generate a publish-ready event in minutes.") \
                            .classes('text-[#6B7280] text-sm leading-relaxed mb-4')

                        with ui.row().classes('items-center gap-2 mt-auto'):
                            ui.icon('auto_awesome').classes('text-[#3B82F6] text-2xl group-hover:scale-110 transition-transform')
                            ui.label('Generate with AI').classes('text-[#3B82F6] font-medium')

                    #  KPI Stat below: Total Categories
                    with ui.card().classes('bg-white p-5 rounded-xl shadow-sm border border-gray-100 w-full max-w-md text-center'):
                        ui.icon('sell').classes('text-4xl text-[#f55c2b] mx-auto mb-3 ml-80')
                        ui.label(f'{total_categories}').classes('text-3xl font-bold text-gray-800')
                        ui.label('Ticket Categories').classes('text-gray-500 mt-1')
                    
