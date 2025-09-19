from nicegui import ui

def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-0")

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

                  ui.html("Africa's most trusted online advert partner since 2025. Discover and book events with ease, while<br>while empowering creators to sell and manage with ease.") \
                    .classes("text-white text-xl text-left leading-tight mt-2")

                  ui.button("CREATE EVENT", on_click=lambda: ui.navigate.to("/add_event")) \
                    .classes("uppercase rounded-full px-5 py-3 font-bold tracking-widest leading-tight mt-6") \
                    .style("letter-spacing: 0.15em;") \
                    .props("color=orange text-color=white push ripple")
                  

                  # Grey lines between columns
                  with ui.row().classes("w-full text-white justify-between flex-nowrap pt-10 mb-0 divide-x divide-gray-500/40"):
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
                            


