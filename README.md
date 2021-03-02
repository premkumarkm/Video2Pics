About

Video2Pics library which helps to convert video file into pictures / image with adjustable time frame.
The objective why I created this library is to ease the process of creating the video to pictures / image frames conversion process. We can generate picture / images of an video or a subpart of a video and that too custom frame capture rate and start / end time (in sec) of video.
How to install?
pip install Video2Pics

Requirements
It requires to be installed
•	Opencv2 and numpy


Class Object Argument Description

Argument	Description

video_srcpath	source path of the video
start_time	Default value is None i.e 0s will be considered

end_time	Default value is None i.e till end of duration will be
considered

frame_rate	No. of frames you want to capture per second.
For e.g if frame_rate= 15 then only first 15
frames will be captured out of input Frames per second

save_format	Output picture / image file extension. By default "jpg"

output_dir	Output directory for saving picture / images. If not specified
the source file path the pictures will be saved


Note:- The capture_rate if not specified will consider the original video frames per second rate
Frame Capture Rate Explaination

Valid Extensions

For Video
•	.mov
•	.avi
•	.mpg
•	.mpeg
•	.mp4
•	.mkv
•	.wmv

For Image
•	.jpg, .jpeg
•	.png
•	.bmp
•	.tiff, .tif
•	.dicom, .dcm

How to use?
Minimal setting (Basic)
from Video2Pics import Video2Pics
Video2Pics(video_srcpath="--path-to-video-source file--",
            output_dir="--path-to-output-directory--")

Note:- The output will be saved in a pic_{timestamp}_count
Output Process Screenshot

Author
I will be happy to help and connect with you guys!!
Any suggestions are most welcome.

