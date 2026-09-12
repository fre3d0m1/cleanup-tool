import os

downloads_path = "/home/fre3d0m/Downloads"
pictures_path = "/home/fre3d0m/Pictures"
videos_path = "/home/fre3d0m/Videos"

for file in os.listdir(downloads_path):
    if file.endswith(".mp4"):
        print(f"Moving: {file}")
        os.rename(f"{downloads_path}/{file}", f"{videos_path}/{file}")

    if file.endswith((".png", ".jpg", ".gif")):
        print(f"Moving: {file}")
        os.rename(f"{downloads_path}/{file}", f"{pictures_path}/{file}")
