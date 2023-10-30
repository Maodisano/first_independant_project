
class GrammarStats:
    def __init__(self):
        
        self.total_texts = 0
        self.passed_texts = 0
        

    def check(self, text):
        self.total_texts += 1
        if text == "":
            raise Exception("Cannot check grammar of empty string")
        if text[0].isupper() and text[-1] in ".?!":
            self.passed_texts += 1 
            return True 
        return False
        

        # passed_count = sum(1 for passed in text if self.check(text))
        # percentage_passed = (passed_count / len(text)) * 100
        # return int(percentage_passed)
    
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        


    def percentage_good(self):
        if self.total_texts == 0:
            return 0
        return (self.passed_texts / self.total_texts) * 100

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
    