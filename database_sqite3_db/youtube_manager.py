import sqlite3

# Establish connection
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create the videos table if it doesn't exist
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

# Function to list all videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# Function to add a new video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# Function to update an existing video
def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

# Function to delete a video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# Main function to handle the menu and user input
def main():
    while True:
        print("\nYouTube App Manager with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()
