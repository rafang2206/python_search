import json
from rich.console import Console
from rich.table import Table

class ResultsParser:
    def __init__(self, results):
        self.results = results


    def export_html(self, out_file):
        with open('html_template.html', 'r', encoding='utf-8') as f:
            template = f.read()

        html_elements = ''

        for index, data in enumerate(self.results, start=1):
            element = f'<div class="resultados">' \
                        f'<div class="indice"> Resultado {index} </div>' \
                        f'<h5>{data['title']}</h5>' \
                        f'<p>{data['description']}</p>' \
                        f'<a href="{data['link']}" target="_blank">{data['link']}</a>' \
                        f'</div>'
            html_elements += element
        
        inform = template.replace('{{ resultados }}', html_elements)

        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(inform)

        self.export_json('google.json')
        self.show_screen()
        print(f'Resultados exportados a html. fichero creado {out_file}')

    def export_json(self, out_file):
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print('Resultados exportados a JSON')

    def show_screen(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("#", style="dim")
        table.add_column("Title", width=50)
        table.add_column("Description")
        table.add_column("Link")

        for index, result in enumerate(self.results, start=1):
            table.add_row(str(index), result['title'], result['description'], result['link'])
            table.add_row("-----", "-----", "-----", "-----")
        
        console.print(table)