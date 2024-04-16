# Import the TikTok module
import tiktok

def main():
    # Call functions from the TikTok module to perform specific actions
    
    # Step 1: Prompt the user to select a TikTok account
    selected_account = tiktok.select_account()
    
    # Step 2: Upload content for the TikTok post
    uploaded_file_path = tiktok.upload_content()
    
    # Step 3: Set caption for the TikTok post
    caption = tiktok.set_caption()
    
    # Step 4: Set hashtags for the TikTok post
    hashtags = tiktok.set_hashtags()
    
    # Step 5: Schedule the date and time for the TikTok post
    scheduled_datetime = tiktok.schedule_post()
    
    # Step 6: Preview the TikTok post
    tiktok.preview_post(selected_account, uploaded_file_path, caption, hashtags, scheduled_datetime)

# Entry point of the script
if __name__ == "__main__":
    main()
