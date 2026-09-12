import click
import os
import socket
import shutil

downloads_path = "/home/fre3d0m/Downloads"


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


@click.command()
def analyze() -> None:
    video_count = 0
    image_count = 0

    for file in os.listdir(downloads_path):
        if file.endswith(".mp4"):
            click.echo(f"Found: {file}")
            video_count += 1

        if file.endswith((".png", ".jpg", ".gif")):
            click.echo(f"Found: {file}")
            image_count += 1

    click.echo(f"Images found: {image_count}")
    click.echo(f"Videos found: {video_count}")
