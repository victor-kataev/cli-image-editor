# CLI image editor
Semester project of BI-PYT(Python programming) subject. The editor running via command line edits a given picture
according to specified options (see Usage) and saves the result to specified destination.



## Usage
Run
```shell script
python3 core/main.py [options] SRS_PATH DST_PATH
```
Options list:
- --rotate - rotates the image 90 degree clockwise
- --mirror - flips the image horizontally
- --inverse - represents the image in negative
- --bw - black-and-whites the image
- --lighten <0-100> - increases brightness on <0-100> percent
- --darken <0-100> - decreases brightness on <0-100> percent
- --sharpen - sharps the image

You can combine multiple options in arbitrary order.
