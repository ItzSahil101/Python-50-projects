from instagrapi import Client

cl = Client()

# Login
cl.login("", "")

# Upload a photo
cl.photo_upload("upload.png", "testing python automation")

# Follow & unfollow
cl.user_follow(cl.user_id_from_username("sheryians_coding_school"))
cl.user_unfollow(cl.user_id_from_username("sheryians_coding_school"))

# Send a message
cl.direct_send("PYTHON AUTOMATION MSG", [cl.user_id_from_username("itx_sahil1110"), cl.user_id_from_username("amit.re4l_10")])

# Get followers
for follower_id in cl.user_followers(cl.user_id_from_username("sahil.not.found.z")):
    print(cl.user_info(follower_id).dict())

# Get following
for following_id in cl.user_following(cl.user_id_from_username("sahil.not.found.z")):
    print(cl.user_info(following_id).dict())
