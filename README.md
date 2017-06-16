# PyGradle JSON-LD CLI tool

Example of of building a CLI tool for applying a JSON-LD frame on RDF data (RDF needs to be serialised as turtle).

To Do:
* write tests
* generate documentation from source code

## Building and Running the application

### Requirements
1. Python 2.7
2. Gradle 3.0+ https://gradle.org/
3. Pypi Ivy repository either a local one (see https://github.com/linkedin/pygradle/blob/master/docs/pivy-importer.md for more information) or you can deploy your own version using https://github.com/blankdots/ivy-pypi-repo


### Building the application

After all the requirements are satisfied in the root directory run `gradle build`

### Running the application

To use the deployable artifact after build run `./build/deployable/bin/ldframe --frame=tests/resources/frame.jsonld --data=tests/resources/library.ttl`

To deploy the artifact on your a server unzip `build/distributions/pygradle-jsonld-cli-1.0.tar.gz` on one's server and run using `./ldframe`. CLI options:

* `--frame FILENAME`  Location of JSON-LD frame
* `--data FILENAME`   Location of the RDF file
* `--output TEXT`     File name for output. Default is `output.jsonld`
* `--help`            Show this message and exit.
