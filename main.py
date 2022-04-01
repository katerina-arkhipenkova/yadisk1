import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_link(self, disk_file_path: str):
        disk_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(disk_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, filename: str):
        href = self.upload_link(disk_file_path=filename).get("href", "")
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print('success')
        else:
            print('error')


if __name__ == '__main__':
    path_to_file = 'text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_link(path_to_file)
    uploader.upload_file_to_disk(path_to_file)