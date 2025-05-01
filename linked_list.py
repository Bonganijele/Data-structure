class Node:
    def __init__(self, track_t, track_artist, track_d):
        self.track_t = track_t
        self.track_d = track_d
        self.track_artist = track_artist
        self.next = None


class PlayList:
    def __init__(self):
        self.head = None

    def add_track(self, track_t, track_artist, track_d):
        new_node = Node(track_t, track_artist, track_d)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display_playlist(self):
        current = self.head

        if not current:
            print("The playlist is empty.")
            return

        print("Playlist:")
        while current:
            print(f"Track: {current.track_t}, Artist: {current.track_artist}, Duration: {current.track_d}s")
            current = current.next

    def remove_track(self, track_t):
        current = self.head
        previous = None

        while current and current.track_t != track_t:
            previous = current
            current = current.next

        if current is None:
            print(f"Track '{track_t}' not found in playlist.")
            return

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Track '{track_t}' has been removed from playlist.")

    def find_song(self, track_t):
        current = self.head
        while current:
            if current.track_t == track_t:
                return current
            current = current.next
        return None

    def total_d(self):
        current = self.head
        total = 0
        while current:
            total += current.track_d
            current = current.next
        return total


# Example usage
p_list = PlayList()

p_list.add_track('track 1', 'zucci mane', 5)
p_list.add_track('track 2', 'bob marley', 150)
p_list.add_track('track 3', 'coi leeray', 2)
p_list.add_track('track 4', 'lil tecca', 5)

p_list.display_playlist()

p_list.remove_track('track 4')
p_list.display_playlist()

song = p_list.find_song('track 4')
if song:
    print(f"Found: {song.track_t} by {song.track_artist} ({song.track_d}s)")
else:
    print("Track not found.")

print(f"Total playlist duration: {p_list.total_d()} sec")