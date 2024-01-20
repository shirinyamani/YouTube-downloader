import argparse
from pathlib import Path

import pytube
from pytube import YouTube
from tqdm import tqdm
from pytube.exceptions import VideoUnavailable, RegexMatchError


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
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print('Video Unavaiable!')
            return 
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
            
        self.pbar = tqdm(desc=':): Downloading...', 
                        total = stream.filesize,
                        unit= 'B',
                        unit_scale= True)
        
        stream.download(self.output_save_path)
    
    
    def on_progress(self,stream, chunk, byte_remaining):
        current = stream.filesize - byte_remaining
        self.pbar.update(current - self.pbar.n)


    def complete(self, stream, filepath):
        pass
        #print(f'Download completed and saved in {filepath}')
        
        

if __name__ == "__main__":
        parser = argparse.ArgumentParser(
        description= 'Youtube Downloader'
        )

        parser.add_argument('url',help='youtube video URL')
        parser.add_argument('-q','--quality', help='enter your desired quality', default='highest')
        parser.add_argument('-o','--output_save_path', help='path for video', default=None)

        args = parser.parse_args()
    
        YouTubeDownloader(
             url=args.url,
             quality=args.quality,
             output_save_path=args.output_save_path
        ).download()