from lib.diary_entry import *
import pytest 

"""
Test if class instance reflect parameters
"""
# create a test for the initialliser


def test_if_formmated_class_is_return():
    diary_entry = DiaryEntry("title", "contents")
    assert diary_entry.format() == "title: contents"

def test_to_find_the_number_of_words_in_diaryentry():
    diary_entry = DiaryEntry("title", "Hi my name is bla")
    assert diary_entry.count_words() == 5

def test_to_check_time_taken__to_read_entry():
    diary_entry = DiaryEntry("title","my najkdksn kjfvnvdsv") #" ".join(["word" for i in range(0, 200)])
    assert diary_entry.reading_time(200) == 0.015

def test_with_200_word_contents_returns_one():
    words = " ".join(["word" for i in range(0, 200)])
    diary_entry = DiaryEntry("two hundred",words)
    assert diary_entry.reading_time(200) == 1.0 

def test_with_empty_contents_raise_exception():
    diary_entry = DiaryEntry("title", "")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(200)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time for empty contents"

# given a contents of six words 
# and a wpm of 2
# and minutes of 1
# reading chunk returns first two words

def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"


def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"




