# Types of blocks
- paragraphs
- headlines (3 types)
- bold text
- highlighted block  
- quote blocks
- code block
- link 

These types of blocks can be used to style a blog post.

# 1. Paragraphs
Paragraphs are used to divide big blocks of text. Normal content should go into paragraph blocks.

They are used with <p> tag, which needs to be closed with </p>, example:
```
<p>This is a paragraph 1</p>
<p>This is the second paragraph. They will automatically be divided</p>
```

# 2. Headlines
There are 3 types of headlines to be used. 
h2 - big
h3 - medium
h4 - small

They are used this way:
```
<h2>Headline 2… </h2>
<p>Now, it’s time to explain what I mean by…</p>
<h3>Headline 3..,</h3>
<p>Subtopic of this headline…</p>
```

# 3. Bold text
Text in the paragraph can be made bold with <b> </b> tags. 
Example:
```
<p> This is a normal text while <b> this is bold </b> </p>
```

# 4. Highlighted block
A highlighted block is a portion of text in the paragraph with a background color that makes it more noticeable.

A highlighted block is used with <span>content</span> tags in a paragraph:
```
<p> This is normal text <span> while this is highlighted </span> </p>
```

# 5. Quote block 
A quote block is a block existing outside of a paragraph block and can be used with <blockquote> </blockquote> tags. Additionally, for the cite source, <cite> </cite> tags can be used.

Example:
```
<blockquote> The only kind of education is self-education </blockquote> 
<cite> Albert Einstein </cite>
```

When no cite block is given, "nocite" class should be added to the blockquote.
```
<blockquote class="nocite">The only kind of education is self-education </blockquote>
```

# 6. Code block 
A code block is a block existing outside of a paragraph block and can be used with pre & code tags.

Example:
```
<pre><code>
function Panel(element, canClose, closeHandler) { this.element = element; this.canClose = canClose; this.closeHandler = function () { if (closeHandler) closeHandler() }; }
</code></pre>
```

# 7. Link 
A link can exist in a normal paragraph block with <a href=”link”> </a> tags.

Example:
```
<p> This is a text with a <a href=”www.google.com” target=”_blank”>link. </a>
```

