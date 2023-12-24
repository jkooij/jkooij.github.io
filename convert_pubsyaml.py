import yaml
import os
import textwrap

inp_path = 'allpubs.yml'
out_dir = '_publications/'
screenshot_path_patterns = (
    'files/publications/{key}.png',
    'files/publications/{key}.jpg',
    'files/publications/{key}.gif',
)

# load yaml file
with open(inp_path, 'r') as file:
    pubs = yaml.load(file, Loader=yaml.Loader)

# add ordering field to publications, as they appear in the souce yml file
for j, pub in enumerate(reversed(pubs)):
    pub['_order'] = j

# find screenshots
for pub in pubs:
    for screenshot_path_pattern in screenshot_path_patterns:
        screenshot_path = screenshot_path_pattern.format(key=pub['key'])
        if os.path.isfile(screenshot_path):
            pub['screenshot'] = screenshot_path
            continue


# list all used fields
fields = [
    'key',
    'title',
    'year',
    'authors',
    'booktitle',
    'publisher',
    'journal',
    'volume',
    'number',
    'pages',
    'puburl',
    'video',
    'arxiv',
    'code',
    'project',
    'open_access',
    'doi',
    'note',
]

def pub_to_bibtex(pub):
    if 'journal' in pub:
        pubtype = 'article'
        fields = ('title', 'author', 'journal', 'volume', 'number', 'pages', 'year', 'publisher', 'puburl', 'doi')
    else:
        pubtype = 'inproceedings'
        fields = ('title', 'author', 'booktitle', 'pages', 'year', 'publisher', 'puburl', 'doi')

    bibtex = '@' + pubtype + '{' + pub['key'] + ',\n'
    for field in fields:
        if not field in pub: continue
        value = pub[field]
        if field == 'title':
            value = '{' + value + '}'
        value = str(value)
        bibtex += '    ' + field + '={' + value + '},\n'
    bibtex += '}\n'
    return bibtex

def pub_to_video(pub):
    if not 'video' in pub:
        return None

    link = pub['video']
    return f'<iframe width="560" height="315" src="{link}" title="video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

def pub_to_markdown_page(pub):
    title = pub.get('title', '')
    year = pub.get('year', '')
    authors = pub.get('authors', '')
    doi = pub.get('doi', '')
    journal = pub.get('journal', '')
    booktitle = pub.get('booktitle', '')
    screenshot = pub.get('screenshot', '')
    bibtex = pub_to_bibtex(pub)
    video = pub_to_video(pub)

    showfields = [
        ('Authors', authors),
        ('Journal', journal),
        ('Proceedings', booktitle),
        ('Year', year),
        ('DOI', doi),
    ]

    content = ''

    for k, v in showfields:
        if not v: continue
        content += f' - {k}: {v}\n'
    content += '\n'

    if screenshot:
        content += f'<img class="screenshot" src="../../{screenshot}" alt="{title}" />\n'

    if video:
        content += '## Video\n\n' + video + '\n'

    content += '## Bibtex\n\n{% raw %}\n```bibtex\n' + bibtex + '\n```\n{% endraw %}\n'

    return content

# generate list of publications
for pub in reversed(pubs):
    # create file content
    content = '---\n'
    content += yaml.dump(pub)
    content += '---\n'
    content += '\n'
    #content += pub_to_markdown_page(pub)

    key = pub['key']
    out_path = out_dir + '{year}_{key}.md'.format(**pub)
    print(out_path)

    with open(out_path, 'w') as file:
        file.write(content)

print(f'Converted {len(pubs)} publications')
