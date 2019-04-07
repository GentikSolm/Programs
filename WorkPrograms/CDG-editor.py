import ffmpeg
path = "D:\\Testing\\OneFile\\"
song = "4 Minutes - Madonna & Justin Timberlake & Timbaland"
in_file = ffmpeg.input('input.mp4')
overlay_file = ffmpeg.input(path + song)
(
    ffmpeg
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .output('out.mp4')
    .run()
)
