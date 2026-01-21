from nicegui import ui

def show_header():
    search_input = None
    with ui.header().classes("bg-black shadow-md flex justify-between items-center px-4"):
        
        with ui.row().classes('items-center gap-2'):
            ui.icon('local_activity').classes('text-3xl text-[#f64209]')
            ui.label('Ste').classes('font-bold text-2xl text-white')
            ui.label('llar').classes('text-[#f64209] text-2xl font-semibold -ml-2')

        with ui.element('div').classes('absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 hidden md:block'):
            with ui.row().classes('items-center bg-white/10 backdrop-blur-md border border-white/20 rounded-full px-4 py-1 w-[350px] flex-nowrap'):
                ui.icon('search').classes('text-white/60 text-lg')
                search_input = ui.input(placeholder='Search events...').props('borderless dense dark input-class="text-white"').classes('flex-1 ml-2 text-white')

        with ui.row().classes("items-center gap-4"):
            ui.button("Home", on_click=lambda: ui.navigate.to("/")).props("flat dense no-caps text-color=white")
            ui.button("Events", on_click=lambda: ui.navigate.to("/all_events")).props("flat dense no-caps text-color=white")
            ui.button("Login", on_click=lambda: ui.navigate.to("/vendor/signin")).props("flat dense no-caps text-color=white")
            ui.button("Sign Up", on_click=lambda: ui.navigate.to("/signup")).props("flat dense no-caps").classes("bg-[#f64209] text-white rounded-full px-6")
    return search_input

def show_home_page():
    search_input = show_header()
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")

    with ui.row().classes("h-screen w-full relative"):
         # Video background container
      ui.html(
              f"""
              <video autoplay loop muted class="-z-10 absolute insert-0 w-full h-full object-cover">
                <source src="/assets/HV.mp4" type="video/mp4">
            </video>
        """
         )
    # with ui.element("section") \
    #     .classes("relative w-full h-screen m-0 p-0 overflow-hidden") \
    #     .style('background-image: url("/assets/H3.jpg"); background-size: cover; background-position: center;'):
        
      ui.element("div").classes("absolute inset-0 bg-black/60")

      with ui.element("div").classes("absolute inset-0 z-10 flex flex-col justify-center items-start py-20 pl-12 md:pl-20 pr-6"):
                  ui.html('Find, book, and enjoy<br>events you love.') \
                    .classes("text-white text-7xl font-bold text-left leading-tight") \
                    .style("line-height:1.05;")

                  ui.html("Africa's most trusted online advert partner since 2025. Discover and book events with ease, while<br> empowering creators to sell and manage with ease.") \
                    .classes("text-white text-xl text-left leading-tight mt-2")

                  ui.button("GET TICKETS", on_click=lambda: ui.navigate.to("/all_events")) \
    .classes("uppercase rounded-full px-5 py-3 text-white font-bold tracking-widest leading-tight mt-6") \
    .style("background:#f64209; color:white; letter-spacing:0.15em;") \
    .props("flat dense no-caps push ripple")
                  

                  # Grey lines between columns
                  with ui.row().classes  ("w-full text-white justify-between flex-nowrap pt-10 mb-0 divide-x divide-gray-500/40"):
                            col = "w-full sm:w-1/2 lg:w-1/4 px-6 md:px-8"
                            with ui.column().classes(col):
                                ui.label("Event Power").classes("text-orange-500 font-bold text-3xl text-left")
                                ui.html("Creators across Africa trust us<br>to bring events to life.").classes("text-gray-300 leading-tight text-left")
                            with ui.column().classes(col):
                                ui.label("Creator First").classes("text-orange-500 font-bold text-3xl text-left")
                                ui.html("We’re the partner behind<br>thousands of successful events.").classes("text-gray-300 leading-tight text-left")
                            with ui.column().classes(col):
                                ui.label("Easy Payouts").classes("text-orange-500 font-bold text-3xl text-left")
                                ui.html("Fast, secure, stress-free earnings<br>— every time.").classes("text-gray-300 leading-tight text-left")
                            with ui.column().classes(col):
                                ui.label("Time-Tested").classes("text-orange-500 font-bold text-3xl text-left")
                                ui.html("Over a decade of building tools<br>that make events better.").classes("text-gray-300 leading-tight text-left")
    return search_input
                            
