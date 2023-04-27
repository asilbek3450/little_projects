import instaloader
# save images to image file

username = "mirolimov.1"
bot1 = instaloader.Instaloader(dirname_pattern=f"image/{username}")

print(bot1.download_profile(username, profile_pic_only=True, download_stories=True))
