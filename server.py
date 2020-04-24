from pyfcm import FCMNotification



def uploadNotification(video_id, video_title, course):
    key = "AAAAhHPOtR4:......"

    push_service = FCMNotification(api_key=key)

    data = {

        "type":"upload",
        "video_title":video_title,
        "video_url":video_id,
        "click_action":"FLUTTER_NOTIFICATION_CLICK",
        "route":"youtube"
    }
    # Changed message_icon to  ['notification']['image'] field in library files for my use case
    result = push_service.notify_topic_subscribers(topic_name=course, message_title="A new video has been uploaded", message_body="Please tap on this notification to continue", data_message=data, message_icon=f"https://img.youtube.com/vi/{data['video_url']}/hqdefault.jpg")

    if result['success'] == 1:
        print("notification sent") 

if __name__ == "__main__":
    uploadNotification("LLxdzKgNYcQ","FireFlies : Owl City", "allusers")
