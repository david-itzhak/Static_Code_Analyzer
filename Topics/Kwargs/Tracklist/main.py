def tracklist(**artists):
    for artist, albums in artists.items():
        print(artist)
        for album, music_trak in albums.items():
            print(f'ALBUM: {album} TRACK: {music_trak}')

