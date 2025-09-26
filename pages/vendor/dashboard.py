from nicegui import ui
from components.sidebar import show_sidebar
from datetime import datetime
import requests
from utils.api import base_url

events = [
    {
        'image': '/assets/CD1.jpeg',
        'title': 'Ako Adjei Lit Up 4.0',
        'date': 'Fri, Sep 26. 6PM - Sat 12AM',
        'location': 'Kukun, Accra',
        'price': 'Free',
        'tag': None,
    },
    {
        'image': '/assets/CD4.png',
        'title': 'Afro Flavors Food Festival 25',
        'date': 'Sun, Sep 14. 11AM - 9PM',
        'location': 'Ghud Park, Accra',
        'price': 'Free',
        'tag': None,
    },
    {
        'image': '/assets/CD6.jpg',
        'title': 'DETTY DEN HOUSE PARTY',
        'date': 'Sat, Sep 13. 7:30PM - Sun 2:45AM',
        'location': 'Oyibi, Greater Accra Region, Ghana, Oyibi',
        'price': 'RSVP',
        'tag': None,
    },
    {
        'image': '/assets/CD8.jpeg',
        'title': 'CUPS AND ARTS FESTIVAL',
        'date': 'Sat, Dec 6. 10AM - Sun 2:30AM',
        'location': "Afro's Event, Accra",
        'price': 'Paid',
        'tag': None,
    },
]

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
    
        username = ('Vera')  # TODO: Replace with dynamic user/session in production
    
        ui.query(".nicegui-content").classes("m-0 p-0")

    # Mock data — replace with DB/API calls later
        total_tickets = 347
        total_categories = 7

        with ui.row().classes("w-full h-full  flex-nowrap"):
        # Sidebar (Left)
            with ui.column().classes("w-[20%] h-full fixed"):
                show_sidebar()

        # Main content (Right)
        with ui.column().classes("w-full pl-[25%] p-10 overflow-y-auto bg-gray-50"): 

            # Time-based Greeting
            greeting_message = get_time_based_greeting(username)
            ui.label(greeting_message) \
                .classes('text-5xl font-extrabold text-[#1E1B4B]')

            # Section Subtitle
            ui.label('Create your first event') \
                .classes('text-2xl font-semibold text-[#4B5563] mt-2 mb-12')

            #  Wrap each Card + KPI in a column, then place columns in row
            with ui.row().classes('gap-8 flex-nowrap w-full'):

                # COLUMN 1: Scratch Card + Tickets KPI
                with ui.column().classes('items-center gap-4'):
                    # Card 1: Start from scratch
                    with ui.card().classes(
                        (
                            'flex flex-col justify-between p-6 rounded-xl bg-[#FFF1F0] w-full max-w-md '
                            'hover:shadow-lg hover:scale-105 transition-all duration-300 cursor-pointer group'
                        )
                    ).on('click', lambda: ui.navigate.to('/vendor/add_event')):

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
                    with ui.card().classes('bg-white p-5 rounded-xl shadow-sm border border-gray-100 w-full text-center'):
                        ui.icon('sell').classes('text-4xl text-[#f55c2b] mx-auto mb-3 ml-80')
                        ui.label(f'{total_categories}').classes('text-3xl font-bold text-gray-800')
                        ui.label('Ticket Categories').classes('text-gray-500 mt-1')

            with ui.element('section').classes('w-full py-10'):
                with ui.element('div').classes('mx-auto max-w-7xl w-full'):
                    ui.label('Events').classes('text-5xl font-semibold mb-8')

                    with ui.element('div').classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-10 mt-30'):
                        for idx, ev in enumerate(events):
                            # Original styling + view-stroke + clickable
                            with ui.element('div').classes(
                                'group bg-white rounded-xl shadow-md overflow-hidden '
                                'transition-all duration-300 hover:shadow-lg h-full flex flex-col relative '
                                'view-stroke cursor-pointer'
                            ).props('tabindex=0 role=link aria-label="View details"') as card:
                                card.on('click', lambda e, i=idx: ui.navigate.to(f'/event/{i}'))

                                # Image + optional tag
                                with ui.element('div').classes('relative h-40 w-full overflow-hidden'):
                                    ui.image(ev['image']).classes(
                                        'h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105'
                                    )
                                    if ev.get('tag'):
                                        ui.label(ev['tag']).classes(
                                            'absolute top-2 left-2 text-xs bg-red-100 text-red-600 font-semibold px-2 py-1 rounded-full'
                                        )

                                # Content (unchanged)
                                with ui.element('div').classes('p-4 flex flex-col gap-1 grow'):
                                    ui.label(ev['title']).classes('font-semibold text-md leading-snug')
                                    ui.label(ev['date']).classes('text-sm text-gray-600')
                                    with ui.element('div').classes('flex items-start gap-2 text-sm text-gray-600'):
                                        ui.icon('place').classes('text-gray-500 flex-shrink-0 mt-[2px]')
                                        ui.label(ev['location']).classes('flex-1 min-w-0 whitespace-normal break-words leading-snug')
                                    ui.label(ev['price']).classes('text-sm text-gray-800 font-semibold')   
                with ui.element('div').classes('w-full flex justify-end mt-10'):
                    ui.button('Load More')\
  .props("flat dense no-caps push ripple")\
  .classes("uppercase rounded-full px-10 py-4  text-white font-bold tracking-widest leading-tight mt-6 ml-auto text-center")\
  .style("background:#f64209; color:white; letter-spacing:0.15em; max-width:180px;")


