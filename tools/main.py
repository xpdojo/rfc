import re

import requests
from markdownify import markdownify as md
from rfc2html import markup


def main(
        output_directory: str,
        serial_number: int,
) -> None:
    """
    Download RFC txt and convert it to HTML and Markdown.

    :param output_directory: Directory to save the RFC files.
    :param serial_number: RFC number
    """
    rfc_name = f'rfc{serial_number}'
    text = requests.get(f"https://www.rfc-editor.org/rfc/{rfc_name}.txt").text
    text1 = re.sub(r'(?<=[a-z., ]{2})\n(?!\n)', '', text)  # Remove single line breaks

    with open(f'{output_directory}/{rfc_name}.txt', 'w') as f:
        f.write(text1)

    html = markup(text1)
    with open(f'{output_directory}/{rfc_name}.html', 'w') as f:
        f.write(html)

    with open(f'{output_directory}/{rfc_name}.md', 'w') as f:
        f.write(md(html))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    Download RFC txt and convert it to HTML and Markdown.
    """)
    parser.add_argument('-o', '--output-directory', metavar='<str>', required=False,
                        default='.', type=str,
                        help='Output directory')
    parser.add_argument('-sn', '--serial-number', metavar='<int>', required=True,
                        default=None, type=int,
                        help='RFC serial number')

    args = parser.parse_args()
    main(
        output_directory=args.output_directory,
        serial_number=args.serial_number,
    )
