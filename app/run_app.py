"""Main entry point for the app."""
import settings
from app.finders import NLPFindersFactory
from app.input_readers import InputReaderFactory
from app.output_writers import OutputWriterFactory


def run_finder():
    """Try to find scam-like entities and write the result."""
    input_reader = InputReaderFactory.create_reader(settings.env.INPUT_TYPE)
    output_writer = OutputWriterFactory.create_writer(settings.env.INPUT_TYPE)

    finders = NLPFindersFactory()

    with output_writer:
        for text in input_reader.read_by_one():
            result = finders.find_first_in(text)

            output_writer.write(input_text=text, finder=result.finder, results=result.results)
