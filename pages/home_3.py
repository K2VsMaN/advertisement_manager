from nicegui import ui

@ui.page('/')
def show_home_page_3():
    # Center the main content on the page
    with ui.column().classes('w-full flex justify-center items-center mx-auto max-w-7xl w-full px-6 mt-5'):
        with ui.row().classes('bg-[#ff4c06] rounded-[48px] max-w-[1500px] w-full px-12 py-14 items-center justify-between'):
            # Left side: text and download options
            with ui.column().classes('gap-y-0 flex-1'):
                ui.html('Trusted by the brands<br>and creators you love.').classes(
                    'font-bold text-white text-[3.2rem] md:text-[4rem] leading-tight mb-6'
                )
                ui.html(
                    'From <b>mega-festivals</b> to <b>intimate gatherings</b>, we power every event with passion<br>and expertise. '
                    'Discover and book your next experience anytime, anywhere—online,<br>offline, USSD, WhatsApp, or the Cityloop app!'
                ).classes('text-white text-lg mb-10').props('rich')

                with ui.row().classes('gap-6 mt-2 justify-center'):
                    # App Store
                    with ui.row().classes('bg-white rounded-full px-6 py-3 items-center gap-2 min-w-[140px] max-w-[200px]'):
                        ui.icon('apple').classes('text-black text-2xl')
                        with ui.column().classes('items-start'):
                            ui.label('Download on the').classes('text-xs text-black')
                            ui.label('App Store').classes('text-base font-bold text-black')
                    # Google Play
                    with ui.row().classes('bg-white rounded-full px-6 py-3 items-center gap-2 min-w-[140px] max-w-[200px]'):
                        ui.icon('android').classes('text-black text-2xl')
                        with ui.column().classes('items-start'):
                            ui.label('GET IT ON').classes('text-xs text-black')
                            ui.label('Google Play').classes('text-base font-bold text-black')
                    # USSD
                    with ui.row().classes('bg-white rounded-full px-6 py-3 items-center gap-2 min-w-[140px] max-w-[200px]'):
                        # ui.label('#').classes('text-black text-2xl font-bold')
                        with ui.column().classes('items-start'):
                            ui.label('DIAL').classes('text-xs text-black')
                            ui.label('*713*33#').classes('text-base font-bold text-black')
                    # WhatsApp
                    with ui.row().classes('bg-white rounded-full px-6 py-3 items-center gap-2 min-w-[140px] max-w-[200px]'):
                        # ui.icon('whatsapp').classes('text-[#25D366] text-2xl')
                        with ui.column().classes('items-start'):
                            ui.label('WHATSAPP').classes('text-xs text-black')
                            ui.label('0242426427').classes('text-base font-bold text-black')

            # Right side: QR code and download label (centered, expanded)
            with ui.column().classes('justify-center items-center flex-none ml-10 mt-5 h-full'):
                ui.image('/assets/QRCODE.png').classes('bg-white rounded-xl p-2 w-[300px] h-[300px] object-contain flex justify-center items-center')
                ui.label('Scan to download').classes('text-white font-bold text-xl mt-6 flex justify-center')

    with ui.element("section") \
        .classes("w-full h-80 flex justify-center items-center mx-auto max-w-7xl w-full px-6 mt-10 -mb-0") \
        .style('background-image: url("/assets/BRANDS.jpg"); background-size: contain; background-position: center; background-repeat: no-repeat;'):
        pass

with ui.row().classes('w-full max-w-7xl mx-auto items-center justify-between mt-8'):
    # Left side: text content
    with ui.column().classes('flex-1 pr-8'):
        ui.label('What creators are saying...').classes('text-[#ff4c06] font-bold text-xl mb-2')
        ui.label('When I think events, I\nalways think\neGotickets').classes(
            'font-extrabold text-[#222] text-[4rem] leading-tight mb-4'
        )
        ui.html('<span class="font-bold text-black">- Amma Aboagye</span> Founding curator of The Afropole').classes(
            'text-lg mt-6'
        )

    # Right side: video
    with ui.column().classes('items-center justify-center flex-none'):
        ui.video('/assets/eGotickets - Africa’s Top Events Platform — Book in Ghana, Nigeria, Kenya & Beyond.mp4').classes(
            'rounded-2xl shadow-xl w-[540px] h-[320px] object-cover'
        )
        