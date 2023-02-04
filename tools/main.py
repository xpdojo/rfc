import requests
from rfc2html import markup


def main(serial_number: int) -> None:
    """
    Download RFC txt and convert it to HTML.

    :param serial_number: RFC number
    :return:
    """
    rfc_name = f'rfc{serial_number}'
    text = requests.get(f"https://www.rfc-editor.org/rfc/{rfc_name}.txt").text

    txt_file_name = f'{rfc_name}.txt'
    with open(txt_file_name, 'w') as f:
        f.write(text)

    html = markup(text)
    html_file_name = f'{rfc_name}.html'
    with open(html_file_name, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    Bulk Indexing Oracle data to Elasticsearch
    """)
    parser.add_argument('-sn', '--serial-number', metavar='<int>', required=True,
                        default=None, type=int,
                        help='RFC serial number')

    args = parser.parse_args()
    main(serial_number=args.serial_number)
