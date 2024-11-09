# Extended WebElements Methods in Selenium Page Factory

from: https://pypi.org/project/selenium-page-factory/

## Methods Overview

| Method Name                                    | Description                                          |
|------------------------------------------------|------------------------------------------------------|
| `set_text(element, text)`                      | Sets the specified text into the element.           |
| `get_text(element)`                            | Retrieves the visible text from the element.        |
| `clear_text(element)`                          | Clears the text from the element.                   |
| `click_button(element)`                        | Clicks the specified button element.                |
| `double_click(element)`                        | Performs a double-click action on the element.      |
| `get_list_item_count(element)`                 | Returns the number of items in a list element.      |
| `select_element_by_text(select, text)`         | Selects an option from a dropdown by visible text.  |
| `select_element_by_index(select, index)`       | Selects an option from a dropdown by index.       |
| `select_element_by_value(select, value)`       | Selects an option from a dropdown by value.       |
| `get_all_list_items(element)`                  | Retrieves all items from a list element.            |
| `get_list_selected_item(element)`              | Gets the currently selected item in a list.         |
| `highlight(element)`                           | Highlights the element for better visibility.       |
| `is_enabled(element)`                          | Checks if the element is enabled.                   |
| `is_checked(element)`                          | Checks if a checkbox or radio button is checked.    |
| `get_attribute(element, attribute)`            | Gets the specified attribute of the element.        |
| `hover(element)`                               | Hovers over the specified element.                  |
| `visibility_of_element_located(locator)`       | Waits for an element to be visible.             |
| `invisibility_of_element_located(locator)`     | Waits for an element to become invisible.      |
| `element_to_be_clickable(locator)`             | Waits for an element to be clickable.               |
| `execute_script(script, element)`              | Executes a JavaScript script in the context of the element. |
| `context_click(element)`                       | Performs a right-click (context click) on the element. |
| `text_to_be_present_in_element(locator, text)` | Waits for specific text to be present in the element. |
| `click_and_hold(element)`                      | Clicks and holds the specified element.             |


