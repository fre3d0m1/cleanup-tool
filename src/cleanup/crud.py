import click
import os
import socket
import shutil

from pathlib import Path

DOWNLOADS_PATH = Path.home() / "Downloads"
VIDEOS_PATH = Path.home() / "Videos"
PICTURES_PATH = Path.home() / "Pictures"

CONFIG_DIR = Path.home() / ".config" / "cleanup-tool"
CONFIG_FILE = CONFIG_DIR / "config.json"

VIDEO_EXTS = (".mp4", ".mov")
IMAGE_EXTS = (".png", ".jpg", ".gif")


@click.command()
def stats() -> None:
    click.echo(f"Hostname: {socket.gethostname()}")

    usage = shutil.disk_usage(".")

    total_gb = usage.total / (1024**3)
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)

    click.echo(f"Total: {total_gb:.2f} GB")
    click.echo(f"Used: {used_gb:.2f} GB")
    click.echo(f"Free: {free_gb:.2f} GB")


def get_files(path) -> list:
    return os.listdir(path)


def keep_images(files: list) -> list:
    images = []
    for file in files:
        if file.endswith(IMAGE_EXTS):
            print(f"Found: {file}")
            images.append(file)
    return images


def keep_videos(files: list) -> list:
    videos = []
    for file in files:
        if file.endswith(VIDEO_EXTS):
            print(f"Found: {file}")
            videos.append(file)
    return videos


def move_videos(videos: list) -> None:
    for video in videos:
        click.echo(f"Moving: {video}")
        os.rename(f"{DOWNLOADS_PATH}/{video}", f"{VIDEOS_PATH}/{video}")


def move_images(images: list) -> None:
    for image in images:
        click.echo(f"Moving: {image}")
        os.rename(f"{DOWNLOADS_PATH}/{image}", f"{PICTURES_PATH}/{image}")


@click.command()
def analyze() -> None:
    videos: list = keep_videos(get_files(DOWNLOADS_PATH))
    images: list = keep_images(get_files(DOWNLOADS_PATH))

    click.echo(f"Images found: {len(images)}")
    click.echo(f"Videos found: {len(videos)}")


@click.command()
def basic_organize() -> None:

    videos: list = keep_videos(get_files(DOWNLOADS_PATH))
    images: list = keep_images(get_files(DOWNLOADS_PATH))

    if click.confirm("Are you sure you want to move these files?", abort=True):
        move_videos(videos)
        move_images(images)
