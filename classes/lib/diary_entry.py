
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.read_so_far = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        formmatted = f"{self.title}: {self.contents}"
        return formmatted
        

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        check_words_count = self.contents.count(" ")+1
        return check_words_count
        

    def reading_time(self, wpm):
        if self.contents == "":
            raise Exception("Cannot calculate reading time for empty contents")
        
        time_to_read = self.count_words() / wpm 
        return time_to_read
    
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
    

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)
