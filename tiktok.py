# tiktok.py

def select_account():
    """
    Prompt the user to select a TikTok account (true crime or fun facts).
    Returns the selected account name.
    """
    print("Select a TikTok account:")
    print("1. True Crime")
    print("2. Fun Facts")
    
    while True:
        account_choice = input("Enter the number corresponding to your choice: ")
        
        if account_choice == "1":
            return "True Crime"
        elif account_choice == "2":
            return "Fun Facts"
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def upload_content():
    """
    Upload content for the TikTok post.
    Returns the file path of the uploaded content.
    """
    print("Upload content for the TikTok post.")
    file_path = input("Enter the file path of the video: ")
    
    # You can add validation here to ensure the file exists and is in a supported format
    
    return file_path

def set_caption():
    """
    Set caption for the TikTok post.
    Returns the caption entered by the user.
    """
    print("Set caption for the TikTok post:")
    caption = input("Enter the caption: ")
    return caption

def set_hashtags():
    """
    Set hashtags for the TikTok post.
    Returns a list of hashtags entered by the user.
    """
    print("Set hashtags for the TikTok post (separate multiple hashtags with spaces):")
    hashtags_input = input("Enter hashtags: ")
    hashtags = hashtags_input.split()
    return hashtags

def schedule_post():
    """
    Schedule the date and time for the TikTok post.
    Returns the scheduled date and time.
    """
    print("Schedule the date and time for the TikTok post (format: YYYY-MM-DD HH:MM):")
    scheduled_datetime = input("Enter the scheduled date and time: ")
    return scheduled_datetime

def preview_post(account, file_path, caption, hashtags, scheduled_datetime):
    """
    Preview the TikTok post before it's published.
    """
    print("Preview the TikTok post:")
    print("Account:", account)
    print("File path:", file_path)
    print("Caption:", caption)
    print("Hashtags:", hashtags)
    print("Scheduled date and time:", scheduled_datetime)
