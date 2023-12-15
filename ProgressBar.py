class ProgressBar:
    # 下载进度条
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s...] %s %.2f %s %s %.2f %s"
        self.title = title
        self.count = count
        self.total = total
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.sep = sep

    def __get_info(self):
        _info = self.info % (
            self.title, self.status, self.count / self.chunk_size, self.unit, self.sep,
            self.total / self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = "\n"
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)

import requests
from contextlib import closing


def download(url, name=None):
    with closing(requests.request("GET", url, stream=True, verify=False)) as response:
        chunk_size = 1024
        x = response.headers
        content_size = int(response.headers.get('content-length'))
        progress = ProgressBar(name, total=content_size, unit="KB", chunk_size=chunk_size,
                               run_status="downloading", fin_status="download completed")
        with open(name, "wb") as fh:
            for data in response.iter_content(chunk_size=chunk_size):
                fh.write(data)
                progress.refresh(count=len(data))


if __name__ == "__main__":

    download("https://baidu.com", "index.html")
