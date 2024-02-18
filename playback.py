import cv2

def record_video(filename, duration=10):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    start_time = cv2.getTickCount()
    while cv2.waitKey(1) & 0xFF != ord('q'):
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('Recording...', frame)
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() >= duration:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def merge_videos(existing_video, recorded_video, output_video):
    cap1 = cv2.VideoCapture(existing_video)
    cap2 = cv2.VideoCapture(recorded_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, 20.0, (640, 480))

    while cap1.isOpened():
        ret1, frame1 = cap1.read()

        if not ret1:
            break

        out.write(frame1)
        cv2.imshow('Merged Video', frame1)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    while cap2.isOpened():
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        out.write(frame2)
        cv2.imshow('Merged Video', frame2)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap1.release()
    cap2.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Record video from webcam
    recorded_video = "recorded_video.mp4"
    record_video(recorded_video)

    # Existing video
    existing_video = "existing_video.mp4"

    # Output video
    output_video = "merged_video.mp4"

    # Merge recorded video with existing video
    merge_videos(existing_video, recorded_video, output_video)
