import cv2
import mediapipe as mp
from utils import calculate_angle

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture("input/test.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output/result.mp4", fourcc, fps, (width, height))

with mp_pose.Pose() as pose:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
            elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
            wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

            shoulder_point = [shoulder.x, shoulder.y]
            elbow_point = [elbow.x, elbow.y]
            wrist_point = [wrist.x, wrist.y]

            angle = calculate_angle(shoulder_point, elbow_point, wrist_point)

            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            cv2.putText(
                frame,
                f"Angle: {int(angle)}",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        out.write(frame)
        cv2.imshow("Pose", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()