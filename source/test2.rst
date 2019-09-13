程序设计
=========

lorem ipsum

Install the package (or add it to your ``requirements.txt`` file):

.. list-table:: This is a list table with images in it.

    * - .. figure:: https://sphinx-rtd-theme.readthedocs.io/en/stable/_images/yi_jing_01_chien.jpg

           This is a short caption for a figure.

      - .. figure:: https://sphinx-rtd-theme.readthedocs.io/en/stable/_images/yi_jing_01_chien.jpg

           This is a long caption for a figure. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
           Donec porttitor dolor in odio posuere, vitae ornare libero mattis. In lobortis justo vestibulum nibh aliquet, non.

fig
----

.. figure:: https://sphinx-rtd-theme.readthedocs.io/en/stable/_images/yi_jing_01_chien.jpg
   :align: center

img
----

.. image:: https://sphinx-rtd-theme.readthedocs.io/en/stable/_images/yi_jing_01_chien.jpg
   :target: https://cn.bing.com
Literal Blocks
--------------

Literal blocks are indicated with a double-colon ("::") at the end of
the preceding paragraph (over there ``-->``).  They can be indented::

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None

Or they can be quoted without indentation::

>> Great idea!
>
> Why didn't I think of that?

Line Blocks
-----------

| This is a line block.  It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
  they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

Take it away, Eric the Orchestra Leader!

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...

Block Quotes
------------

Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

tip
-----

.. Tip:: 15% if the service is good.

    +---------+
    | Example |
    +=========+
    | Thing1  |
    +---------+
    | Thing2  |
    +---------+
    | Thing3  |
    +---------+

hihihih

.. code-block:: python
   :linenos:
   :emphasize-lines: 3,5
   :caption: this is cap

   import hljs as hljs
   from hljs import hljs

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

.. parsed-literal::

    # parsed-literal test
    curl -O http://someurl/release-|version|.tar-gz


compound paragraph
--------------------

.. compound::

   This paragraph contains a literal block::

       Connecting... OK
       Transmitting data... OK
       Disconnecting... OK

   and thus consists of a simple paragraph, a literal block, and
   another simple paragraph.  Nonetheless it is semantically *one*
   paragraph.

guilabel
---------

:guilabel:`Some action`

downloadlink
---------------

:download:`This and should wrap white-spaces <https://cdn.bootcss.com/mathjax/2.7.6/latest.js>`