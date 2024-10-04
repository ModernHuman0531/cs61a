"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    """PESUDOCODE:
    valid_paragraph = []
    <repeat all the string in the paaragraphs>:
        if select is true:
            valid_paragraph[] = letter
        return the kth element , if k's element don't exist , then will return empty string
    """
    valid_paragraph = []
    for paragraph in paragraphs:
        if select(paragraph):
            valid_paragraph.append(paragraph)#valid_paragraph += paragraph if we write like this , the paragraph will divide into letter and store in that array , but that's not we want
    if k < len(valid_paragraph):
        return valid_paragraph[k]
    else:
        return ""

    
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    """It is obviously the  high order function , if we need to compare the paragraph word with topic , we must first remove all the punctuation , and then 
    spilt all the letter.
    PESUDOCODE:
    def select(paragraphs):
        1.clean up all the punctuation
        2.divide the paragraphs into the the letter
        3.compare the letters with topics , if exists return true , else return false
    
    return select
    """
    def select(paragraphs):
        Judge = False
        paragraphs = remove_punctuation(paragraphs)
        paragraphs = lower(paragraphs)
        paragraphs = split(paragraphs)
        for paragraph in paragraphs:
            if paragraph in topic:
                Judge = True
        return Judge
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """

    """PESUDOCODE:
    1.check out special condition , like the typed word is empty
    2.loop all the typed word to check if that match with the reference
    3.sum the matched word's number up , and divided by the total sum of the typed word
    """

    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    matched_num , index= 0 , 0
    if len(typed_words) == 0:
        return 0.0
    for letter in typed_words:
        if (len(reference_words) - 1) >= index: #This code is to check if the length of the reference_words is larger than index or not 
            if letter == reference_words[index]:
                matched_num += 1
            index += 1
    percentage = (matched_num / len(typed_words)) * 100
    return percentage
        
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    total_words = 0
    for letter in typed:
        total_words += 1
    typed_per_minute = (total_words / 5) * (60 / elapsed)
    return typed_per_minute
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """

    """PESUDOCODE:
    1.Handle the special case. (->if the user word is already contain in the valid word)
    2.find the smallest difference word in the valid word(hint: remember to use the min function)
    3.call the diff function
    4.retunrn the smallest difference
    
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        diff = [] #The array that store the number of difference between user_word and the valid_word
        for valid_word in valid_words:
            diff.append(diff_function(user_word , valid_word , limit))
        min_num = min(diff)
        if limit >= min_num:
            min_index = diff.index(min_num)
            return valid_words[min_index]
        else:
            return user_word

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line
    #Because we must keep track of the amount of difference , but  the total_diff isn't in the shifty_shifts function so we can use the high_order_function
    #to achieve the goal
    total = abs(len(start) - len(goal))
    def shifty_shift_helper(start , goal , total):
        if len(start) == 0 or len(goal) == 0:
            return total#Before it reach the base_case , it'll keep update the amount of the total difference. When reach the base case , it'll return total
        elif total > limit:
            return total 
        else:
            if start[0] != goal[0]:
                total += 1
            return shifty_shift_helper(start[1:] , goal[1:] , total)
    return shifty_shift_helper(start , goal ,total)
        
    

    return shifty_shift_helper(start , goal , total)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    #assert False, 'Remove this line'
    def pawssible_patches_helper(start , goal , diff_num):
        if len(start) == 0 or len(goal) == 0: # Fill in the condition
            # BEGIN
            "*** YOUR CODE HERE ***"
            return diff_num + abs(len(start) - len(goal))
            # END

        elif diff_num > limit: # Feel free to remove or add additional cases
            # BEGIN
            "*** YOUR CODE HERE ***"
            return diff_num
            # END
        elif start[0] == goal[0]:
            return pawssible_patches_helper(start[1:] , goal[1:] , diff_num)

        else:
            add_diff = pawssible_patches_helper(start , goal[1:] , diff_num + 1) # Fill in these lines
            remove_diff = pawssible_patches_helper(start[1:] , goal , diff_num + 1)
            substitute_diff = pawssible_patches_helper(start[1:] , goal[1:] , diff_num + 1)
            # BEGIN
            "*** YOUR CODE HERE ***"
            return min(add_diff , remove_diff , substitute_diff)
            # END
    return pawssible_patches_helper(start , goal , 0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    progress , index = 0 , 0
    for word in typed:
        if word == prompt[index]:
            progress += 1
        else:
            break
        index += 1
    progress /= len(prompt)
    report = {
        'id':user_id,
        'progress':progress
    }
    send(report)
    return progress

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word_helper(times_per_player , number_of_player):
    times = []
    player_num_range = range(number_of_player)
    time_num_range = range(len(times_per_player[0]) - 1)
    for i in player_num_range:
        player = []
        for j in time_num_range:
            delta_time = times_per_player[i][j + 1] - times_per_player[i][j]
            player.append(delta_time)
        times.append(player)
    return times

    


    
def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    number_of_player = len(times_per_player)
    times = time_per_word_helper(times_per_player , number_of_player)
    return game(words , times)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    """PESUDOCODE
    Create a list of lists , for each player to store the fastest word they typed
    loop for each word:
        append the fastest word they typed
    """
    times = all_times(game)
    result = []
    for i in player_indices:
        player = []
        for j in word_indices:
            min , index= 100000 , 0
            for k in player_indices:
                num  = times[k][j]
                if num < min:
                    min , index = num , k
            if index == i:
                player.append(word_at(game,j))
        result.append(player)
    return result
     

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)