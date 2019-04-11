import ffmpeg
path = "D:\\Testing\\OneFile\\"
song = "4 Minutes - Madonna & Justin Timberlake & Timbaland.cdg"
def manFile():
    path = "D:\\Testing\\OneFile\\"
    song = "4 Minutes - Madonna & Justin Timberlake & Timbaland.cdg"
    in_file = ffmpeg.input(path + song)
    (
        ffmpeg
        .trim(start_frame=10, end_frame=20)
        .output('out.mp4')
        .run()
    )
def conFile():
    mylogo = ffmpeg.input("lymlogo.png")
    #mylogo = ffmepg.scale(mylogo,w=)
    (
        ffmpeg
        .input(path + song)
        .drawbox(t="fill",replace=1,color="black",enable='between(t,0,5)',x=0,y=0,width=1280,height=720)
        .overlay(mylogo,enable='between(t,0,5)')
        .filter("fps", fps=25, round="up")
        .output("out.cdg")
        .run()
    )
conFile()
