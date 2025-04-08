class Song:
  def __init__(self, song_name, song_artists):
    self.song_name = song_name
    self.song_artists = song_artists
    self.next = None
    self.prev = None

  def __str__(self):
    return f"{self.song_name}, by {', '.join(self.song_artists)}"

class Playlist:
  def __init__(self):
    self.current_playing_song = None
    self.head = None

  def __str__(self):
    current = self.head
    songs = []
    count = 1

    while current:
      songs.append(f"{count}. {current.song_name}, by {", ".join(current.song_artists)}")
      current = current.next
      count += 1

    return "\n".join(songs) if songs else "Playlist is empty."
  
  def _get_song_at_index(self, index):
    if index < 0:
      raise IndexError("Index must be a non-negative integer")

    current = self.head
    i = 0
  
    while current and i < index:
      current = current.next
      i += 1

    if current is None:
      raise IndexError(f"Index {index} is out of range")

    return current

  def insert(self, song_name, song_artists):
    new_song = Song(song_name, song_artists)

    if self.head is None:
      self.head = new_song
    else:
      current = self.head

      while current.next:
        current = current.next

      current.next = new_song
      new_song.prev = current

    return song_name
  
  def delete(self, index):
    song = self._get_song_at_index(index)

    if song.prev:
      song.prev.next = song.next
    else:
      self.head = song.next

    if song.next:
      song.next.prev = song.prev

    if self.current_playing_song == song:
      self.current_playing_song = None

    return song.song_name
      
  def play_song(self, index):
    self.current_playing_song = self._get_song_at_index(index)
    return self.current_playing_song
  
  def what_is_playing(self):
    if not self.current_playing_song:
      raise ValueError("No song is currently playing")
    
    print("Now playing:", self.current_playing_song)

    return self.current_playing_song.song_name
  
  def play_next_song(self):
    if not self.current_playing_song or not self.current_playing_song.next:
      raise ValueError("No next song to play")
    
    self.current_playing_song = self.current_playing_song.next
    return self.current_playing_song
  
  def play_previous_song(self):
    if not self.current_playing_song or not self.current_playing_song.prev:
      raise ValueError("No previous song to play")
    
    self.current_playing_song = self.current_playing_song.prev
    return self.current_playing_song
  
  
favorities = Playlist()

favorities.insert("Song 1", ["Artist 1", "Artist 2"])
favorities.insert("Song 2", ["Artist 1", "Artist 2"])
favorities.insert("Song 3", ["Artist 1", "Artist 2"])

favorities.play_song(0)
favorities.what_is_playing()

favorities.play_next_song()
favorities.what_is_playing()

favorities.play_previous_song()
favorities.what_is_playing()

favorities.play_next_song()
favorities.play_next_song()
favorities.what_is_playing()