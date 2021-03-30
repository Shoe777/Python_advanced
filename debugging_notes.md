# What you need to do #

1. Make sure you can complete all the steps outlined in *Testing menu.py* below. This will not be as easy as it sounds. The code **HAS** errors that you will need to debug and fix. You can use *PDB*, *Pysnooper* or any other debugging techniques you like. **Make sure you capture your findings in a file called *debugging_notes.md*** (same metadata format used for this README file). This file **must be submitted with the rest of your work**.

## Testing *menu.py* ##

1. Load the users database.
   misprint at (user_collection)
   main.load_users(filename, user_selection) -> main.load_users(filename, user_collection)
   using *PDB* and set break point at line 12.
   
2. Add a new user and confirm you get a success message.
   User ID: Evgeny01
   User email: Evgeny.Shibaev@gmail.com
   User name: Evgeny
   User last name: Shibaev
User was successfully added
    
3. Try to add the same user ID again and confirm you get an error message.
   confirm: An error occurred while trying to add new user  

4. Update the name of an existing user.
   User ID: Evgeny01
   User email: Evgeny.Shibaev@gmail.com
   User name: Alex
   User last name: Shibaev
   
   recieved an error: update_user() missing 1 required positional argument: 'user_collection'
   neet to add "user_collection" at line 42: 
   
   Correction: -> if not main.update_user(user_id, email, user_name, user_last_name, user_collection):
   
   After this correction: "User was successfully updated"

5. Try to update the name of a non-existing user and confirm you get an error message.
	User ID: Evgeny
	User email: Evgeny.Shibaev@gmail.com
	User name: Alex
	User last name: Shibaev
An error occurred while trying to update user

6. Search for an existing user and return that user's email, name and last name.
	Enter user ID to search: Evgeny01
Error message: line 53, in search_user if not result.name:
	       AttributeError: 'Users' object has no attribute 'name'
correction: line: 53: -> if not result.user_name: (was: result.name)

	Enter user ID to search: evmiles97
	User ID: evmiles97
	Email: eve.miles@uw.edu
	Name: Eve
	Last name: Miles

7. Search for a non-existing user and return a message indicating that the user does not exist.
if not result.user_id -> was corrected -> if result is None:

	Enter user ID to search: Alex
	ERROR: User does not exist

8. Delete an existing user.
	User ID: evmiles97
	User was successfully deleted

9. Try to delete a non-existing user and confirm you get an error message.
	User ID: alex
	An error occurred while trying to delete user

10. Save the users database.
	Enter filename for users file: accounts_Mod.csv
	File was created as expected.

11. Load the status database.
	Enter filename for status file: status_updates.csv
	No issues.

12. Add a new status and confirm you get a success message.
	User ID: Evgeny
	Status ID: Evgeny_001
	Status text: Hello Python
	New status was successfully added

13. Try to add the same status ID again and confirm you get an error message.
	User ID: Evgeny
	Status ID: Evgeny_001
	Status text: DOuble Check
	An error occurred while trying to add new status

14. Update the text of an existing status ID.
	User ID: Evgeny
	Status ID: Evgeny_001
	Status text: Hello Python Update
	An error occurred while trying to update status

15. Try to update the text of a non-existing status ID and confirm you get an error message.
	User ID: Alex
	Status ID: Alex_001
	Status text: New Text
	Status was successfully updated

16. Search for an existing status ID and return the ID of the user that created the status and the status text.
	Enter status ID to search: evmiles97_00001
	User ID: evmiles97
	Status ID: evmiles97_00001
	Status text: Code is finally compiling

17. Search for a non-existing status ID and return a message indicating that the status ID does not exist.
	Enter status ID to search: Alex_001
	Error message: line 108, in search_status if not result.user_id:
		AttributeError: 'NoneType' object has no attribute 'user_id'

	corrections: if not result.user_id -> was corrected -> if result is None:

	Enter status ID to search: Alex_001
	ERROR: Status does not exist

18. Delete an existing status.
	Status ID: evmiles97_00001
	Status was successfully deleted
	
19. Try to delete a non-existing status and confirm you get an error message.
	Status ID: Alex_001
	An error occurred while trying to delete status
	
20. Save the status database.
	Enter filename for status file: status_updates_Mod.csv
	File was created as expected.

21. Make sure menu options are case-insensitive (i.e., typing "a" or "A" works in the same way).
    
    if you type lower case letter 'a' -> crush
    to fix it need to add ".upper()": menu_options[user_selection.upper()]()


The following files need to be submitted:

* *menu.py*
* *main.py* (Your starting code should be the file you modified for assignment 1).
* *users.py* (Your starting code should be the file you used for assignment 1).
* *user_status.py* (Your starting code should be the file you used for assignment 1).
* *debugging_notes.md*.
* *.pylintrc* (if using custom rules).



