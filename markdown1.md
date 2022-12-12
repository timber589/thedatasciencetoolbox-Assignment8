# Part 1a - Markdown files

In this assignment, each Markdown (.md) file needs to contain at least 4 of the following five components
- 2 block math equations
- 2 code blocks
- 2 image files
- 2 admonitions
- 1 margin content

## Block Math Equations
The example math equation from the course, "The Data Science Toolbox"  shows a math block of the total mass of Jupiter.

$$
  m_{j} \approx 1.9 \times 10^{27} \: \text{kg}
$$

This is written with MathJax which Jupyter-book uses to add LateX-style maths to the book.

Here's another example:
$
  E=mc^2
$

## Image Files
Markdown files can also hold image files such as the pictures of Jupiter the planet below:

```{figure} https://cdn.britannica.com/84/4284-050-16C7E8C2/Photograph-Jupiter-range-Voyager-1-cloud-bands-February-1-1979.jpg?w=300&h=300
---
height: 200px
name: jupiter-image1
---
Jupiter Image  from [Britannica website](https://www.britannica.com/place/Jupiter-planet)
```

## Admonitions

Admonitions are very similar to what I use in Notion for calling out items. In Notion, it would look like this:

``` {figure} https://pbs.twimg.com/media/D9W0mlpUwAE1TaD?format=jpg&name=small
---
height: 400px
name: notion-callout-image
---
Callout Block from Notion from [Twitter](https://twitter.com/notionhq/status/1141017380388085760?lang=en)
```

```{margin} Admonitions are very similar to Notions Callout Blocks. 
I think that Notion has copied a lot of Jupyter's features!
```

Admonitions on the other hand would look like this:
```{tip}
Remember to ping @Ivan Zhao for review before changing the status of this entry to completed.
```
or
```{note}
Remember to ping @Ivan Zhao for review before changing the status of this entry to completed.
```

if you wanted the lightbulb to look like an (i).

