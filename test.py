import click
import textrank

@click.command()
@click.argument('filename')
def extract_phrases(filename):
    """Print key-phrases to stdout."""
    with open(filename) as f:
        phrases = textrank.extract_key_phrases(f.read())
        print(phrases)

if __name__ == '__main__':
    extract_phrases()
