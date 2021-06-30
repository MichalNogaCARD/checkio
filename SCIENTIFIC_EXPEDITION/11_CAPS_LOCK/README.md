 Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters. “Caps Lock” key is assumed to be initially off.

Input: A string. The typed text.

Output: A string. The showed text after being typed.

Example:
caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
caps_lock("Madder than Mad Brian of Madcastle") == "MDDER THn MD BRIn of MDCstle"
