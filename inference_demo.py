import cv2
from geti_sdk.deployment import Deployment
from geti_sdk.utils import show_image_with_annotation_scene

if __name__ == "__main__":

    project_name = 'uk_licence_plates-int8'     # model name
    inference_target = 'CPU'                    # target hardware
    exit_key = 'q'                              # esc also works
    win_name = "Live Output"                    # window nanme
    # media = 'test.mp4'                        # can be video file
    media = 2                                   # or camera ID


    # Step 1: Load the deployment
    deployment = Deployment.from_folder(project_name)

    # Step 2: Load model onto target device
    deployment.load_inference_models(device=inference_target)

    #set up output display
    cv2.namedWindow(win_name, 0)

    #set up camera capture, change camera index for different devices
    cap = cv2.VideoCapture(media)
    
    while cap.isOpened():

        # Read images from the camera
        (ok, frame) = cap.read()
        if not ok:
            break

        # Step 3: Convert the colourspace
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Step 4: Infer image
        prediction = deployment.infer(image_rgb)

        # Step 5: Visualization
        output = show_image_with_annotation_scene(image_rgb, prediction, show_results=False)
        cv2.imshow(win_name, output)
        key = cv2.waitKey(1)
        if key == ord(exit_key) or key == 27:
            break

    cap.release()