import pytube

link = 'https://youtu.be/9WKV2emy5vk?si=qEU_f7dk8opaPG-j'
link = 'https://youtu.be/Qt66HAlva2A?si=FsiLkcdtq1YT0rAO'

yt = pytube.YouTube(link)
yt.streams.first().download()
print(f'Downloaded {link}')