import pyfiglet

font_list = []
for font in pyfiglet.FigletFont.getFonts():
    font_list.append(pyfiglet.figlet_format("Hello", font=font))
    with open('font_examples.txt', 'w') as file:
        file.write('\n'.join(font_list))
