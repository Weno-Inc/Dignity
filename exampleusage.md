This is some code written in Dignity:

```
A: header: | style: 1: #6278 2:#2827 | click: on-time |
B: h1: | style: 1: #6278 2:#2827 | click: on-time |
C: body: | style: 1: #6278 2:#2827 | click: on-time |
D: messages: | style: 1: #6278 2: #2827 | click: on-time |
Runner: A 1,2,3 | B 1,2,3 | C 1,2,3 | D 1,2,3 | 
```

How does this code work?

- Elements, keywords like header, h1, body and messages are the main components in this code.
- Properties, these are definitions of an element like the color, text-color, and interactivity like click.
- Labels, these are letters on the beggining of each line or numbers on the begining of each property.
- Runner, this is the required extra line that runs the code without having an interpreter, each run has an Element label and some Property labels.
