import click

@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
@click.option('--stock', prompt='Add stock:', help='Enter the stock symbol to monitor for news updates.')
def add_stock(stock):
    """Simple program that greets NAME for a total of COUNT times."""
    print(f'adding: {stock}')

if __name__ == '__main__':
    add_stock()

#python cli.py --stock=ESI:CT