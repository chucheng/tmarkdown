# tmarkdown.py

A template-based markdown enhancement.

The [markdown](http://daringfireball.net/projects/markdown/) is very powerful
but as the author said, I quote

>  The mardown is not intended to replace html


Markdown is easy to write, and easy to read as a writer.
However, to embed the html output of markdown to some html template could
be quite annoying in that copy-paste is quite cumbersome.  

Therefore, I create this enhancement script, aiming to help
markdown to **embed** its html output to a pre-defined html template (*.mdt).
In a word, it helps the merge by search replace a keyword ($content$) in your 
template file.

Author: Chu-Cheng Hsieh  
Contact: chucheng <at> ucla <dot> edu


## Installation

	sudo cp tmarkdown.py /usr/bin/tmarkdown
	sudo chmod 755 /usr/bin/tmarkdown
	
## Usage
Usage: tmarkdown [options] <markdown file>

Options:
  -h, --help            show this help message and exit
  -t FILE, --template=FILE
                        assign a specific template filename
  -k STRING, --keyword=STRING
                        the keyword to be replaced in the template,the default
                        is: $content$
  -o, --output_to_html  write output to a file (replace md with html &
                        overwrite existed file.
  -i, --keep_indent     Counting # of space in front of the keyword and indent
                        each line in output.


## Pre-req
Make sure you have markdown ready.

The markdown should be able to run by issuing

	markdown <filename>
	
in your shell.


## Configuration
Or you may edit the variable **g_markdown_cmd** [Setting] section in the tmarkdown.py.

By default the keyword is $content$. You may customize it as well.


## Note

If not template file is assigned, the default one is the file with the same base filename and
the extension **.mdt**

## Makefile

A example of Makefile:

	FILES=$(shell ls *.md)
	
	all: embed
			
	#run tmarkdown for all files
	embed: $(FILES)
		$(foreach f,$(FILES),tmarkdown --output_to_html --keep_indent $(f);)
	
	display: $(FILES)
		$(foreach f,$(FILES),tmarkdown $(f);)



## License

> This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

>This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

>You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.