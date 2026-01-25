import os
import logging
import pickle

demo_comment_data = "# This is a comment" # To add a comment to a python file
content_of_pickle_file = "" # To store data in pickle file
file_name_to_write_and_append = "demo_file.py" # Name of the python file to add the comment in
pickle_file_name = "demo_pickle.pkl" # Name of the pickle file to store data
number_of_comments = 0 # Number of comments in the file

try:
    if os.path.exists(file_name_to_write_and_append):
        # Create the file and write the comment
        with open(file_name_to_write_and_append, 'r') as f:
            content = f.read()
            number_of_comments = content.count('# ')
            f.close()
    else:
        with open(file_name_to_write_and_append, 'w') as f:
            input_lines = ""
            content = ""
            print("Enter '//' to stop adding text to the file.")
            while input_lines != '//':
                input_lines = input()
                if input_lines != '//':
                    content += input_lines + '\n'
            f.write(content)
            f.close()

            content_of_pickle_file = content
        
        with open(pickle_file_name, 'ab') as pkl_file:
            pickle.dump(content_of_pickle_file, pkl_file)
            pkl_file.close()

except Exception as e:
    logging.error(f" {e}")

finally:
    with open(file_name_to_write_and_append, 'a') as f:
        f.write('\n' + demo_comment_data)
        f.close()

# If number of comments exceed 5 (proving that the code has been executed for more than 5 times), delete the file
if number_of_comments > 5:
    os.remove(file_name_to_write_and_append)
    with open(pickle_file_name, 'rb') as pkl_file:
        loaded_content = pickle.load(pkl_file)
        print("Content from pickle file:")
        print(loaded_content)
        pkl_file.close()
else:
    print(number_of_comments)