from nicegui import ui

def show_footer():
    ui.add_head_html('<script src="https://kit.fontawesome.com/a4861baa7d.js" crossorigin="anonymous"></script>')
    link_base = 'text-white text-sm font-semibold hover:text-blue-400 transition-colors duration-300 no-underline'

    # Overlay footer (controlled with z-index via classes 'front' and 'behind')
    with ui.element('footer').props('id=page-footer') \
        .classes('w-full bg-black text-white transition-all duration-300 ease-in-out shadow-xl front'):
        with ui.element('div').classes(
            'mx-auto max-w-7xl w-full px-6 py-6 '
            'flex flex-col md:flex-row items-center justify-between gap-6'
        ):
            with ui.row().classes('items-center gap-2'):
                # ui.icon('public').classes('text-white text-2xl')
                # ui.label('Stellar').classes('text-white text-xl font-bold')
                ui.icon('local_activity').classes('text-3xl text-[#f64209]')
                ui.label('Ste').classes('font-bold text-2xl text-white')
                ui.label('llar').classes('text-[#f64209] text-2xl font-semibold -ml-2')

            with ui.row().classes('gap-6'):
                # ui.link('Home', '/').classes(link_base)
                ui.label('© 2025 Stellar')
                
                # ui.link('Add Event', '/add_event').classes(link_base)
                # ui.link('Edit Event', '/edit_event').classes(link_base)
                # ui.link('View Event', '/view_event').classes(link_base)

            with ui.row().classes('gap-4'):
                ui.icon('public').classes('text-white cursor-pointer hover:text-blue-400')
                ui.icon('share').classes('text-white cursor-pointer hover:text-blue-400')
                ui.icon('mail').classes('text-white cursor-pointer hover:text-blue-400')
                # ui.html('<i class="fa-brands fa-facebook"></i>')
                

# Make content stack above footer and add bottom padding for when footer is in front
ui.query('body').classes('min-h-screen flex flex-col')
with ui.column().props('id=main-content').classes('relative z-10 flex-grow p-6 pb-28'):
    ui.label('Main content goes here')
    # ... more content

# Footer
show_footer()

# Styles to control stacking without shifting layout
ui.add_head_html('''
<style>
#page-footer.front  { z-index: 60; pointer-events: auto; opacity: 1; }
#page-footer.behind { z-index: 0;  pointer-events: none; opacity: .85; }
</style>
''')

# JS: send footer behind content when scrolling down; bring to front when scrolling up
ui.add_head_html('''
<script>
let lastScroll = 0;
window.addEventListener('scroll', () => {
  const footer = document.getElementById('page-footer');
  const current = window.pageYOffset || document.documentElement.scrollTop;
  const goingDown = current > lastScroll;
  if (goingDown) {
    footer.classList.add('behind');
    footer.classList.remove('front');
  } else {
    footer.classList.add('front');
    footer.classList.remove('behind');
  }
  lastScroll = current <= 0 ? 0 : current;
});
</script>
''')

