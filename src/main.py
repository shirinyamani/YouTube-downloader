from pathlib import Path

import pytube
from pytube import YouTube


class YouTubeDownloader:
    def __init__(self, url, output_save_path= None, quality=None):
        self.url = url
        self.output_save_path = output_save_path or Path.cwd()
        self.quality = quality or 'highest'
        self.yt = YouTube(
            self.url, 
            on_progress_callback=self.on_progress,
            on_complete_callback=self.complete)


    def download(self):
        if self.quality == 'highest':
            stream = self.yt.streams.filter(
                progressive=True, 
                file_extension='mp4'
                ).get_highest_resolution()
        else:
            stream = self.yt.streams.filter(
                progressive=True, 
                file_extension='mp4', 
                res=self.quality).first()
        
        stream.download(self.output_save_path)

    def on_progress(self,stream, chunk, byte_remaining):
        total_size = stream.filesize
        byte_downloaded = total_size - byte_remaining
        print(f'downloading...{byte_downloaded/total_size*100:.2f} % of {stream.title}')

    def complete(self, stream, filepath):
        total_size = stream.filesize / 1024 /1024
        print()
        print(f'TotalSize of {total_size:.2f} MB download completed. file saved to: {filepath}')


        
