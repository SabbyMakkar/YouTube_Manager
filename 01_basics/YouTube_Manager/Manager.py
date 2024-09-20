import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    index=1
    print(videos)
    for video in videos:
        print(f"{index}. {video['name']}, Time: {video['time']}")
        index+=1

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the Number to update"))
    if 1<=index <=len(videos):
        name = input("Enter the new video name")
        time =input("Enter the new video time")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the Number to Delete"))
    if 1<= index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")
def main():
    videos = load_data()
    
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List of Favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube Video Details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
