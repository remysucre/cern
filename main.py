#!/usr/bin/env python3
"""
Crawl the CERN WWW project page, convert all reachable pages to markdown,
and update links to use absolute cern.la URLs.
"""

import re
import sys
from urllib.parse import urljoin, urlparse
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from markitdown import MarkItDown

TARGET_DOMAIN = "https://cern.la"
CERN_DOMAIN = "info.cern.ch"


def get_all_links(url, base_url):
    """Extract all links from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        links = set()
        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            full_url = urljoin(url, href)

            parsed_base = urlparse(base_url)
            parsed_url = urlparse(full_url)

            if (parsed_url.netloc == parsed_base.netloc and
                parsed_url.path.startswith('/hypertext/')):
                links.add(full_url)

        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return set()


def crawl_site(start_url, max_pages=50):
    """Crawl the site starting from start_url and return all unique pages."""
    visited = set()
    to_visit = {start_url}
    all_pages = set()

    while to_visit and len(all_pages) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        print(f"Crawling: {url}")
        visited.add(url)
        all_pages.add(url)

        links = get_all_links(url, start_url)
        for link in links:
            if link not in visited:
                to_visit.add(link)

    return all_pages


def url_to_filepath(url):
    """Convert a URL to a file path preserving directory structure."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    if not path:
        path = 'index.html'

    if path.endswith('.html'):
        path = path[:-5] + '.md'
    else:
        path += '.md'

    return path


def url_to_cern_la_path(url):
    """Convert a CERN URL to a cern.la path."""
    parsed = urlparse(url)
    path = parsed.path

    if path.endswith('.html'):
        path = path[:-5] + '.md'

    return path


def download_and_convert(url, output_dir):
    """Download a page and convert it to markdown."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        temp_html = output_dir / 'temp.html'
        temp_html.write_bytes(response.content)

        md = MarkItDown()
        result = md.convert(str(temp_html))

        temp_html.unlink()

        filepath = url_to_filepath(url)
        output_file = output_dir / filepath
        output_file.parent.mkdir(parents=True, exist_ok=True)

        markdown_content = f"# {url}\n\n{result.text_content}"
        output_file.write_text(markdown_content)
        print(f"Converted: {url} -> {filepath}")

        return True
    except Exception as e:
        print(f"Error converting {url}: {e}", file=sys.stderr)
        return False


def fix_links_in_file(filepath, pages_dir):
    """Update all links in a markdown file to use absolute cern.la URLs."""
    with open(filepath, 'r') as f:
        content = f.read()

    first_line = content.split('\n')[0]
    if first_line.startswith('# http'):
        base_url = first_line[2:].strip()
    else:
        rel_path = filepath.relative_to(pages_dir)
        base_url = f"https://{CERN_DOMAIN}/{rel_path}".replace('.md', '.html')

    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    def replace_link(match):
        text = match.group(1)
        link = match.group(2)

        if link.startswith(TARGET_DOMAIN):
            return match.group(0)

        parsed = urlparse(link)
        if parsed.scheme in ('mailto', 'ftp', 'news', 'telnet', 'gopher'):
            return match.group(0)

        if link.startswith('http'):
            if CERN_DOMAIN not in link:
                return match.group(0)
            abs_url = link
        else:
            abs_url = urljoin(base_url, link)

        parsed_abs = urlparse(abs_url)
        if CERN_DOMAIN not in parsed_abs.netloc:
            return match.group(0)

        fragment = ''
        if '#' in abs_url:
            abs_url, fragment = abs_url.split('#', 1)
            fragment = '#' + fragment

        new_path = url_to_cern_la_path(abs_url)
        new_url = f"{TARGET_DOMAIN}{new_path}{fragment}"

        return f'[{text}]({new_url})'

    updated_content = re.sub(link_pattern, replace_link, content)

    with open(filepath, 'w') as f:
        f.write(updated_content)

    return content != updated_content


def fix_all_links(pages_dir):
    """Fix links in all markdown files."""
    print("\nUpdating links to absolute cern.la URLs...")
    updated_count = 0

    for md_file in sorted(pages_dir.rglob('*.md')):
        rel_path = md_file.relative_to(pages_dir)
        if fix_links_in_file(md_file, pages_dir):
            print(f"Fixed links: {rel_path}")
            updated_count += 1

    print(f"{updated_count} files had links updated")


def main():
    start_url = "https://info.cern.ch/hypertext/WWW/TheProject.html"
    output_dir = Path(__file__).parent.resolve()

    print("Starting crawl...")
    pages = crawl_site(start_url)

    print(f"\nFound {len(pages)} pages. Converting to markdown...")

    success_count = 0
    for url in sorted(pages):
        if download_and_convert(url, output_dir):
            success_count += 1

    print(f"\nConversion complete: {success_count}/{len(pages)} pages successfully converted")

    fix_all_links(output_dir)

    print(f"\nOutput directory: {output_dir}")


if __name__ == "__main__":
    main()
