# GH2GDrive

Automate downloading files from multiple sources and upload them directly to Google Drive using GitHub Actions.

This repository provides ready-to-use GitHub Actions workflows for:

- 📥 Direct download links → Google Drive
- 📺 YouTube videos/audio → Google Drive
- 💬 Telegram files → Google Drive

Everything runs on GitHub's hosted runners—no local server or VPS required.

---

## Features

- ✅ Download files from direct URLs
- ✅ Download YouTube videos or extract audio
- ✅ Download files from Telegram posts
- ✅ Upload directly to Google Drive
- ✅ Manual execution using GitHub Actions
- ✅ Standard and FAST workflow variants
- ✅ Supports custom filenames
- ✅ Supports Google Drive folder IDs, shared folder URLs, or folder paths

---

## Repository Structure

```
.github/
└── workflows/
    ├── direct2gdrive.yml
    ├── direct2gdrive_fast.yml
    ├── telegram2gdrive.yml
    ├── telegram2gdrive_fast.yml
    ├── youtube2gdrive.yml
    └── youtube2gdrive_fast.yml
```

---

# Required GitHub Secrets

Before running any workflow, configure the following repository secrets.

## Google Drive

| Secret | Description |
|---------|-------------|
| `GDRIVE_CLIENT_ID` | Google OAuth Client ID |
| `GDRIVE_CLIENT_SECRET` | Google OAuth Client Secret |
| `GDRIVE_REFRESH_TOKEN` | Google OAuth Refresh Token |

---

## Telegram (Telegram workflows only)

| Secret | Description |
|---------|-------------|
| `TG_API_ID` | Telegram API ID |
| `TG_API_HASH` | Telegram API Hash |
| `TG_SESSION` | Telegram session string |

---

# Available Workflows

## Direct Link → Google Drive

Downloads a file from a direct URL and uploads it to Google Drive.

Typical inputs:

- File URL
- Optional custom filename
- Download method
- Destination Google Drive folder

---

## YouTube → Google Drive

Downloads a YouTube video or extracts audio before uploading to Google Drive.

Typical inputs:

- Video URL
- Output format
  - MP4 (video)
  - MP3 (audio)
- Desired quality
- Destination Google Drive folder

---

## Telegram → Google Drive

Downloads media from a Telegram post and uploads it to Google Drive.

Typical inputs:

- Telegram post link
- Destination Google Drive folder
- Download method

---

# FAST Workflows

Each workflow has a corresponding **FAST** version.

These workflows are optimized for faster execution while providing the same functionality.

Examples:

- Direct Link → Google Drive (FAST)
- Telegram → Google Drive (FAST)
- YouTube → Google Drive (FAST)

---

# Usage

1. Fork this repository.
2. Add the required GitHub Secrets.
3. Open the **Actions** tab.
4. Select the desired workflow.
5. Click **Run workflow**.
6. Fill in the required inputs.
7. Wait for the workflow to finish.
8. Your files will be available in your Google Drive.

---

# Google Drive Folder Formats

The workflows accept any of the following:

- Folder ID
- Shared folder URL
- Folder path

Examples:

```
1AbCdEfGhIjKlMnOpQrStUvWxYz

https://drive.google.com/drive/folders/1AbCdEfGhIjKlMn

Movies

Downloads/Anime

Telegram/Movies
```

---

# Requirements

- GitHub account
- Google Drive API credentials
- Configured Google OAuth Refresh Token
- Telegram API credentials (Telegram workflows only)

---

# Notes

- Files are processed on GitHub-hosted runners.
- Large downloads may be limited by GitHub Actions runtime restrictions.
- Ensure your Google Drive account has sufficient storage space.
- Some download sources may impose their own rate limits or restrictions.

---

# License

This project is provided as-is. Feel free to modify and use it for your own workflows.
