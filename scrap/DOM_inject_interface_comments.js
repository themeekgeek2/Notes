// Previous code
const widget=document.createElement('div');
widget.id='widget';
widget.innerHTML=`
<div class='header'>Placeholder</div>
<button id='run'>Test</button>`
document.appendChild;

/* Issue:

Console error "Uncaught HierarchyRequestError: Failed to execute 'appendChild' on 'Node': Only one element on document allowed.
at <anonymous>:1:159"
Explained: This console error usually appears when you put something in the DOM that is only supposed to appear once, and the browser is warning you that you tried to create a second element.
For example, the elements 'html', 'head' and 'body' can only appear once in a document. Also happens when: the <title> tag is injected inside <head>; you inject <style> or <link rel="stylesheet"> in a place where the browser doesn't expect (e.g. in the body). However, browsers allow for multiple 'style' tags.


Fix: Change 'document.appendChild;' to 'document.body.appendChild;'
The object 'document' isn't a DOM element, therefore it cannot have children appended to it directly.Only the <html> (the root) element is allowed inside 'document'.
Since it's a Document object (and at the very top of the DOM hierarchy), it's not a node that can have arbitrary children.

Browser basically interpreted like: "You're trying to add another top-level element to the document. Only one root element is allowed."
Referencing the DOM hierarchy (document->html->head, body), you can append elements to 'document.body', 'document.head' or any element inside them, just NOT to 'document' element itself.

    NOTE: (see first explanation) The elements <html>, <head> and <body are unique (can only have one), but their contents are not.
    Basically, as long as it's WITHIN any of those elements, the browser allows as many children you want.
    You can't create another <body> element (as a specific example), but you can put anything you want inside the existing one.

    ** Here's an analogy: 

        Think of DOM hierarchy like a house:
        House=document
        Foundation = <html>
        Two rooms = <head> and <body>

        You can't:
        * Add a second foundation
        * Add a second <head> room
        * Add a second <body> room
        But you CAN put furniture (appended elements) is just adding furniture.

        Appending elements to 'document.body' is just adding furniture.
        Appending elements to 'document' is trying to add a second house.
*/


// Second snippet:

widget.innerHTML = `
  <div class="widget-header">My Widget</div>
  <button>Run</button>`;

/* Issue:
Console prints "'\n  <div class="widget-header">My Widget</div>\n  <button>Run</button>\n'
" instead of displaying the button on the page.

Explanation: The chrome and firefox browser have "expression" (evaluates and prints a value) and "statement" (actually runs code) mode for their consoles. 
The pasted code either started with a newline (accidental space or indent) or had no newline, but Chrome interpreted the backtick string as a standalone template literal (which is returned like an expression and printed in the console); this means Chrome showed the evaluated value of the template literal instead of running the code.

This likely was a syntax or accidently adding other characters.

Fixes:
    * Make sure your paste does NOT start with a newline. Put the cursor at the end of a line and paste.
    * Add a semicolon before pasting. Helpful for Chrome.
    E.g. ';const widget=...'

    * Paste into the multi-line console using Shift+Enter. This forces "statement mode".
    * Wrap your code in curly brackets.
    E.g. '{const widget = ...}'


**Additional notes: 

In the context where you enter (likely accidently) a value or expression instead of a command,
    1) It reads the text as a string literal
    2) It preserves your line breaks
    3) It displays those breaks as escaped characters (\n)
    4) It prints the string back to you.
The console's showing you the invisible newlines that were already there.
*/


// Code that works 
const widget=document.createElement('div');
widget.id='widget';
widget.innerHTML = `
  <div class="widget-header">My Widget</div>
  <button>Run</button>
`;document.body.appendChild(widget);
