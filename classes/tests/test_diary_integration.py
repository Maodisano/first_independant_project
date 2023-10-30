from lib.diary_ex import *
from lib.diary_ex_entry import * 


# when multiple entries are added, a list of them is returned 



def test_when_multiple_entries_are_added_they_are_returned_in_list():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "My Entry 1")
    entry_2 = DiaryEntry("Title 2", "My Entry 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


# when mulitple entries are added the word count of all entries is returned

def test_when_mulitple_entries_return_word_count_for_all():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "My Entry 1")
    entry_2 = DiaryEntry("Title 2", "My Entry 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words_in_all_entries() == 6

# when multiple entries added, return time takn to read all entries 

def test_with_multiple_entries_return_total_time_to_read():
    diary = Diary()
    words = " ".join(["word" for i in range(0, 200)])
    entry_1 = DiaryEntry("Title 1", words)
    entry_2 = DiaryEntry("Title 2", words)
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.total_reading_time(200) == 2.0

# when multiple entries added, return best entry for reading time if it is exact  

def test_with_multiple_entries_return_most_suitable():
    diary = Diary()
    words = " ".join(["word" for i in range(0, 400)])
    words = " ".join(["word" for i in range(0, 400)])
    words2 = " ".join(["word" for i in range(0, 200)])
    entry_1 = DiaryEntry("Title 1", words)
    entry_2 = DiaryEntry("Title 2", words)
    entry_3 = DiaryEntry("Title", words2)
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(200, 1) == entry_3

# when multiple entries added, return the closest entry the user can read (not over)

def test_with_multiple_entrie_suitable_time_returned():
    diary = Diary()
    words = " ".join(["word" for i in range(0, 400)])
    words2 = " ".join(["word" for i in range(0, 201)])
    words3 = " ".join(["word" for i in range(0, 199)])
    entry_1 = DiaryEntry("Title 1", words)
    entry_2 = DiaryEntry("Title 2", words2)
    entry_3 = DiaryEntry("Title 3", words3)
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(200, 1) == entry_3



