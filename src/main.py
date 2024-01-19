from pathlib import Path

import pytube
from pytube import YouTube
from tqdm import tqdm


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
            
        self.pbar = tqdm(desc='Downloading...', 
                         total = stream.filesize,
                         unit= 'B',
                         unit_scale= True)

        
        stream.download(self.output_save_path)

    def on_progress(self,stream, chunk, byte_remaining):
        current = stream.filesize - byte_remaining
        self.pbar.update(current - self.pbar.n)


    def complete(self, stream, filepath):
        print()
        print(f'Download completed and saved in {filepath}')
        
        

if __name__ == "__main__":
  
    url = input('Please Enter the URL of your desired video:')
    if "youtube.com" not in url:
        print('Invalid URL! Please Enter YOUTUBE link')
    
    else:
        YouTubeDownloader(url).download()
