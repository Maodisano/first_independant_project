class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._entries.append(entry)
        

    def all(self):
        return self._entries

    def count_words_in_all_entries(self):
        all_words = 0 
        for entry in self._entries:
            all_words += entry.count_words() 
        return all_words 
            

    def total_reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:list
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_read_time = 0 
        for entry in self._entries:
            total_read_time += entry.reading_time(200)
        return total_read_time
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        words_user_can_read = wpm * minutes
        for entry in self._entries:
            if entry.count_words() <= words_user_can_read:
                return entry
