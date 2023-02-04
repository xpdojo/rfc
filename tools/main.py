import re

import requests
from markdownify import markdownify as md
from rfc2html import markup


def main(
        serial_number: int,
        output_directory: str,
        to: str,
) -> None:

    rfc_name = f'rfc{serial_number}'
    text = requests.get(f"https://www.ietf.org/rfc/{rfc_name}.txt").text
    reformat = re.sub(r'(?<=[a-z., ]{2})\n(?!\n)', '', text)  # Remove single line breaks

    if to == "txt":
        with open(f'{output_directory}/{rfc_name}.txt', 'w') as f:
            f.write(reformat)
        return

    html = markup(reformat)
    if to == "html":
        with open(f'{output_directory}/{rfc_name}.html', 'w') as f:
            f.write(html)
        return

    print('test')
    if to == "markdown":
        with open(f'{output_directory}/{rfc_name}.md', 'w') as f:
            f.write(md(html))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    Download RFC txt and convert it to other format.
    """)
    parser.add_argument('-sn', '--serial-number', metavar='<int>', required=True,
                        default=None, type=int,
                        help='RFC serial number')
    parser.add_argument('-o', '--output-directory', metavar='<str>', required=False,
                        default='.', type=str,
                        help='Output directory')
    parser.add_argument('-t', '--to', metavar='<str>', required=False,
                        default='txt', type=str,
                        help='Output format')

    args = parser.parse_args()
    main(
        serial_number=args.serial_number,
        output_directory=args.output_directory,
        to=args.to,
    )
