import streamlit as st

st.markdown("""
# Welcome
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
####### Heading 7 (doesn't work)

*italics*

**bold**

| col1 | col 2 |
| --- | --- |
| 2 | 3 |
| 4 | 6 |

---

***phrase for bold italic***

> Block quote
This is a test

> Humm
>> nested blockquote

```
import streamlist as st

st.write("Awesome")
``` 
Here's a number: `42`

Unordered List
* one
* two
* three
  * indent
    * even more
      * and more
        * more still
          * wow
            * oh my
              * does this end?
                * hmm
                  * most surprising
                    * let's keep going
                      * again

Ordered List
1. one
1. two
1. three
    1. three-one
    1. three-two

[Google](https://google.com)

<https://google.com>

<eric@emelz.com>

![picleball paddle](https://proxrpickleball.com/cdn/shop/files/PinkProductImage-01.jpg?v=1700158303)
""")