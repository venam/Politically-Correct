#!/usr/bin/python2
#encoding: utf-8

"""
Made by venam <patrick [at] iotek [dot] org>
COPYRIGHT AND PERMISSION NOTICE

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1.  The author is informed of the use of his/her code. The author does not have to consent to the use; however he/she must be informed.
    2.  If the author wishes to know when his/her code is being used, it the duty of the author to provide a current email address at the top of his/her code, above or included in the copyright statement.
    3.  The author can opt out of being contacted, by not providing a form of contact in the copyright statement.
    4.  If any portion of the author’s code is used, credit must be given.
            a. For example, if the author’s code is being modified and/or redistributed in the form of a closed-source binary program, then the end user must still be made somehow aware that the author’s work has contributed to that program.
            b. If the code is being modified and/or redistributed in the form of code to be compiled, then the author’s name in the copyright statement is sufficient.
    5.  The following copyright statement must be included at the beginning of the code, regardless of binary form or source code form.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Except as contained in this notice, the name of a copyright holder shall not
be used in advertising or otherwise to promote the sale, use or other dealings
in this Software without prior written authorization of the copyright holder.

Words credits to all the nice webistes on the internet
"""

import random

#Global
word_list    = open("words",'r').readlines()
punctuations = [
        "\n",
        ".",
        ",",
        ":",
        "&",
        "!",
        "?",
        "*",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "<",
        ">",
        ";",
        "'",
        "`",
        "%",
        "#",
        "$",
        "-",
        "_",
        "+",
        "=",
        "#",
        "@",
        "~",
        "\"",
        "|",
        "\\"
        ]


"""
polit_changer :: String -> String

takes a string and returns a politically correct equivalent based on the "word"
dictionary
"""
def polit_changer(the_string):
    #safe space at the end of the string to avoid unexpected errors
    the_string  = the_string+" "
    #create a special version of the string easier to search in
    easy_string = create_easy_string(the_string)

    #loop through the polically uncorrect wordlist
    for word in word_list:
        #for better matching
        
        #the list is composed of un-politically correct word: politically 
        #correct equivalent
        word        = word.split(":")
        uncorrect   = word[0].replace("\n","") #and make sure we don't get \n
        correct     = word[1].replace("\n","") #and make sure we don't get \n

        #check if the string starts with it or ends with it, a case that is not
        #catch by change_word()
        if easy_string.startswith(uncorrect+" "):
            to_replace = get_word_to_replace(correct, the_string[0])
            second_part_easy_string = easy_string[len(uncorrect):]
            easy_string = to_replace.upper()+second_part_easy_string
            second_part_string_normal = the_string[len(uncorrect):]
            the_string = to_replace + second_part_string_normal

        #replace the word in the string and get them back
        (easy_string, the_string) = change_word(
                easy_string, 
                the_string, 
                uncorrect, 
                correct
                )
    return the_string

"""
create_easy_string :: String -> String

takes a string and returns a lower case equivalent with spaces instead of 
punctuations and endlines.
"""
def create_easy_string(the_string):
    #lower it
    the_string_lower = the_string.lower()
    #remove all punctations by replacing them with spaces
    for char in punctuations:
        the_string_lower = the_string_lower.replace(char," ")
    return the_string_lower

"""
change_word :: String -> String -> String -> String -> (String, String)

takes the easy string, normal string, the word to find and the word to replace
with and returns the two first string with the new replaced words
"""
def change_word(easy_string, string_normal, word_to_find, word_to_replace):
    #we replace until we can't find the word in the string anymore
    #aka replace every instance of the word in the strings
    pos = easy_string.find(" "+word_to_find+" ")
    while pos != -1:
        #prepare the word to replace
        word_to_replace_new = get_word_to_replace(word_to_replace, string_normal[pos+1])

        #replace the word in the 2 strings
        #first the normal one ...
        first_part_string_normal  = string_normal[0:pos+1]
        second_part_string_normal = string_normal[pos+len(word_to_find)+1:]
        string_normal             = first_part_string_normal+word_to_replace_new+second_part_string_normal
        #... and the easy_one with an UPPER version of the word so it doesn't
        #get catch twice
        first_part_easy_string    = easy_string[0:pos+1]
        second_part_easy_string   = easy_string[pos+len(word_to_find)+1:]
        easy_string               = first_part_easy_string+word_to_replace_new.upper()+second_part_easy_string

        #recheck for another position of the word
        #if found it will re-loop
        pos           = easy_string.find(" "+word_to_find+" ")
    return (easy_string, string_normal)

"""
get_word_to_replace :: String -> Char -> String

Takes a word to replace and a char. It'll prepare it if it has multiple choices.
and check for the upper case
"""
def get_word_to_replace(word_to_replace, character):
    #split by ',' if has multiple answers
    if "," in word_to_replace:
        word_to_replace = word_to_replace.split(",")
        word_to_replace = random.choice(word_to_replace)
    if character.isupper():
        word_to_replace = word_to_replace[0].upper() + word_to_replace[1:]
    return word_to_replace


"""
main :: IO()

main procedure for testing

def main():
    the_file   = raw_input("\n\033[1;36m[\033[1;32m+\033[1;36m] \033[0mEnter a file that you want to be politically corrected:\n\033[1;32m=> ")
    the_output = raw_input("\n\033[1;36m[\033[1;32m+\033[1;36m] \033[0mEnter the output name:\n\033[1;32m=> ")
    the_file   = open(the_file,'r').read()
    the_file   = polit_changer(the_file)
    open(the_output,'w').write(the_file)
"""
"""
Test the program

main()
"""
