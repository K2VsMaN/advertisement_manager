from nicegui import ui

def show_footer():
    ui.add_head_html('<script src="https://kit.fontawesome.com/a4861baa7d.js" crossorigin="anonymous"></script>')

    ui.add_head_html('''
    <style>
    #page-footer.front  { z-index: 60; pointer-events: auto; opacity: 1; }
    #page-footer.behind { z-index: 0;  pointer-events: none; opacity: .85; }
    </style>
    ''')

    ui.add_head_html('''
    <script>
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const footer = document.getElementById('page-footer');
      if (!footer) return;
      const current = window.pageYOffset || document.documentElement.scrollTop;
      const goingDown = current > lastScroll;
      footer.classList.toggle('behind', goingDown);
      footer.classList.toggle('front', !goingDown);
      lastScroll = current <= 0 ? 0 : current;
    });
    </script>
    ''')

    with ui.element('footer').props('id=page-footer') \
        .classes('w-full bg-black text-white shadow-xl front'):
        with ui.element('div').classes(
            'mx-auto max-w-7xl w-full px-6 py-6 flex flex-col md:flex-row items-center justify-between gap-6'
        ):
            with ui.row().classes('items-center gap-2'):
                ui.icon('local_activity').classes('text-3xl text-[#f64209]')
                ui.label('Ste').classes('font-bold text-2xl text-white')
                ui.label('llar').classes('text-[#f64209] text-2xl font-semibold -ml-2')

            ui.label('© 2025 Stellar').classes('text-sm')

            with ui.row().classes('gap-4'):
                ui.icon('public').classes('cursor-pointer')
                ui.icon('share').classes('cursor-pointer')
                ui.icon('mail').classes('cursor-pointer')
