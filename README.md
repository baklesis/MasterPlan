# MasterPlan
An automatic event scheduling desktop application.

**Run Instructions:**
Run main.py. Requires Pyside2 and Python 3.7 to run. 

**Log In Instructions:**
1. Enter organization using example organization "upatras".
2. a) Enter as admin using username "upatras" and password "1".
   b) Enter as organizer using username "makris" and password "1" OR username "alexiou" and password "1".
3. Switch between Grid and Calendar View using the respective buttons.
4. Select the edit button (pencil) after you log in to enter Edit Mode.

**Grid View Instructions:**
1. In Grid View select the building to enter from the grid.
2. After the rooms load in the grid, select a blue room to see its current event information. If the room is grey, there is currently no event being held.
3. Change floor using arrows in the floor spin box at the bottom of the grid.
4. Change building by selecting the "Go Back to Buildings" button at the bottom or the "Selected Building" drop down menu at the top.
5. Select a filter using the filter drop down menu.

**Calendar View Instructions:**
1. In Calendar View select a blue date from the calendar to see the events scheduled for that day. If the date is gray, there is no event scheduled for that day yet. Default date selected is today's date.
2. After selecting a date, double click an event from the list in the right to see its information.
3. Change building using the "Selected Building" Menu.
4. Select a filter using the filter drop down menu.
5. Download the calendar by selecting the download button at the bottom left.
6. Select a range for the calendar to be downloaded and click "ok" and then "yes". *(Currently no downloading happens)*

**Edit Mode Instructions:**
If you are logged in as an admin:

1. On Event List you can choose to Create Organizer.
2. On the pop-up Window type the name and email address for the new Organizer and finalize your action by clicking OK.
3. On Event List choose Create Event and enter the Name, duration ,Room Group and Tag    that corresponds to the  new event and save your actions.
4. On the list of events, by selecting an event, you can view the existing constraints-if any connected to.
5. By selecting to assign organizer, choose one from the list appearing on the pop-up window and assign them to the previously selected event.
6. You can also choose to add a Tag to the selected event.
7. By selecting the execute scheduling button on the buttom right section of the window. 
8. When the new schedule is created either publish it, or reset the scheduling to the previously existing one.

If you are logged in as an organizer:

1. Select an event on Event List. The constraints corresponding to the chosen event appear on the Event Details section.  
2. In the Time Constraint field select the add button.
3. On the pop-up window select the start/end dates and the repetition.
4. Set weight to ‘low’, ‘medium’ or ‘high’ on the slider and then choose Add to save the new constraint.
5. In the Tag Constraint field, add Tag and select one of the tags appearing on the pop-up window, along with its weight and save your   
actions.
6. In the Space Constraint field, fill the expected capacity of the event and update the constraint 


