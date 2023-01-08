import cv2
import argparse
import os


#input_file_dir="C:/Users/lulu/Desktop/workspace/pic/dock"
#output_file_dir='C:/Users/lulu/Desktop/workspace/pic/dock/pic1'


# 遍历该文件夹下的文件名称
def read_directory(directory_name):
    file_list = []
    for filename in os.listdir(directory_name):
        str = directory_name + '/' + filename
        file_list.append(str)
    return file_list


# 设置处理的帧数与文件位置，并整合。
def parse_args(input, output):
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # default为间隔多少帧截取一张图片
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=1, type=int)
    # input为输入视频的路径 ，output为输出存放图片的路径
    args = parser.parse_args(['--input', input, '--output', output])
    return args


# 处理帧数函数
def process_video(i, i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("该视频的总帧数为：", num_frame)
    expand_name = '.jpg'

    if not cap.isOpened():
        print("检查路径名")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        width = 640
        height = 480
        dim = (width, height)
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        cnt += 1
        if cnt % num == 0:
            count += 1
            cv2.imwrite(os.path.join(o_video, str(count) + expand_name), resized)
        if not ret:
            break


if __name__ == '__main__':
    # 命名不要带中文，可能报错
    intput = read_directory("C:/Users/lulu/Desktop/workspace/pic/dock")#改成自己的，注意斜杠方向
    output = 'C:/Users/lulu/Desktop/workspace/pic/dock/pic1'#改成自己的，注意斜杠方向
    print("该目录下共有：", len(intput), "个视频")
    i = 1
    for input_i in intput:
        args = parse_args(input_i, output)
        print("开始输出第", i, "个视频")
        process_video(i, args.input, args.output, args.skip_frame)
        print("第", i, "个视频处理完毕")
        print("-----------------------------------")
        i = i + 1
    print("汇总", len(intput), "个视频处理完毕")