import os
import requests


async def download_file_on_disc(url, path, file_name, file_type):

    base_path = './data/secret_agency_evidence/{}'.format(path)

    if file_type == 'exe' or file_name == 'js':
        return
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
    }
    r = requests.get(url, headers=headers, stream=True)
    full_file_path = '{}/{}.{}'.format(base_path, file_name, file_type)

    with open(full_file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return full_file_path
