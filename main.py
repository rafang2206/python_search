from dorks.ninjaDorks import main
from config.args import args
import sys

if not args.query  :
    print('Debes especificar una query')
    sys.exit(1)


main(
    args.query, 
    args.start_page, 
    args.pages, 
    args.lang
)