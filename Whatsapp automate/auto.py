import pywhatkit
import time

# List of 15 phone numbers in international format (Nepal: +977)
numbers = [
    "+9779800596635",  # Trendy Corner
    "+9779818228568",  # Vastra Collection
    "+9779847346286",  # Moominfits
    "+9779700972073",  # Chiso Nepal
    "+9779840777909",  # Gadgets Ghar
    "+9779851061460",  # iStore Online Shopping
    "+9779823222399",  # Aroco Needs and Nutritions
    "+9779843567690",  # Revive Supplement Nepal
    "+9779706574914",  # Delivery All Over
    "+9779810035368",  # NPL Kart Store
    "+9779865498705",  # Timeless Legacy NP
    "+9779765779363",  # Hangger
    "+9779808072948",  # SS Clothing Nepal
    "+9779845328645",  # Gadget User
    "+9779828555133"   # Brand Castle
]

message =  """
🚀 Want to Take Your Shop Online Like a Pro?

Hey! 👋 I noticed you run an awesome store — whether it’s tech, clothes, gym gear, or other accessories.

What if I told you that you can get your own e-commerce website like this 👉 nepcart.vercel.app, fully secure, professional, and ready to boost your online sales?

Here’s what your shop will get:

🔒 Secure Login via Nepali Phone OTP  
📝 Signup, Login, Logout, Forgot Password  
🛍️ Add Unlimited Products (Name, Price, Description, Image)  
🔍 Powerful Search + Filters  
🛒 Smooth Add to Cart, Edit Quantity, Remove, Buy  
📍 Users can set Location, Place Orders Easily  
👤 User Profile Page (Track Orders, Cancel in 1hr, See Purchase History)  
👕 A Unique Custom T-shirt Page – Upload Design & Order  
🏆 Leaderboard of Top Buyers + Feedback Box  
📦 Full Order Tracking + Preview Before Buying  

For Sellers (Admin Panel):  
✅ Edit Product Price, Description, Name, Image  
✅ Add/Delete Products Anytime  
✅ See All Orders with Customer Contact  

📱 While others just create a TikTok page — you’ll have a full website!  
You’ll look more premium, more trusted, and reach 10x more customers.

💬 Curious about pricing or want to see the admin panel? Just message me! I’ll walk you through everything.

Let’s take your shop to the next level. Want to get started?
"""

# Send messages
for number in numbers:
    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
    time.sleep(15)  # delay between messages to avoid issues

print("All messages sent!")
