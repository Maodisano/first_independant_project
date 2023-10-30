class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def count_words(self):
        
        check_words_count = self.contents.count(" ")+1
        return check_words_count


    def reading_time(self, wpm):
        if self.contents == "":
            raise Exception("Cannot calculate reading time for empty contents")
        
        time_to_read = self.count_words() / wpm 
        return time_to_read
    

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)