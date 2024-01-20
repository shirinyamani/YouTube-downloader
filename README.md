![logo](./img/logo.jpg)

Welcome to the YouTube Downloader Project! In this project, you will develop a Python application that allows users to download YouTube videos for offline viewing. Your mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the pytube library, user input handling, and feedback mechanisms such as a download progress bar.

Users should be able to run YouTube Downloader from the command line or used as a module in other Python scripts. Here are the basic steps to use the tool:

```Python
python youtube_downloader.py <youtube-url> <video-quality> <output-directory>
```

You can also use argparse to parse the command line arguments. The following is an example of how to use argparse to parse the command line arguments:

```Python
python youtube_downloader.py --url <youtube-url> --quality <video-quality> --output <output-directory>
```

## Requirements
Run the following command to install the required packages:

```Python
pip install -r requirements.txt
```

## More about `pytube`
We used the `pytube` library for this project, which is a Python library for interfacing with YouTube content. It allows you to query for metadata about videos, streams, and playlists; as well as download video and audio streams.

To learn more about pytube, you can explore the official documentation and this [repo](https://github.com/pytube/pytube/tree/master). It will guide you through the process of using pytube and help you implement the required features for the project.

