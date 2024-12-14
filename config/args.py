import argparse

parser = argparse.ArgumentParser(description="Esta Herramienta permite ejecutar busquedas hacking en google o duckduck de manera automatica")
parser.add_argument('-q', '--query', type=str, help='Especifica el el dork que deseas buscar. .\nEjemplo: -q "filetype:sql "Mysql dump" (pass|password|passwd|pwd)"')
parser.add_argument('--start-page', type=int, default=1, help='Define la pagina de inicio del buscador para obtener los resultados')
parser.add_argument('--pages', type=int, default=1, help='Numero de Paginas de resultados de busqueda')
parser.add_argument('--lang', type=str, default='lang_es', help='Idioma de los resultados de la busqueda, por defecto es español')

args = parser.parse_args()