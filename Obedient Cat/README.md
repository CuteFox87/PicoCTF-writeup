# PicoCTF2021 - Obedient Cat

## Information

Point Value: **5 points**

Catgory: **General Skills**

## Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](./flag).

## Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2. To get the file accessible in your shell, enter the following in the Terminal prompt:  
   ``$ wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag``
3. ``$ man cat``

## Solutions

### Windows:

將flag下載下來並透過文字編輯器開啟，常見的文字編輯器有 **記事本**、**notepad++**、**VScode** 等...

### Linux:

#### wget
在terminal中輸入  
``wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag``

#### cat
在terminal輸入  
``cat flag``

## Flag
``picoCTF{s4n1ty_v3r1f13d_28e8376d}``

## Concept
單純教你如何使用wget去下載資料
