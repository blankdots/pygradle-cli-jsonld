import json
import click
from pyld import jsonld
from ldframe.utils.logs import app_logger
from rdflib import ConjunctiveGraph


@click.command()
@click.option('--frame', help='Location of JSON-LD frame', type=click.File('rb'))
@click.option('--data', help='Location of the RDF file', type=click.File('rb'))
@click.option('--output', help='File name for output. Default is `output.jsonld`', default="output.jsonld")
def cli(frame, data, output):
    """Run the server with options."""
    output_file = open(output, 'w')
    graph_data = data.read()
    frame_data = frame.read()
    output_file.write(create_jsonLD(graph_data, frame_data))


def create_jsonLD(graph_data, filter_frame):
    """Create JSON-LD output for the given subject."""
    graph = ConjunctiveGraph()
    graph.parse(data=graph_data, format="turtle")
    try:
        # pyld likes nquads, by default
        expanded = jsonld.from_rdf(graph.serialize(format="nquads"))
        framed = jsonld.frame(expanded, json.loads(filter_frame))
        result = json.dumps(framed, indent=1, sort_keys=True)
        app_logger.info('Serialized as JSON-LD compact with the frame.')
        return result
    except Exception as error:
        app_logger.error('JSON-LD frame failed with error: {0}'.format(error))
        return error


def main():
    """Main function."""
    cli()


if __name__ == '__main__':
    main()
