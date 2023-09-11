import cv2

def video_to_frames(video_path, output_path, interval):
    # 打開影片檔案
    video = cv2.VideoCapture(video_path)

    # 檢查影片是否成功打開
    if not video.isOpened():
        raise Exception("無法讀取影片檔案")

    # 計數器，用於圖片檔案命名
    frame_count = 0

    # 計時器，控制截取間隔
    timer = 0

    # 逐幀讀取影片
    while True:
        # 讀取影格
        ret, frame = video.read()

        # 如果影格讀取失敗，則退出迴圈
        if not ret:
            break

        # 更新計時器
        timer += 1

        # 檢查計時器是否達到截取間隔
        if timer >= interval:
            # 保存影格為圖片
            frame_output_path = f"{output_path}/shrimp_{str(frame_count+46).zfill(4)}.jpg"
            cv2.imwrite(frame_output_path, frame)

            # 更新計數器
            frame_count += 1

            # 重置計時器
            timer = 0

    # 釋放影片物件和關閉視窗
    video.release()
    cv2.destroyAllWindows()

# 呼叫函式進行轉換，每0.5秒截取一張影格
video_to_frames('C:\\code\\shrimp_video\\input\\g7.MP4', 'C:\\code\\shrimp_video\\output', 15)  # 15 表示每秒30幀，0.5秒截取15幀
