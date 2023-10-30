from lib.diary_ex import *

# when no entry is added, an empty list is returned 


def test_when_no_entry_added_return_empty_list():
    diary = Diary()
    diary.add("")
    assert diary.all() == [""]

    