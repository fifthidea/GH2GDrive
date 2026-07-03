from google_auth_oauthlib.flow import InstalledAppFlow
import json

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/drive']  # full Drive access

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)

# Use local server (opens browser once)
creds = flow.run_local_server(port=0)

print("\n=== Save these as GitHub secrets ===\n")
print("GDRIVE_CLIENT_ID =", creds.client_id)
print("GDRIVE_CLIENT_SECRET =", creds.client_secret)
print("GDRIVE_REFRESH_TOKEN =", creds.refresh_token)