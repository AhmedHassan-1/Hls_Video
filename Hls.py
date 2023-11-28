import ffmpeg
import os
import argparse


parser = argparse.ArgumentParser(description="Hls_Video")
parser.add_argument(
    "-i",
    "--Video_Input",
    type=str,
    help="Video will be copied to make it Hls",
    required=True,
)
parser.add_argument(
    "-dir",
    "--directory",
    type=str,
    help="your directory for output",
    required=False,
    default=os.getcwd(),
)
parser.add_argument(
    "-n",
    "-name",
    "--Name",
    type=str,
    help="file name",
    required=False,
    default="output",
)
parser.add_argument(
    "-t", "-time", "--Time", type=int, help="time for each video", required=True
)
parser.add_argument(
    "-e",
    "-extension",
    "--Extension",
    type=str,
    help="default : ts",
    required=False,
    default="ts",
)
parser.add_argument(
    "-l",
    "-log",
    "--Log",
    help="mangment log ",
    choices=[
        "quiet",
        "panic",
        "fatal",
        "error",
        "warning",
        "info",
        "verbose",
        "debug",
        "trace",
    ],
    default="info",
    type=str,
    required=False,
)
args = parser.parse_args()
try:
    ffmpeg.input(args.Video_Input).output(
        f"{args.directory}/{args.Name}.m3u8",
        start_number=1,
        hls_time=args.Time,
        hls_list_size=0,
        hls_segment_filename=f"{args.directory}/{args.Name}_%03d.{args.Extension}",
        loglevel=args.Log,
    ).run()
except:
    print("We have an error in ffmpeg config , please try agian with another data")

"""
loglevel_Values=
"quiet"
"panic"
"fatal"
"error"
"warning"
"info"
"verbose"
"debug"
"trace"
"""
