import click


@click.command()
@click.option('--host', default='127.0.0.1', help='host wfAPI host.')
@click.option('--port', default=4302, help='gmAPI server port.')
@click.option('--workers', default=2, help='gmAPI server workers.')
@click.option('--log', default='logs/server.log', help='log file for app.')
def cli(host, port, log, workers):
    """Run the server with options."""


def main():
    """Main function."""
    cli()


if __name__ == '__main__':
    main()
