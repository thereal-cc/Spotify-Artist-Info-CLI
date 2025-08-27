# Spotify Artist Info CLI

A simple Python command-line tool that uses the [Spotipy](https://spotipy.readthedocs.io/) library to fetch and display information about an artist from Spotify.  

This script allows you to:  

- Search for an artist by name  
- Display the artist’s basic information (followers, genres, popularity)  
- Show their **5 most recent albums**  
- Show their **top 10 tracks**  

---

## Features  

✅ Search for an artist by name  
✅ View artist details (genres, followers, popularity)  
✅ Get the 5 most recent albums (no duplicates)  
✅ Get the artist’s top tracks  

---

## Requirements  

- Python 3.7+  
- A [Spotify Developer Account](https://developer.spotify.com/) with a registered application  
- A valid **Client ID** and **Client Secret**  

---

## Installation & Usage

1. Clone this repository or copy the script.  

   ```bash
   git clone https://github.com/thereal-cc/Spotify-Artist-Info-CLI.git
   cd spotify-artist-cli
   ```

2. Install dependencies:

   ``` bash
   pip install -r requirements.txt
   ```  

3. Create a .env file in the project directory and add your Spotify API credentials:

   ```bash
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

4. Run the script:

   ```bash
   python3 artist_info.py
   ```

# License

This project is open-source under the MIT License
