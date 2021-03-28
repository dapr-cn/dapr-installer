import urllib.request
from invoke import task
import json
import os
import logging


@task
def sync_cli(c):
    base_dir = "../release/cli"
    release_json_path = f'{base_dir}/releases.json'
    urllib.request.urlretrieve("https://api.github.com/repos/dapr/cli/releases", filename=release_json_path)
    with open(release_json_path) as json_file:
        tags = json.load(json_file)

    for tag in tags:
        tag_dir = f"{base_dir}/{tag['tag_name']}"
        if not os.path.exists(tag_dir):
            os.makedirs(tag_dir)
        for asset in tag['assets']:
            asset_path = f"{tag_dir}/{asset['name']}"
            if not os.path.exists(asset_path):
                download_url = asset['browser_download_url']
                logging.info(f"start to request {download_url}")
                urllib.request.urlretrieve(download_url, filename=asset_path)
            else:
                logging.debug(f"skip to download {asset_path}")
