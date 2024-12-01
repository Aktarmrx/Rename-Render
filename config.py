# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29538599")

API_HASH = os.environ.get("API_HASH", "b208ef895a7b942fb422db99633ad7a6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7774420156:AAGVI4sTnIVf_xzDNrri1KpCcRVgUGR7U2mongodb+srv://ssk376860:AC1bWUYfaDZtNXFb@cluster0.wkmdl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
mongodb+srv://ssk376860:AC1
FORCE_SUB = os.environ.get("FORCE_SUB", "A_animex") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ssk376860:AC1bWUYfaDZtNXFb@cluster0.wkmdl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5565530322').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
