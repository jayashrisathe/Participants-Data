participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]

def get_all_participants(participants_list):
    return [participant for inner_list in participants_list for participant in inner_list]


all_participants = get_all_participants(participants_list)


def daily_participants(participants_list):
    """Returns the list of all participants who participated everyday
    for the sample input, the right answer is
    ['Desmond', 'Krish', 'Sam']
    expected return object is a list of strings
    """
    daily_participants_lst = [participant for participant in set(all_participants) if all([participant in record for record in participants_list])]
    return daily_participants_lst


def one_time_participants(participants_list):
    """Returns the list of all participants who participated only once
    for the sample input, the right answer is
    ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
    expected return object is a list of strings
    """
    onetime_participants_lst = [participant for participant in set(all_participants) if all_participants.count(participant) == 1]
    return onetime_participants_lst


def first_day_only_participants(participants_list):
    """Returns the list of all participants who participated on the first day and never participated again.
    for the sample input, the right answer is
    ['John', 'Joan']
    expected return object is a list of strings
    """
    remaining_days_participants = get_all_participants(participants_list[1:])
    first_day_participants = [participant for participant in set(participants_list[0]) if participant not in remaining_days_participants]
    return first_day_participants


print("\nDaily participants:", daily_participants(participants_list))
print("\nOne time participants:", one_time_participants(participants_list))
print("\nFirst day participants only:", first_day_only_participants(participants_list))